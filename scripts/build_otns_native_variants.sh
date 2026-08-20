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

readonly STOCK_DEFINES="-DOPENTHREAD_CONFIG_PARENT_SEARCH_ENABLE=0 -DOPENTHREAD_CONFIG_EXPERIMENTAL_PREFERRED_PARENT_ENABLE=0"
readonly PREFERRED_DEFINES="-DOPENTHREAD_CONFIG_PARENT_SEARCH_ENABLE=0 -DOPENTHREAD_CONFIG_EXPERIMENTAL_PREFERRED_PARENT_ENABLE=1"

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
    local targets="$3"
    local source_dir="${OTNS_VARIANT_ROOT}/${profile}/source"
    local build_dir="${OTNS_VARIANT_ROOT}/${profile}/build"

    (
        cd "${OTNS_RFSIM_DIR}"
        OT_DIR="${source_dir}" \
        OT_CMAKE_BUILD_DIR="${build_dir}" \
        OT_CMAKE_NINJA_TARGET="${targets}" \
        ./script/build \
            "-DCMAKE_C_FLAGS=${defines}" \
            "-DCMAKE_CXX_FLAGS=${defines}"
    )
}

create_source_variant stock
create_source_variant stock-delay-diagnostic \
    patches/canonical/parent-response-delay-diagnostic.patch
create_source_variant preferred-parent \
    patches/canonical/openthread-preferred-parent-controller.patch \
    patches/otns/preferred-parent-cli-adapter.patch

build_variant stock "${STOCK_DEFINES}" "ot-cli-mtd ot-cli-ftd"
build_variant stock-delay-diagnostic "${STOCK_DEFINES}" "ot-cli-ftd"
build_variant preferred-parent "${PREFERRED_DEFINES}" "ot-cli-mtd"

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
    "${OTNS_VARIANT_ROOT}/stock-delay-diagnostic/build/bin/ot-cli-ftd" \
    "${OTNS_VARIANT_ROOT}/artifacts/stock-ftd-delay-diagnostic/ot-cli-ftd"
readonly HASHES_FILE="${OTNS_VARIANT_ROOT}/artifacts/SHA256SUMS"
sha256sum \
    "${OTNS_VARIANT_ROOT}/artifacts/stock-mtd-pps-off/ot-cli-mtd" \
    "${OTNS_VARIANT_ROOT}/artifacts/preferred-parent-mtd-pps-off/ot-cli-mtd" \
    "${OTNS_VARIANT_ROOT}/artifacts/stock-ftd/ot-cli-ftd" \
    "${OTNS_VARIANT_ROOT}/artifacts/stock-ftd-delay-diagnostic/ot-cli-ftd" | tee "${HASHES_FILE}"

readonly COMPILER_PATH="$(sed -n 's/^CMAKE_C_COMPILER:FILEPATH=//p' "${OTNS_VARIANT_ROOT}/stock/build/CMakeCache.txt" | head -n 1)"
readonly COMPILER_VERSION="$(${COMPILER_PATH} --version | head -n 1)"
readonly PROVENANCE_FILE="${OTNS_VARIANT_ROOT}/artifacts/PROVENANCE.txt"
{
    echo "openthread_commit=${BASE_OPENTHREAD_COMMIT}"
    echo "compiler=${COMPILER_VERSION}"
    echo "parent_rank_instrumentation=disabled"
    echo "profile=stock-mtd-pps-off pps=0 preferred_parent=0 defines=${STOCK_DEFINES}"
    echo "profile=preferred-parent-mtd-pps-off pps=0 preferred_parent=1 defines=${PREFERRED_DEFINES}"
    echo "profile=stock-ftd pps=n/a preferred_parent=0 defines=${STOCK_DEFINES}"
    echo "profile=stock-ftd-delay-diagnostic pps=n/a preferred_parent=0 parent_response_delay_diagnostic=1 defines=${STOCK_DEFINES}"
    sha256sum \
        "${REPO_ROOT}/patches/canonical/openthread-preferred-parent-controller.patch" \
        "${REPO_ROOT}/patches/otns/preferred-parent-cli-adapter.patch" \
        "${REPO_ROOT}/patches/canonical/parent-response-delay-diagnostic.patch"
} > "${PROVENANCE_FILE}"

cat "${PROVENANCE_FILE}"
