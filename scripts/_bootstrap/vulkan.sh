#!/usr/bin/env bash

# source: https://vulkan.lunarg.com/doc/sdk/1.2.198.0/linux/getting_started_ubuntu.html
# There's also an archived version available, that I made on 2021-11-28, on https://web.archive.org
echo "== installing vulkan SDK for Ubuntu 20.04 =="
echo "installing PGP key or something idk, it's from the documentation"
wget -qO - http://packages.lunarg.com/lunarg-signing-key-pub.asc | sudo apt-key add -
echo "get the installation list from LunarG (the peeps who maintain the vulkan SDK"
sudo wget -qO /etc/apt/sources.list.d/lunarg-vulkan-focal.list http://packages.lunarg.com/vulkan/lunarg-vulkan-focal.list
# updating silently
sudo apt update -q
echo "installing the vulkan-sdk"
sudo apt install vulkan-sdk -y
