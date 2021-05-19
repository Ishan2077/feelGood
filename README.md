# feelGood
Elevate your mood!
 You can install the Project's files and can use IDE of your choice.
 
 NOTE: Please make sure Python 3.x is installed in your system!
 
 It is preferred to use Visual Studio Code here.
 To run the project, go to: https://kivy.org/#home
 
 Now you can go to https://kivy.org/doc/stable/gettingstarted/installation.html and from there, search for,
''' Using pip¶'''
The easiest way to install Kivy is with pip, which installs Kivy using either a pre-compiled wheel, if available, otherwise from source (see below).

Kivy provides pre-compiled wheels for the supported Python versions on Windows, OS X, Linux, and RPi. Alternatively, installing from source is required for newer Python versions not listed above or if the wheels do not work or fail to run properly.


<h4>Setup terminal and pip</h4>
Before Kivy can be installed, Python and pip needs to be pre-installed. Then, start a new terminal that has Python available. In the terminal, update pip and other installation dependencies so you have the latest version as follows (for linux users you may have to substitute python3 instead of python and also add a --user flag in the subsequent commands outside the virtual environment):

''' python -m pip install --upgrade pip setuptools virtualenv '''

<h4>Create virtual environment</h4>
Create a new virtual environment for your Kivy project. A virtual environment will prevent possible installation conflicts with other Python versions and packages. It’s optional but strongly recommended:

Create the virtual environment named kivy_venv in your current directory:

''' python -m virtualenv kivy_venv '''
Activate the virtual environment. You will have to do this step from the current directory every time you start a new terminal. This sets up the environment so the new kivy_venv Python is used.

<b>For Windows default CMD, in the command line do</b>:

'''kivy_venv\Scripts\activate'''

If you are in a bash terminal on Windows, instead do:
'''source kivy_venv/Scripts/activate'''

If you are in linux, instead do:
'''source kivy_venv/bin/activate'''

Your terminal should now preface the path with something like (kivy_venv), indicating that the kivy_venv environment is active. If it doesn’t say that, the virtual environment is not active and the following won’t work.

<h4>Install Kivy</h4>

Finally, install Kivy using one of the following options:

Pre-compiled wheels
The simplest is to install the current stable version of kivy and optionally kivy_examples from the kivy-team provided PyPi wheels. Simply do:

'''python -m pip install kivy[base] kivy_examples'''

<i>This also installs the minimum dependencies of Kivy. To additionally install Kivy with audio/video support, install either kivy[base,media] or kivy[full]. </i>
