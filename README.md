#How to run tests in windows

To run automated test that are written in python, you need to finish some steps:
 1. install python 3.8
 2. install selenium
 3. set environment variables
 
 - Go to python site (python.org) and download and install latest python.
    During installation check checkbox: Add Python 3.8 to PATH
    
    To check if step is done: open Command prompt, and execute "python -V". 
    Value 'Python 3.8...' should be returned.
    
 - From Command prompt execute command: "pip install selenium"
 
    To check if step is done: in Command prompt execute command: "python". Python console
    will open. In opened python console execute python command "import selenium".
    If ImportError is not shown, this step is done.
    
 - System variable **PYTHONPATH** should have value of  path to SandBox folder.
    User variables, **Path** should have path to chromedriver folder. 
    
Note: restart cmd after setting environment variables. Use latest Chrome version for running tests.


#About test framework:
Modules are stored in Lib folder. There exist common.py file that contains business logic
that is not bound to web site, every web site can use it. Other filer are bound to
sandbox web site. It contains business logic for this site. Files are separated
by feature. 

Tests are created in a way that they don't leave changes on web site.
For example if test needs specific use case, test will create it, and delete it at the end
of test. Example how logging would be added, if logging mechanism exist,
is given in pattern: **# log.info("")** ,** # log.screenshot("")**. Proposal is to
write info before action, and after action is done put screenshot.
Method **wait_until** is used for dynamic waiting, when condition that we are waiting for is
 reached this method is finished, as opposite of static waiting (time.sleep()).
  
What this framework is missing is logging mechanism, way to store elements from web page
in one location, some configuration file that
would contain variables from tests and that every test can reach, reporting dashboard, plans
that contains tests.
    
    
   
 