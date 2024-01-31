import os
import re
import shutil


class Utils:

    @classmethod
    def get_plugin_descriptor_path(cls, plugin_directory: str):
        for file in os.listdir(plugin_directory):
            if file.endswith(".uplugin"):
                return rf"{plugin_directory}\{file}"

        assert False, "Plugin descriptor not found!"

    @classmethod
    def extract_engine_version(cls, package_directory: str):
        plugin_descriptor = cls.get_plugin_descriptor_path(package_directory)
        with open(plugin_descriptor, "r") as f:
            for line in f.readlines():
                version = re.search(r"(\"EngineVersion\".+?)(\d\.\d)", line)
                if version:
                    return version.group(2)

        assert False, "Engine version not found!"

    @classmethod
    def archive_directory(cls, archive_name: str, directory: str):
        return shutil.make_archive(archive_name, "zip", directory)
