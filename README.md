How to run tests in windows

To run automated test that are written in python, you need to finish some steps:
 1. install python 3.8
 2. install selenium
 3. set environment variables
 
 1. Go to python site (python.org) and download and install latest python.
    During installation check checkbox: Add Python 3.8 to PATH
    
    To check if step is done: open Command prompt, and execute "python -V". 
    Value 'Python 3.8...' should be returned.
    
 2. From Command prompt execute command: "pip install selenium"
 
    To check if step is done: in Command prompt execute command: "python". Python console
    will open. In opened python console execute python command "import selenium".
    If ImportError is not shown, this step is done.
    
 3. System variable PYTHONPATH should have value of relative path to SandBox folder.
    User variables, Path should have path to chromedriver folder.
    
Note: restart cmd after setting environment variables.
    
    
   
 