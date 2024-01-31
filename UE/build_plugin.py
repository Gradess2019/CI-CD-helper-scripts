import argparse
import os
import re

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--unreal-directory", "-ud", type=str, required=True)
arg_parser.add_argument("--plugin-directory", "-pd", type=str, required=True)
arg_parser.add_argument("--destination", "-d", type=str, required=True)
arg_parser.add_argument("--submission", "-s", type=bool, default=False, required=False)
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


plugin_descriptor = ""
for file in os.listdir(plugin_directory):
    if file.endswith(".uplugin"):
        plugin_descriptor = rf"{plugin_directory}\{file}"
        break

plugin_name = re.search(r"(\w+).uplugin", plugin_descriptor).group(1)

print("Plugin name: ", plugin_name)
print("Plugin descriptor: ", plugin_descriptor)


package_name = ""
if submission:
    package_name = rf"{destination}\{plugin_name}Submission_{unreal_version}"
else:
    package_name = rf"{destination}\{plugin_name}_{unreal_version}"

print("Archive name: ", package_name)


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
