CONFIG ?= stock_test_devices.toml
RUNNER := ./run_stock_test.sh --config $(CONFIG)
UCAST_CONFIG ?= ucast_no_early_attach_test_devices.toml
UCAST_RUNNER := ./run_ucast_no_early_attach_test.sh --config $(UCAST_CONFIG)

.PHONY: stock-test dry-run precompile-only clean-before-compile ucast-no-early-attach-test ucast-no-early-attach-dry-run ucast-no-early-attach-precompile-only ucast-no-early-attach-clean-before-compile

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
