# TODO: Clean up or delete as appropriate

# Installing Python

#Anaconda

You can install Python with all of the relevant libraries by using the Anaconda installation package.

More detailed instructions are here: http://continuum.io/downloads

```sh
wget http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-1.6.0-MacOSX-x86_64.sh
bash Anaconda-1.6.0-MacOSX-x86_64.sh
```

Note: If wget is not installed, try `brew install wget`, if brew is not installed, down the file from http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-1.6.0-MacOSX-x86_64.sh

##Other Installation Options

If do not want the full Anaconda package, there are other ways to install Python as well.  1) You probably have it by default, but you may want to upgrade it.


If you have brew:
```sh
brew install python
```

If not:

###Installing Packages
If you chose not to install Anaconda but want to install some of the packages, the best options are `pip` or `easy_install`.  `easy_install sometimes requires root permissions, so might be more difficult to use.

```sh
brew install easy_install 

OR

brew install pip
```

Once those are installed you can use them to install Python packages as follows:

```sh
pip install numpy
pip install scipy
pip install scikit.learn

OR
easy_install numpy
easy_install scipy
easy_install scikit.learn
```

###VirtualEnv
If you are using Python actively for other purpose, you may not want to upgrade Python without some safety. Some of the packages we use might require a more modern Python/ Virtual environments allow you to do that (as does Anaconda).
