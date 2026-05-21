PYTHON ?= ../venv/bin/python
RUNNER := scripts/run_stock_test.py
CONFIG ?= stock_test_devices.toml

.PHONY: dry-run run-stock

dry-run:
	$(PYTHON) $(RUNNER) --config $(CONFIG) --dry-run

run-stock:
	$(PYTHON) $(RUNNER) --config $(CONFIG)
