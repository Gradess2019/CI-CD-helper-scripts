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
plugin_name = os.path.basename(plugin_directory)

print("Unreal version: ", unreal_version)
print("Plugin name: ", plugin_name)


plugin_descriptor = ""
for file in os.listdir(plugin_directory):
    if file.endswith(".uplugin"):
        plugin_descriptor = rf"{plugin_directory}\{file}"
        break

print("Plugin descriptor: ", plugin_descriptor)


archive_name = ""
if submission:
    archive_name = rf"{destination}\{plugin_name}Submission_{unreal_version}.zip"
else:
    archive_name = rf"{destination}\{plugin_name}_{unreal_version}.zip"

print("Archive name: ", archive_name)


run_uat_bat = rf"{args.unreal_directory}\Engine\Build\BatchFiles\RunUAT.bat"
build_plugin_cmd = rf"{run_uat_bat} BuildPlugin -Rocket -Plugin={plugin_descriptor} -Package={archive_name}"

print("RunUAT.bat: ", run_uat_bat)
print("Build plugin command: ", build_plugin_cmd)

os.system(build_plugin_cmd)

print("Done!")
