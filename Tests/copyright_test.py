import os
import re
import pytest


def test_copyright_notice(plugin_dir, copyright_regex):
    """Test that all source files in the plugin have the correct copyright notice."""
    # Validate plugin path
    assert os.path.exists(plugin_dir), f"Plugin directory {plugin_dir} does not exist!"

    # Locate the Source directory
    source_path = os.path.join(plugin_dir, "Source")
    assert os.path.exists(source_path), f"Source directory not found in {plugin_dir}!"

    # Collect all source files
    source_files = []
    for root, _, files in os.walk(source_path):
        for file in files:
            if file.endswith((".cpp", ".h", ".cs")):
                source_files.append(os.path.join(root, file))

    assert source_files, "No source files (.cpp, .h, .cs) found in the Source directory!"

    # Collect failed files
    failed_files = []
    for file in source_files:
        with open(file, "r", encoding="utf-8-sig") as f:
            first_line = f.readline().strip()
            if re.match(copyright_regex, first_line):
                continue
            if not re.match(copyright_regex, first_line):
                failed_files.append(file)

    # Print all failed files if any
    if failed_files:
        error_message = "\n".join(failed_files)
        pytest.fail(f"The following files failed the copyright check:\n{error_message}")
