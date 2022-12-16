workspace "Rits"
    architecture "x64"

    configurations
    {
        "Debug",
        "Release",
        "Dist"
    }

outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

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
        "%{prj.name}/vendor/spdlog/include"
    }

    cppdialect "C++17"
    staticruntime "On"
    systemversion "latest"
    
    filter "configurations:Debug"
        defines "RT_DEBUG"
        symbols "On"

    filter "configurations:Release"
        defines "RT_RELEASE"
        symbols "On"

    filter "configurations:Dist"
        defines "RT_DIST"
        symbols "On"

project "Sandbox"
    location "Sandbox"
    kind "ConsoleApp"

    language "C++"

    targetdir ("bin/" .. outputdir .. "/%{prj.name}")
    objdir ("bin-int/" .. outputdir .. "/%{prj.name}")

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
    systemversion "latest"

    filter "configurations:Debug"
        defines "RT_DEBUG"
        symbols "On"

    filter "configurations:Release"
        defines "RT_RELEASE"
        symbols "On"

    filter "configurations:Dist"
        defines "RT_DIST"
        symbols "On"

