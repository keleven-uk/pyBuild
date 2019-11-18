###############################################################################################################
#  Kompiles executables for both 32 & 64 bit windows, from a python script.                                            #
#                                                                                                             #
#  The different versions of python [32 & 64 bit] need to be set up in the python launcher                    #
#  and are hard coded, for the moment.                                                                        #
#                                                                                                             #
#  Usage: pyBuild.py [-h] source                                                                                #
#                                                                                                             #
#  October 2019                Kevin Scott                                                                    #
#                                                                                                             #
#   V1.00   01 Oct.2019   All seems to be working.                                                            #
#   V1.01   16 Oct.2019   Added command line arguments and docstrings.                                        #
###############################################################################################################
#    Copyright (C) <2019>  <Kevin Scott>                                                                      #
#                                                                                                             #
#    This program is free software: you can redistribute it and/or modify it under the terms of the           #
#    GNU General Public License as published by the Free Software Foundation, either version 3 of the         #`
#    License, or (at your option) any later version.                                                          #
#                                                                                                             #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without        #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#    GNU General Public License for more details.                                                             #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################


import os
import time
import datetime
import subprocess, shlex
import argparse
from _version import __version__

PY_32 = "py -3.7-32 -m PyInstaller "                  #  call pyinstaller in 32 bit mode.
PY_64 = "py -3.7-64 -m PyInstaller "                  #  call pyinstaller in 64 bit mode.
ARGS  = " --onefile --noconsole --log-level ERROR"    #  arguments for pyinstaller.


def compile32(source_file, exec_file, ex32_file):
    """  Kompiles the 32 bit executable.
         The source is compiled into an executable file and then renamed 
         to a file with the _32 extension.
         i.e. file.exe -> file_32.exe

    Parameters:
    argument1 (str): name of source file. Already checked to exist.
    argument2 (str): name of executable file.
    argument3 (str): name of 32 bit executable file.

    Returns:
    none

    """
    #  Compile 32 bit.
    command = PY_32 + source_file + ARGS
    call_params = shlex.split(command)
    subprocess.run(call_params)

    #  rename .exe for 32 bit.
    if os.path.exists(ex32_file): os.remove(ex32_file)   #  delete file first, else rename complains       
    if os.path.exists(exec_file): os.rename(exec_file, ex32_file)


def compile64(source_file, exec_file, ex64_file):
    """  Kompiles the 64 bit executable.
         The source is compiled into an executable file and then renamed 
         to a file with the _64 extension.
         i.e. file.exe -> file_64.exe

    Parameters:
    argument1 (str): name of source file. Already checked to exist.
    argument2 (str): name of executable file.
    argument3 (str): name of 64 bit executable file.

    Returns:
    none

    """
    #  Compile 64 bit.
    command = PY_64 + source_file + ARGS
    call_params = shlex.split(command)
    subprocess.run(call_params)

    #  rename .exe for 64 bit.
    if os.path.exists(ex64_file): os.remove(ex64_file)   #  delete file first, else rename complains       
    if os.path.exists(exec_file): os.rename(exec_file, ex64_file)


def Kompile(sourceFile):
    """  Kompiles the python source into both 32 & 64 bit executables.

    Parameters:
    argument1 (str): name of source file. Already checked to exist.

    Returns:
    none

    """

    source_file = "./" + sourceFile + ".py"         #  slash other way ;-)
    exec_file   = "dist\\" + sourceFile + ".exe"
    ex32_file   = "dist\\" + sourceFile + "_32.exe"
    ex64_file   = "dist\\" + sourceFile + "_64.exe"
    
    compile32(source_file, exec_file, ex32_file)
    compile64(source_file, exec_file, ex64_file)



if __name__ == "__main__":
    start_time = time.time()

    parser = argparse.ArgumentParser(description="A Python Script Compiler.", epilog = " Kevin Scott (C) 2019")
    #  Add a Positional Argument.
    #  a optional argument would be --source or -s
    parser.add_argument("source", type=str, help="Name of the Source File to be kompiled [without .py extension].")
    parser.add_argument("-v", "--version",   action="version", version="%(prog)s {}".format(__version__))
    args   = parser.parse_args()

    sourceFile = args.source

    if os.path.exists(sourceFile + ".py"):
        print("Compiling " + sourceFile)
        Kompile(sourceFile)
    else:
        print("File not found")
        print("Run pyBuild.py --help for usage")
        exit(2)

    print()
    elapsed_time_secs = time.time() - start_time
    print("Completed %s" % datetime.timedelta(seconds = elapsed_time_secs))
    print()
