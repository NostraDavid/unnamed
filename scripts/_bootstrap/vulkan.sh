#!/usr/bin/env bash

# source: https://vulkan.lunarg.com/doc/sdk/1.2.198.0/linux/getting_started_ubuntu.html
# There's also an archived version available, that I made on 2021-11-28, on https://web.archive.org
echo "== installing vulkan SDK for (WSL) Ubuntu 20.04 =="
echo "installing PGP key or something idk, it's from the documentation"
wget -qO - http://packages.lunarg.com/lunarg-signing-key-pub.asc | sudo apt-key add -
echo "get the installation list from LunarG (the peeps who maintain the vulkan SDK"
sudo wget -qO /etc/apt/sources.list.d/lunarg-vulkan-focal.list http://packages.lunarg.com/vulkan/lunarg-vulkan-focal.list
# updating silently
sudo apt update -q
echo "installing the vulkan-sdk"
sudo apt install vulkan-sdk -y

# These instructions come from https://github.com/gnsmrky/wsl-vulkan-mesa#install-mesa-and-run-vulkan-tools
sudo apt install llvm libxcb-randr0 libxcb-shm0 libxcb-xfixes0 mesa-utils vulkan-tools -y
VULKAN_MESA_TAR=wsl-ubuntu2004-vulkan-mesa20.3-20201220.tar.gz
wget "https://github.com/gnsmrky/wsl-vulkan-mesa/releases/download/v1.0/$VULKAN_MESA_TAR"
mkdir ~/mesa-local
tar xzvf $VULKAN_MESA_TAR -C ~/mesa-local
rm $VULKAN_MESA_TAR

echo "START MANUAL WORK"
echo "Alright, you're going to have to do something manually. Annoying, but necessary to get this program running on Ubuntu WSL"
echo "Protip: Use  this video for help: https://www.youtube.com/watch?v=4SZXbl9KVsw"
echo "Go to https://sourceforge.net/projects/vcxsrv/ and grab at least vcxsrv-64.1.20.9.0.installer.exe (or maybe higher) ON YOUR WINDOWS INSTALLATION"
echo "MAKE SURE THAT DURING INSTALLATION, ONCE YOUR GET THE FIREWALL POPUP, YOU GIVE vcxsrv PULIC ACCESS! IF YOU DON'T, THIS SHIT WON'T WORK, BECAUSE WSL HAS ITS OWN IP AND MORE TECHNICAL DETAILS THAT BORE ME TOO (THAT'S CODE FOR 'I HAVE NO IDEA WHY EITHER, IT'S JUST THE WAY IT IS!')"
echo "If you accidentally screw that up: Open the Firewall, go to Inbound Rules, find 'VcXsrv windows xserver' and make sure 'Profile' is set to 'Public' :)"
echo "After downloading, install vcxsrv by clicking the 'next' button until done."
echo "Do NOT start XLaunch via the shortcut - we're going to create a config file that's going to be used to launch vcxrv with the right settings."
echo "Create a new file, on your Windows desktop, with the name 'config.xlaunch' and copy/paste the next two lines into it:"
echo ""
echo '<?xml version="1.0" encoding="UTF-8"?>'
echo '<XLaunch WindowMode="MultiWindow" ClientMode="NoClient" LocalClient="False" Display="-1" LocalProgram="xcalc" RemoteProgram="xterm" RemotePassword="" PrivateKey="" RemoteHost="" RemoteUser="" XDMCPHost="" XDMCPBroadcast="False" XDMCPIndirect="False" Clipboard="True" ClipboardPrimary="True" ExtraParams="" Wgl="True" DisableAC="True" XDMCPTerminate="False"/>'
echo ""
echo "Now you can doubleclick that icon to start vcxsrv with the right settings, always. Otherwise you would need to go through a wizard, every time you start the program :'("
while read -r -p "Did you install and configure VcXsrv for Windows? [y/N] " response; do
    if [[ "$response" =~ ^([yY]|[yY][eE][sS])$ ]]; then
        echo "Thanks for following the instructions! :D"
        echo "END MANUAL WORK"
        # this grep command sets the $? variable to 0 (True) if that text already exists in your .bashrc
        grep -q 'export DISPLAY=$(grep -oP "(?<=nameserver ).+" /etc/resolv.conf):0' ~/.bashrc
        if [ ! $? ]; then
            # The original documentation said to use DISPLAY=:1, but https://github.com/microsoft/WSL/issues/4106 says to use the IP
            echo 'export DISPLAY=$(grep -oP "(?<=nameserver ).+" /etc/resolv.conf):0' >>~/.bashrc
        fi
        source ~/.bashrc
        break
    else
        echo "You *REALLY* need to do this to run this program on WSL on Windows..."
    fi
done

echo "overwriting mesa files (needed to make things work)"
sudo cp -R ~/mesa-local/usr/* /usr

# TODO(David) unfuck this; am not getting a return value
# glxinfo -B | grep -i 'version string' | grep Mesa
# TODO(David) unfuck this; too many errors :/
# vulkaninfo | grep -i deviceName
