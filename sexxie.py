#!/usr/bin/env python

import argparse
import subprocess
from os import listdir
from os.path import isfile, join

print('\n\nSecSIE :: Security State Inspection Engine\n\n')

plugins = []
parser = argparse.ArgumentParser(description='SecSIE :: Security State Inspection Engine')
parser.add_argument('--plugin', action='append', dest='plugin_to_run', help='Specify a single plugin to run. Option may be repeated multiple times.')
parser.add_argument('--plugins-dir', action='store', dest='plugins_dir', default='plugins', help='Specify the plugins directory.')
parser.add_argument('--profile', action='store', dest='profile', default='default', help='Specify the Authentication Profile to use for connecting to cloud provider API')
args = parser.parse_args()

if args.plugin_to_run is not None:
  plugins = [plugin for plugin in sorted(args.plugin_to_run) if isfile(join(args.plugins_dir, plugin))]
  if not plugins:
    raise KeyError('At least one valid plugin is required')
else:
  plugins = [plugin for plugin in sorted(listdir(args.plugins_dir)) if isfile(join(args.plugins_dir, plugin))]
  if not plugins:
    raise KeyError('At least one valid plugin is required')

print('Executing the following plugins:\n{!r}\n\n'.format(plugins))
for plugin in plugins:
  if subprocess.call([join(args.plugins_dir, plugin), args.profile]):
    raise ValueError(plugin + ' plugin has failed')
  else:
    print(plugin + ' plugin has ensured security state successfully\n\n')

