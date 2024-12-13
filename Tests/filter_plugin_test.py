import os
import pytest


def test_filter_plugin_configuration(plugin_dir, filter_fields):
    if not filter_fields:
        pytest.skip("required_fields not specified, skipping test")
        return

    assert os.path.exists(plugin_dir), f"Plugin directory {plugin_dir} does not exist!"

    filter_ini_path = os.path.join(plugin_dir, "Config/FilterPlugin.ini")
    assert os.path.exists(filter_ini_path), f"FilterPlugin.ini not found in {plugin_dir}!"

    with open(filter_ini_path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    if ";" in filter_fields:
        filter_fields = filter_fields.split(";")
    else:
        filter_fields = filter_fields.split("\n")

    filter_fields = list(filter(None, filter_fields))
    filter_fields = [field.strip() for field in filter_fields]

    for field in filter_fields:
        assert field in lines, f"Field \"{field}\" not found in FilterPlugin.ini!"


