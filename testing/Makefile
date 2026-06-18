CONFIG ?= stock_test_devices.toml
RUNS ?= 1
RUNNER := ./run_stock_test.sh --config $(CONFIG) --runs $(RUNS)
UCAST_CONFIG ?= ucast_no_early_attach_test_devices.toml
UCAST_RUNNER := ./run_ucast_no_early_attach_test.sh --config $(UCAST_CONFIG) --runs $(RUNS)
MCAST_CONFIG ?= mcast_no_early_attach_test_devices.toml
MCAST_RUNNER := ./run_mcast_no_early_attach_test.sh --config $(MCAST_CONFIG) --runs $(RUNS)

.PHONY: stock-test dry-run precompile-only clean-before-compile ucast-no-early-attach-test ucast-no-early-attach-dry-run ucast-no-early-attach-precompile-only ucast-no-early-attach-clean-before-compile mcast-no-early-attach-test mcast-no-early-attach-dry-run mcast-no-early-attach-precompile-only mcast-no-early-attach-clean-before-compile

stock-test:
	$(RUNNER)

dry-run:
	$(RUNNER) --dry-run

precompile-only:
	$(RUNNER) --precompile-only

clean-before-compile:
	$(RUNNER) --clean-before-compile

ucast-no-early-attach-test:
	$(UCAST_RUNNER)

ucast-no-early-attach-dry-run:
	$(UCAST_RUNNER) --dry-run

ucast-no-early-attach-precompile-only:
	$(UCAST_RUNNER) --precompile-only

ucast-no-early-attach-clean-before-compile:
	$(UCAST_RUNNER) --clean-before-compile

mcast-no-early-attach-test:
	$(MCAST_RUNNER)

mcast-no-early-attach-dry-run:
	$(MCAST_RUNNER) --dry-run

mcast-no-early-attach-precompile-only:
	$(MCAST_RUNNER) --precompile-only

mcast-no-early-attach-clean-before-compile:
	$(MCAST_RUNNER) --clean-before-compile
