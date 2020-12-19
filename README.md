# KivyMD Boilerplate APP

The intention for this boilerplate is to have an easy starting point for android apps with material design.

# Building Android apk

The APK is best build on an ubuntu system. Therefor we need to install some dependancies. 

## prepare ubuntu system

`sudo apt update`
`sudo apt install git`

Initiate password for git (not realy needed but helpfull):

`git config --global credential.helper store`

To set the password run a pull command afterwards, so we clone now the repository. 

## load repo from Gitlab / Azure DevOps / Github

`git clone <path to repo>`

### install dependancies for Zbarscan

`sudo apt install zlib1g-dev`

`sudo apt install gettext`

Go back to home folder

`cd ..`

## Buildozer install

####  dependancies for buidozer

First install dependancies for buildozer

`sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev`

`pip3 install --upgrade Cython==0.29.19`
`export PATH=$PATH:~/.local/bin/`

`git clone https://github.com/kivy/buildozer.git`
`cd buildozer`
`sudo python setup.py install`

## Run Buildozer

Now everything should be ready to build the APK.

`cd <kivy-path>`
`buildozer android debug`

## Before rerun buildozer clear buildozer folder
`rm -rf .buildozer`