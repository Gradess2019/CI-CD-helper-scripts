import os
import re
import pytest


def pytest_addoption(parser):
    """Add custom options for pytest."""
    parser.addoption("--plugin-dir", action="store", help="Path to the plugin directory")
    parser.addoption("--copyright-regex", action="store", help="Copyright notice regex")


@pytest.fixture
def plugin_dir(request):
    """Fixture to get plugin directory from pytest options."""
    return request.config.getoption("--plugin-dir")


@pytest.fixture
def copyright_regex(request):
    """Fixture to get copyright regex from pytest options."""
    return request.config.getoption("--copyright-regex")

