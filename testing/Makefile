CONFIG ?= stock_test_devices.toml
RUNNER := ./run_stock_test.sh --config $(CONFIG)

.PHONY: stock-test dry-run precompile-only clean-before-compile

stock-test:
	$(RUNNER)

dry-run:
	$(RUNNER) --dry-run

precompile-only:
	$(RUNNER) --precompile-only

clean-before-compile:
	$(RUNNER) --clean-before-compile
