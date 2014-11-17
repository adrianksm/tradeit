tradeit
=======

A simple, multiplayer game based on the ideas of 'Up for Grabs!' on the Spectrum
=======

TO install on Ubuntu
First you must have git installed:

```
sudo apt-get install git
```


We are going to use a python Virtual environment.
```
sudo apt-get install python-virtualenv
```
Now, create a new directory that will hold your 'virtualenv'
e.g:
```
mkdir /home/adrian/tradeitENV
```
create your virtualenv inside this directory:
```
cd /home/adrian/tradeitEnv

virtualenv .  <-- note the dot is important!
```

This will create some directories and copy the important python files and place them withing your virtual environment. you can check this with a simple directory listing:

```
ls -la
adrian@adrian-Vbox:~/tradeitENV$ ls -la
total 24
drwxrwxr-x 6 adrian adrian 4096 Nov 17 09:25 .
drwxrwxr-x 3 adrian adrian 4096 Nov 17 09:17 ..
drwxrwxr-x 2 adrian adrian 4096 Nov 17 09:25 bin
drwxrwxr-x 2 adrian adrian 4096 Nov 17 09:25 include
drwxrwxr-x 3 adrian adrian 4096 Nov 17 09:25 lib
drwxrwxr-x 2 adrian adrian 4096 Nov 17 09:25 local
```


Now, clone the repository
```
git clone https://github.com/adrianksm/tradeit.git
```

Create a .gitignore file

```
touch tradeit/.gitignore  <-- don't miss the dot!
```

add *.pyc to the .gitignore file using your text editor
Check it like this: (This is so you don't add loads of python compile files to the repo when you 'git push')

```
(tradeitENV)adrian@adrian-Vbox:~/tradeitENV$ cat tradeit/.gitignore 
*.pyc

```

Now run the game:

```
cd tradeit
python play.py
```

