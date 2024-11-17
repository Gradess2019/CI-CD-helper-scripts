import argparse
import os
from utils import Utils

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--package-directory", "-pd", type=str, required=True)
args = arg_parser.parse_args()

package_directory = args.package_directory

print("Package directory: ", package_directory)

plugin_descriptor = Utils.get_plugin_descriptor_path(package_directory)
print("Plugin descriptor: ", plugin_descriptor)

engine_version = Utils.extract_engine_version(package_directory)
print("Engine version: ", engine_version)

archive_path = rf'{package_directory}{("_" + engine_version)}.zip'
print("Archive path: ", archive_path)

if os.path.exists(archive_path):
    print("Archive already exists! Deleting...")
    os.remove(archive_path)

print("Archiving...")
archive_name = archive_path.replace(".zip", "")
new_archive_path = Utils.archive_directory(archive_name, package_directory)

print("Done!")
