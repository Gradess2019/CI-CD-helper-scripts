import pytest


def pytest_addoption(parser):
    """Add custom options for pytest."""
    parser.addoption("--plugin-dir", action="store", help="Path to the plugin directory")
    parser.addoption("--copyright-regex", action="store", help="Copyright notice regex")
    parser.addoption("--filter-fields", action="store", help="Required fields in FilterPlugin.ini")


@pytest.fixture
def plugin_dir(request):
    """Fixture to get plugin directory from pytest options."""
    return request.config.getoption("--plugin-dir")


@pytest.fixture
def copyright_regex(request):
    """Fixture to get copyright regex from pytest options."""
    return request.config.getoption("--copyright-regex")

@pytest.fixture
def filter_fields(request):
    """Fixture to get required fields from pytest options."""
    return request.config.getoption("--filter-fields")

