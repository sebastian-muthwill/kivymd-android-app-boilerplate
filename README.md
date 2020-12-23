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

For local development best use virtual environment [see here](https://docs.python.org/3/tutorial/venv.html).

Once venv is installed and activated install project requirements:

`pip install -r requirements.txt`

Now we are ready for a first test. Start the app with:

`python main.py`

If everything went well, you should now have a running KivyMD App.

## Next steps

From here on you can develop the app to your needs.
A good source to check out is [here](https://kivymd.readthedocs.io/en/latest/)


## Building Android apk

Before you start building the apk uncomment the following 2 lines in main.py file.
The android permissions obviously only work on android and are therefore commented initially. 

`# Remove the comment before apk build
from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA, Permission.INTERNET])`

The APK is best build on an linux system. I prefere here ubuntu but thats up to you.
I assume thet you will work within your home folder.


### prepare ubuntu system and load your app from your git repository

First we need to prepare the ubuntu systam and install some dependancies. 

`sudo apt update`
`sudo apt upgrade`

#### Install git and load your repository (optional)

If you forked the app and made your changes, then you can directly build from your repository. Otherwise you need to copy your files manually to the ubunt machine.

`sudo apt install git`

(Optional) Initiate password for git (not realy needed but helpfull):

`git config --global credential.helper store`

To set the password run a pull command afterwards, so we clone now the repository. 

`git clone <path to repo>`

#### install dependancies for Zbarscan (optional)

If you use the zbar scanner in your app then we need to install some depandancies.

`sudo apt install zlib1g-dev`

`sudo apt install gettext`

Go back to home folder

`cd ..`

### Buildozer install

First install dependancies for buildozer:

`sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev`

`pip3 install --upgrade Cython==0.29.19`
`export PATH=$PATH:~/.local/bin/`

Then clone buildozer:

`git clone https://github.com/kivy/buildozer.git`

`cd buildozer`

`sudo python setup.py install`

`cd ..`

### Run Buildozer

Now everything should be ready to build the APK. The build is spcified in the buildozer.spec file. For the first run the
settings should be fine but change it to your needs.

Change into the directory of your app:

`cd <kivy-path>`

and run the build:

`buildozer android debug`

Depending on your hardware this could take a while. Once finished, your apk will be in the /bin folder.

If you have problems with a second build, clear buildozer folder and try again. 

`rm -rf .buildozer`

## Contribution

If you want to contribute to the project fork, change a and create a pull request. 