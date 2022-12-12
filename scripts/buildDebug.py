
import os
import subprocess
import platform

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname+'/../')
print(os.path.abspath("./"))
#MacOS configuration
if platform.system() == "Darwin":
    #Library
    subprocess.run([
        "g++",
        "-std=c++17",
        "-dynamiclib",
        "-install_name",
        "@rpath/librits.dylib",
        "-g",
        "./Rits/src/Rits/Application.cpp",
        "-o",
        "./bin/Debug/librits.dylib",
        "-I./Rits/src",
        "-lglfw",
        "-lvulkan",
        ])
    #Game
    subprocess.run([
        "g++",
        "-std=c++17",
        "-Wl,-rpath,@executable_path",
        "-g",
        "./Sandbox/src/SandboxApp.cpp",
        "-o",
        "./bin/Debug/game",
        "-L./bin/Debug/",
        "-I./Rits/src",
        "-I./Sandbox/src",
        "-lrits",
        "-lglfw",
        ])
#Linux configuration
if platform.system() == "Linux":
    #Library
    subprocess.run([
        "g++",
        "-std=c++17",
        "-dynamiclib",
        "-g",
        "./Rits/base.cpp",
        "-o",
        "./bin/librits.dylib",
        "-lglfw",
        "-lvulkan"
        ])
        #Game
    subprocess.run([
        "g++",
        "-std=c++17",
        "-g",
        "./Game/main.cpp",
        "-o",
        "./bin/game",
        "-L./bin",
        "-I./Rits",
        "-lrits",
        "-lglfw",
        ])
#Windows configuration
if platform.system() == "Windows":
    print("Windows not yet supported!")