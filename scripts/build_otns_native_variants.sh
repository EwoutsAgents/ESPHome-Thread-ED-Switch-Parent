#!/usr/bin/env bash

set -euo pipefail

readonly BASE_OPENTHREAD_COMMIT="a12ff0d0f54fd41954b45047fcdd08f302731c5f"
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

: "${OPENTHREAD_REPOSITORY:?Set OPENTHREAD_REPOSITORY to a full OpenThread Git repository}"
: "${OTNS_RFSIM_DIR:?Set OTNS_RFSIM_DIR to the ot-ns/ot-rfsim directory}"
: "${OTNS_VARIANT_ROOT:?Set OTNS_VARIANT_ROOT to a new output directory}"

if [[ -n "${NINJA_BIN:-}" ]]; then
    if [[ ! -x "${NINJA_BIN}" ]]; then
        echo "NINJA_BIN is not executable: ${NINJA_BIN}" >&2
        exit 1
    fi
    export PATH="$(dirname "${NINJA_BIN}"):${PATH}"
elif ! command -v ninja >/dev/null 2>&1; then
    echo "Ninja is required; install it or set NINJA_BIN to its executable." >&2
    exit 1
fi

readonly COMMON_DEFINES="-DOPENTHREAD_CONFIG_PARENT_SEARCH_ENABLE=0"
readonly FASTPR_DEFINES="${COMMON_DEFINES} -DOPENTHREAD_CONFIG_EXPERIMENTAL_UNICAST_PARENT_RESPONSE_FASTPATH_ENABLE=1"

if [[ -e "${OTNS_VARIANT_ROOT}" ]]; then
    echo "Refusing to reuse existing variant root: ${OTNS_VARIANT_ROOT}" >&2
    exit 1
fi

mkdir -p "${OTNS_VARIANT_ROOT}"

create_source_variant()
{
    local profile="$1"
    shift
    local source_dir="${OTNS_VARIANT_ROOT}/${profile}/source"

    mkdir -p "${OTNS_VARIANT_ROOT}/${profile}"
    git clone --quiet --no-hardlinks --no-checkout "${OPENTHREAD_REPOSITORY}" "${source_dir}"
    git -C "${source_dir}" checkout --quiet --detach "${BASE_OPENTHREAD_COMMIT}"
    git -C "${source_dir}" submodule update --init --recursive

    local patch
    for patch in "$@"; do
        git -C "${source_dir}" apply "${REPO_ROOT}/${patch}"
    done
    git -C "${source_dir}" diff --check
}

build_variant()
{
    local profile="$1"
    local defines="$2"
    local source_dir="${OTNS_VARIANT_ROOT}/${profile}/source"
    local build_dir="${OTNS_VARIANT_ROOT}/${profile}/build"

    (
        cd "${OTNS_RFSIM_DIR}"
        OT_DIR="${source_dir}" \
        OT_CMAKE_BUILD_DIR="${build_dir}" \
        OT_CMAKE_NINJA_TARGET="ot-cli-mtd ot-cli-ftd" \
        ./script/build \
            "-DCMAKE_C_FLAGS=${defines}" \
            "-DCMAKE_CXX_FLAGS=${defines}"
    )
}

create_source_variant stock
create_source_variant preferred-parent \
    patches/otns/selected-parent-core.patch \
    patches/otns/preferred-parent-cli-controller.patch
create_source_variant preferred-parent-fastpr \
    patches/otns/selected-parent-core.patch \
    patches/otns/preferred-parent-cli-controller.patch \
    patches/otns/fast-unicast-parent-response.patch

build_variant stock "${COMMON_DEFINES}"
build_variant preferred-parent "${COMMON_DEFINES}"
build_variant preferred-parent-fastpr "${FASTPR_DEFINES}"

install -D -m 0755 \
    "${OTNS_VARIANT_ROOT}/stock/build/bin/ot-cli-mtd" \
    "${OTNS_VARIANT_ROOT}/artifacts/stock-mtd-pps-off/ot-cli-mtd"
install -D -m 0755 \
    "${OTNS_VARIANT_ROOT}/preferred-parent/build/bin/ot-cli-mtd" \
    "${OTNS_VARIANT_ROOT}/artifacts/preferred-parent-mtd-pps-off/ot-cli-mtd"
install -D -m 0755 \
    "${OTNS_VARIANT_ROOT}/stock/build/bin/ot-cli-ftd" \
    "${OTNS_VARIANT_ROOT}/artifacts/stock-ftd/ot-cli-ftd"
install -D -m 0755 \
    "${OTNS_VARIANT_ROOT}/preferred-parent-fastpr/build/bin/ot-cli-ftd" \
    "${OTNS_VARIANT_ROOT}/artifacts/fastpr-ftd/ot-cli-ftd"

sha256sum \
    "${OTNS_VARIANT_ROOT}/artifacts/stock-mtd-pps-off/ot-cli-mtd" \
    "${OTNS_VARIANT_ROOT}/artifacts/preferred-parent-mtd-pps-off/ot-cli-mtd" \
    "${OTNS_VARIANT_ROOT}/artifacts/stock-ftd/ot-cli-ftd" \
    "${OTNS_VARIANT_ROOT}/artifacts/fastpr-ftd/ot-cli-ftd"
