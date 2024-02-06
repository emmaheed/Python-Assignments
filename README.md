# How to get started with python
1. Install [python](https://www.python.org/downloads/) or for mac `brew install python3`.
2. Install the package handler [pip](https://pip.pypa.io/en/stable/installation/#get-pip-py).
3. `python3 -m pip install --upgrade pip`: Upgrade pip
4. Create a virtual environment with the command `python3 -m venv -venv` in the root directory of the project. When the virtual environment is created, it copies all the global packages at the computer.    
5. Activate the virtual environment by writing the command `source venv/bin/activate`
6. Use the command `pip -V` to see that your virtual environment is activated.

## Install packages 
1. `python3 -m pip install <package>`: The package ends in the virtual environment if activated, otherwise global on the computer.  
2. `python3 -m pip install --upgrade <package>`
3. `python3 pip install -r <./path/requirement.txt>`: (. = from the current directory, without = operativ system root)

## Run python file
1. Run a python file by writing `python3 main.py`.
