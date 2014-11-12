# Vimrunner.py
Module that implements a client and server interface useful for controlling a 
vim server programatically. This module could be used for unit testing or 
integration testing for a vim plugin written in python. Or you can use it to 
interactively control a vim editor by python code, for example, in an ipython 
session.

## How it all started
I created a class that used the [vim python module]
(http://vimdoc.sourceforge.net/htmldoc/if_pyth.html#python-vim)
to emulate a vim buffer and that would act like a list, so you could read and 
write lines and manipulate text using python.

However, I stumbled across [Vimrunner](https://github.com/AndrewRadev/vimrunner)
which is a Ruby gem used to "spawn a Vim instance and control it 
programatically."

So, this python module is heavily inspired by the project mentioned above. 

## Instalation
There is a package on PyPI.org ...

## Usage
```python
import vimrunner

# initialize vim server
vim = vimrunner.Server()

# start GVIM as server and get a client connected to it
client = vim.start_gvim()
client.edit('any_file')
client.source('path/to/vim/plugin')
```

Documentation is available at http://andri-ch.readthedocs.org/en/latest/

For any suggestions regarding the module and its documentation, please submit 
an issue using [GitHub issue tracker]
(https://github.com/andri-ch/vimrunner.py/issues) 

