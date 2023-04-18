
We will start with getting you a working version of the software for you to play with.
To do this we will be using git:
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Once you have git installed open a terminal and navigate to a dirctory where you want to get your play copy of the code.
Here you use the following prompt to clone the code into the directory:

'''console
git clone <path-to-the-code>
'''

Congratualtions! you now have the code in a saft space for you to play with. 
Make sure to cd (change directory) into the code directory, as git clone creates a directory when you clone.

## Before you start playing
lets get you dressed up as a model citizen with a nice safe virtual-environment.
Do this with the virtualenv package that you can install with the following prompt:
'''console
pip install virtualenv
'''


## setting up you env
The next command will setup a virtual environment.
Packages installed in the virtual environment will keept from you already installed packages.
It will also keep you saf from most version conflicts and other funky effects.

OBS: besure to naviga
'''console
python -m venv env
'''

When you used the above command, it creates a new directory.. but do not worry.
GIT has been instructed to ignore all folders named "env" (we did this with a .gitignore file)
Your virtual environment is not synced with the source code, and remain on your local space.


## Activate the virtual environment

on a windows computer you can active you virtual enviroment by using the following promt:
concole'''
./env/Script/active
'''

Now you are ready to play :)



Currently you run the program by the following prompt:
'''console
python src/main.py
'''

