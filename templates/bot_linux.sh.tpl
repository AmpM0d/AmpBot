#!/bin/sh
# Go to the root project directory
cd "$(dirname $0)/.."
# Run the main file with only {{prettyname}}
sh start.sh {{name}}