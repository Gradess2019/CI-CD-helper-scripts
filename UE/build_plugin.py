import argparse
import shutil
import os
import re
from utils import Utils

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--unreal-directory", "-ud", type=str, required=True)
arg_parser.add_argument("--plugin-directory", "-pd", type=str, required=True)
arg_parser.add_argument("--destination", "-d", type=str, required=True)
arg_parser.add_argument("--submission", "-s", action="store_true", required=False)
args = arg_parser.parse_args()


unreal_directory = args.unreal_directory
plugin_directory = args.plugin_directory
destination = args.destination
submission = args.submission

print("Unreal directory: ", unreal_directory)
print("Plugin directory: ", plugin_directory)
print("Destination: ", destination)
print("Submission: ", submission)


unreal_version = re.search(r"(\d+\.\d+)", unreal_directory).group(1)
print("Unreal version: ", unreal_version)

plugin_descriptor = Utils.get_plugin_descriptor_path(plugin_directory)
print("Plugin descriptor: ", plugin_descriptor)

plugin_name = re.search(r"(\w+).uplugin", plugin_descriptor).group(1)
print("Plugin name: ", plugin_name)

package_name = rf"{destination}\{plugin_name}"
print("Package name: ", package_name)

run_uat_bat = rf"{args.unreal_directory}\Engine\Build\BatchFiles\RunUAT.bat"
build_plugin_cmd = rf'{run_uat_bat} BuildPlugin -Rocket -Plugin="{plugin_descriptor}" -Package="{package_name}"'

print("Build plugin command: ", build_plugin_cmd)

return_code = os.system(build_plugin_cmd)

if return_code == 0 and submission:
    submission_package_name = rf"{destination}\{plugin_name}Submission"
    print("Submission package name: ", submission_package_name)

    if os.path.exists(submission_package_name):
        print("Submission package already exists! Deleting...")
        shutil.rmtree(submission_package_name)

    print("Copying package to submission package...")
    shutil.copytree(package_name, submission_package_name)

    print("Deleting Binaries and Intermediate folders...")
    binaries_path = os.path.join(submission_package_name, "Binaries")
    intermediate_path = os.path.join(submission_package_name, "Intermediate")

    if os.path.exists(binaries_path):
        shutil.rmtree(binaries_path)

    if os.path.exists(intermediate_path):
        shutil.rmtree(intermediate_path)

if return_code == 0:
    license_path = os.path.join(plugin_directory, "LICENSE.txt")
    if os.path.exists(license_path):
        print("Copying LICENSE.txt to package directory...")
        shutil.copy(license_path, package_name)

if return_code != 0:
    print("Error!")
    exit(return_code)
else:
    print("Done!")
