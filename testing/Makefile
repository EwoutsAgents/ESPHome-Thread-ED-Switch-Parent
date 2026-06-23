CONFIG ?= stock_test_devices.toml
RUNS ?= 1
RUNNER := ./run_stock_test.sh --config $(CONFIG) --runs $(RUNS)
UCAST_CONFIG ?= ucast_test_devices.toml
UCAST_RUNNER := ./run_ucast_test.sh --config $(UCAST_CONFIG) --runs $(RUNS)
MCAST_CONFIG ?= mcast_test_devices.toml
MCAST_RUNNER := ./run_mcast_test.sh --config $(MCAST_CONFIG) --runs $(RUNS)

.PHONY: stock-test dry-run precompile-only clean-before-compile ucast-test ucast-dry-run ucast-precompile-only ucast-clean-before-compile mcast-test mcast-dry-run mcast-precompile-only mcast-clean-before-compile

stock-test:
	$(RUNNER)

dry-run:
	$(RUNNER) --dry-run

precompile-only:
	$(RUNNER) --precompile-only

clean-before-compile:
	$(RUNNER) --clean-before-compile

ucast-test:
	$(UCAST_RUNNER)

ucast-dry-run:
	$(UCAST_RUNNER) --dry-run

ucast-precompile-only:
	$(UCAST_RUNNER) --precompile-only

ucast-clean-before-compile:
	$(UCAST_RUNNER) --clean-before-compile

mcast-test:
	$(MCAST_RUNNER)

mcast-dry-run:
	$(MCAST_RUNNER) --dry-run

mcast-precompile-only:
	$(MCAST_RUNNER) --precompile-only

mcast-clean-before-compile:
	$(MCAST_RUNNER) --clean-before-compile
