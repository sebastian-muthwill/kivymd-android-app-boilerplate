# KivyMD Android App Boilerplate

The intention for this boilerplate is to have an easy starting point for android apps with material design.
The KV part is embeded withing the main file and all elements are created directly within KV without dynamic
creatinon with for loops. This makes it easier for beginners to start.

### App features

- QR / Barcode Scanner
- Navigation Drawer (Sidebar)
- 3 Pages

![Screenshot](docs/KivyMDBoilerplateScreenshot.png?raw=true "Screenshot")

## Local installation

For local development best use virtual environment. [see here](https://docs.python.org/3/tutorial/venv.html)

Once venv is installed and activated install project requirements:

`pip install -r requirements.txt`

Now we are ready for a first test. Start the app with:

`python main.py`

If everything went well, you should now have a running KivyMD App.

## Next steps

From here on you can develop the app to your needs. 


## Building Android apk

Before you start building the apk uncomment the following 2 lines in main.py file:

`# Remove the comment before apk build
from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA, Permission.INTERNET])`

The APK is best build on an ubuntu system. Therefor we need to install some dependancies. 

### prepare ubuntu system

`sudo apt update`
`sudo apt install git`

Initiate password for git (not realy needed but helpfull):

`git config --global credential.helper store`

To set the password run a pull command afterwards, so we clone now the repository. 

### load repo from Gitlab / Azure DevOps / Github

`git clone <path to repo>`

#### install dependancies for Zbarscan

`sudo apt install zlib1g-dev`

`sudo apt install gettext`

Go back to home folder

`cd ..`

### Buildozer install

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