Ard coded within the scriptbout pyBuild

  Kompiles executables for both 32 & 64 bit windows,  from a python script
  Should be run in the same directory as the python script.
  The different versions of python [32 & 64 bit] need to be set up in the python launcher
  and are hard coded, for the moment.
  
  usage: pyBuild.py [-h] [-s SOURCE] [-v] [-l]
 
   A Python Script Compiler.
   
   optional arguments:
     -h, --help            show this help message and exit  
     -s SOURCE, --source SOURCE                              
                           Name of the Source File to be kompiled. 
     -v, --version         show program's version number and exit        
     -l, --license         Print the Software License. 

   Kevin Scott (C) 2019  


Hard coded within the script -

PY_32 = "py -3.7-32 -m PyInstaller "                  #  call pyinstaller in 32 bit mode.
PY_64 = "py -3.7-64 -m PyInstaller "                  #  call pyinstaller in 64 bit mode.
ARGS  = " --onefile --noconsole --log-level ERROR"    #  arguments for pyinstaller.


History
-------

V1.00   01 Oct. 2019   All seems to be working.
V1.01   16 Oct. 2019   Added command line arguments and docstrings.
V1.02	20 Oct. 2019   Amended all the argumenst to be optional.
V1.03   21 Oct. 2019   Changed all paths to use pathlib.


