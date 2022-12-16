
import os
import subprocess
import platform

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname+'/../')

#MacOS configuration
if platform.system() == "Darwin":
    #Library
    subprocess.run([
        "g++",
        "-std=c++17",
        "-O2",
        "-DNDEBUG",
        "-dynamiclib",
        "-install_name",
        "@rpath/../Resources/librits.dylib",
        "-g",
        "./Rits/src/Rits/Application.cpp",
        "-o",
        "./bin/Release/game.app/Contents/Resources/librits.dylib",
        "-I./Rits/src",
        "-lglfw",
        "-lvulkan",
        ])
    #Game
    subprocess.run([
        "g++",
        "-std=c++17",
        "-O2",
        "-DNDEBUG",
        "-Wl,-rpath,@executable_path",
        "-g",
        "./Sandbox/src/SandboxApp.cpp",
        "-o",
        "./bin/Release/game.app/Contents/MacOS/game.out",
        "-L./bin/Release/game.app/Contents/Resources/",
        "-I./Sandbox/src",
        "-I./Rits/src",
        "-lrits",
        "-lglfw",
        ])
    subprocess.run([
        "rm",
        "-rf",
        "bin/Release/game.app/Contents/Resources/DWARF",
    ])
    subprocess.run([
        "mv",
        "-f",
        "bin/Release/game.app/Contents/MacOS/game.dSYM/Contents/Resources/DWARF/",
        "bin/Release/game.app/Contents/Resources",
        ])
    subprocess.run([
        "rm",
        "-rf",
        "bin/Release/game.app/Contents/MacOS/game.dSYM",
    ])
#Linux configuration
if platform.system() == "Linux":
    #Library
    subprocess.run([
        "g++",
        "-O3",
        "-DNDEBUG",
        "-std=c++17",
        "-shared",
        "-g",
        "./Rits/src/Rits/Application.cpp",
        "./Rits/src/Rits/Log.cpp",
        "-o",
        "./bin/Release/librits.so",
        "-I./Rits/vendor/spdlog/include",
        "-lglfw",
        "-lvulkan",
        "-fPIC",
        ])
        #Game
    subprocess.run([
        "g++",
        "-Wall",
        "-O3",
        "-std=c++17",
        "-DNDEBUG",
        "-g",
        "./Sandbox/src/SandboxApp.cpp",
        "-o",
        "./bin/Release/game",
        "-L./bin/Release/",
        "-I./Rits/src",
        "-I./Rits/vendor/spdlog/include",
        "-lrits",
        "-lglfw",
        "-Wl,-rpath=$ORIGIN,--enable-new-dtags",
        ])
#Windows configuration
if platform.system() == "Windows":
    print("Windows not yet supported!")