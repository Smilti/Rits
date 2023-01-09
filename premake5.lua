workspace "Rits"
    architecture "x64"

    configurations
    {
        "Debug",
        "Release",
        "Dist"
    }

outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

IncludeDir = {}
IncludeDir["GLFW"] = "Rits/vendor/GLFW/include"

include "Rits/vendor/GLFW"

project "Rits"
    location "Rits"
    kind "SharedLib"
    language "c++"

    targetdir ("bin/" .. outputdir .. "/%{prj.name}")
    objdir ("bin-int/" .. outputdir .. "/%{prj.name}")

    files
    {
        "%{prj.name}/src/**.h",
        "%{prj.name}/src/**.cpp",
    }

    includedirs
    {
        "%{prj.name}/src",
        "%{prj.name}/vendor/spdlog/include",
        "%{IncludeDir.GLFW}"
    }

    links
    {
        "GLFW",
        --"opengl32.lib"
    }

    cppdialect "C++17"
    staticruntime "On"

    filter "system:macosx"
        links
        {
            "OpenGL.framework"
        }

    filter "system:linux"
        systemversion "latest"
        links
        {
            "OpenGL"
        }
    
    filter "configurations:Debug"
        defines
        {
            "RT_DEBUG",
            --"RT_ENABLE_ASSERTS"
        }
        symbols "On"

    filter "configurations:Release"
        defines "RT_RELEASE"
        optimize "On"

    filter "configurations:Dist"
        defines "RT_DIST"
        optimize "On"

project "Sandbox"
    location "Sandbox"
    kind "ConsoleApp"

    language "C++"

    targetdir ("bin/" .. outputdir .. "/%{prj.name}")
    objdir ("bin-int/" .. outputdir .. "/%{prj.name}")

    pchheader "rtpch.h"
	pchsource "Rits/src/rtpch.cpp"

    files
    {
        "%{prj.name}/src/**.h",
        "%{prj.name}/src/**.cpp"
    }

    includedirs
    {
        "%{prj.name}/src",
        "Rits/vendor/spdlog/include",
        "Rits/src"
    }

    links
    {
        "Rits"
    }

    cppdialect "C++17"
    staticruntime "On"
    filter "system:windows"
        systemversion "latest"

    filter "configurations:Debug"
        defines "RT_DEBUG"
        symbols "On"

    filter "configurations:Release"
        defines "RT_RELEASE"
        optimize "On"

    filter "configurations:Dist"
        defines "RT_DIST"
        optimize "On"

