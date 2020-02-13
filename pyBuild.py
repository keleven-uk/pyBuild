###############################################################################################################
#  Kompiles executables for both 32 & 64 bit windows, from a python script                                   # 
#  Should be run in the same directory as the python script.                                                  #
#  The different versions of python [32 & 64 bit] need to be set up in the python launcher                    #
#  and are hard coded, for the moment.                                                                        #
#                                                                                                             #
#  usage: pyBuild.py [-h] [-s SOURCE] [-v] [-l]                                                               #
#                                                                                                             #
#   A Python Script Compiler.                                                                                 #
#                                                                                                             #
#   optional arguments:                                                                                       #
#     -h, --help            show this help message and exit                                                   #
#     -s SOURCE, --source SOURCE                                                                              #
#                           Name of the Source File to be kompiled.                                           #
#     -g, --gui             Does this script have a GUI, else a console script.                               #
#     -v, --version         show program's version number and exit                                            #
#     -l, --license         Print the Software License.                                                       #
#                                                                                                             #
#  NB : Needs pyinstaller, colorama, not in the Python Standard Library                                       #
#                                                                                                             #
#   Kevin Scott (C) 2019 - 2020                                                                               #
#                                                                                                             #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2019 - 2020>  <Kevin Scott>                                                               #
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


import time
import pathlib
import datetime
import textwrap
import argparse
import subprocess, shlex
import colorama
from _version import __version__

PY_32 = "py -3.8-32 -m PyInstaller "                  #  call pyinstaller in 32 bit mode.
PY_64 = "py -3.8-64 -m PyInstaller "                  #  call pyinstaller in 64 bit mode.


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
    command = PY_32 + source_file.name + ARGS
    call_params = shlex.split(command)
    subprocess.run(call_params)

    #  rename .exe for 32 bit.
    if exec_file.exists(): exec_file.replace(ex32_file)

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
    command = PY_64 + source_file.name + ARGS
    call_params = shlex.split(command)
    subprocess.run(call_params)

    #  rename .exe for 64 bit.
    if exec_file.exists(): exec_file.replace(ex64_file)


def Kompile(sourceFile):
    """  Kompiles the python source into both 32 & 64 bit executables.

    Parameters:
    argument1 (str): name of source file. Already checked to exist.

    Returns:
    none

    """

    source_file = pathlib.Path.cwd().joinpath(sourceFile)
    exec_file   = pathlib.Path.cwd().joinpath("dist", source_file.stem + ".exe")
    ex32_file   = pathlib.Path.cwd().joinpath("dist", source_file.stem + "_32.exe")
    ex64_file   = pathlib.Path.cwd().joinpath("dist", source_file.stem + "_64.exe")

    compile32(source_file, exec_file, ex32_file)
    compile64(source_file, exec_file, ex64_file)



def printShortLicense():
    print("""
PyBackup {}   Copyright (C) 2019  Kevin Scott
This program comes with ABSOLUTELY NO WARRANTY; for details type `pyBuild -l''.
This is free software, and you are welcome to redistribute it under certain conditions.
    """.format(__version__), flush=True)



def printLongLicense():
    print("""
    Copyright (C) 2019  Kevin Scott

    This program is free software: you can redistribute it and/or modify it 
    under the terms of the GNU General Public License as published by   
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """, end="")


if __name__ == "__main__":
    colorama.init()
    
    start_time = time.time()

    parser = argparse.ArgumentParser(
        formatter_class = argparse.RawTextHelpFormatter,
        description=textwrap.dedent("""\
        A Python Script Compiler.
        -----------------------
        Kompiles executables for both 32 & 64 bit windows, from a python script.
        Should be run in the same directory as the python script.
        The different versions of python [32 & 64 bit] need to be set up in 
        the python launcher and are hard coded, for the moment."""),
        epilog = " Kevin Scott (C) 2019")

    parser.add_argument("-s", "--source",   type=pathlib.Path, action="store", default=False, help="Name of the Source File to be kompiled.")
    parser.add_argument("-g", "--gui",  action="store_false", help="Does this script have a GUI, else a console script.")
    parser.add_argument("-v", "--version",  action="version", version="%(prog)s {}".format(__version__))
    parser.add_argument("-l", "--license",  action="store_true", help="Print the Software License.")
    args   = parser.parse_args()

    if args.license:
        printLongLicense()
        parser.exit(0)

    if not args.source:
        parser.print_help()
        parser.exit(1)
    else:
        sourceFile = args.source
        
    # if the script is a command line program, needs a console window.
    # if the script is a gui, the console can be dispense with.        

    if sourceFile.exists():
        printShortLicense()
        if args.gui:
            ARGS  = " --onefile --log-level ERROR"    #  arguments for pyinstaller. 
            print(f"{colorama.Fore.GREEN} Compiling a Console script {sourceFile.name} {colorama.Fore.RESET}")    
        else:
            ARGS  = " --onefile --noconsole --log-level ERROR"    #  arguments for pyinstaller.    
            print(f"{colorama.Fore.GREEN} Compiling a GUI script {sourceFile.name} {colorama.Fore.RESET}")
        
        Kompile(sourceFile)
    else:
        print(f"{colorama.Fore.RED} File not found :: {sourceFile.name} {colorama.Fore.RESET}")
        parser.print_help()
        exit(2)

    print()
    elapsed_time_secs = time.time() - start_time
    print(f"{colorama.Fore.CYAN} Completed {datetime.timedelta(seconds = elapsed_time_secs)} {colorama.Fore.RESET}")
    print()
