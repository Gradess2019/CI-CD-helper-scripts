import argparse
import os
import re
from utils import Utils

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--unreal-directory", "-ud", type=str, required=True)
arg_parser.add_argument("--plugin-directory", "-pd", type=str, required=True)
arg_parser.add_argument("--destination", "-d", type=str, required=True)
arg_parser.add_argument("--submission", "-s", type=bool, default=False, required=False)
arg_parser.add_argument("--save-package-name", "-spn", type=bool, default=False, required=False)
args = arg_parser.parse_args()


unreal_directory = args.unreal_directory
plugin_directory = args.plugin_directory
destination = args.destination
submission = args.submission
save_package_name = args.save_package_name

print("Unreal directory: ", unreal_directory)
print("Plugin directory: ", plugin_directory)
print("Destination: ", destination)
print("Submission: ", submission)
print("Save package name: ", save_package_name)


unreal_version = re.search(r"(\d+\.\d+)", unreal_directory).group(1)
print("Unreal version: ", unreal_version)


plugin_descriptor = Utils.get_plugin_descriptor_path(plugin_directory)
print("Plugin descriptor: ", plugin_descriptor)

plugin_name = re.search(r"(\w+).uplugin", plugin_descriptor).group(1)
print("Plugin name: ", plugin_name)


package_name = ""
if submission:
    package_name = rf"{destination}\{plugin_name}Submission"
else:
    package_name = rf"{destination}\{plugin_name}"

print("Package name: ", package_name)

if save_package_name:
    print("Saving package name...")
    with open(rf"{plugin_directory}\package_name.txt", "w") as f:
        f.write(package_name)

run_uat_bat = rf"{args.unreal_directory}\Engine\Build\BatchFiles\RunUAT.bat"
build_plugin_cmd = rf'{run_uat_bat} BuildPlugin -Rocket -Plugin="{plugin_descriptor}" -Package="{package_name}"'

print("RunUAT.bat: ", run_uat_bat)
print("Build plugin command: ", build_plugin_cmd)

return_code = os.system(build_plugin_cmd)
if return_code != 0:
    print("Error!")
    exit(return_code)
else:
    print("Done!")
