#pragma once

#include <memory>

#include "Core.h"
#include "spdlog/spdlog.h"
#include "spdlog/fmt/ostr.h"

namespace Rits {
    class Log
    {
    public:
        static void Init();

        inline static std::shared_ptr<spdlog::logger>& GetCoreLogger() { return s_CoreLogger; }
        inline static std::shared_ptr<spdlog::logger>& GetClientLogger() { return s_ClientLogger; }
    private:
        static std::shared_ptr<spdlog::logger> s_ClientLogger;
        static std::shared_ptr<spdlog::logger> s_CoreLogger;

    };
}

//Core  log macros
#define RT_CORE_ERROR(...) ::Rits::Log::GetCoreLogger()->error(__VA_ARGS__)
#define RT_CORE_WARN(...)  ::Rits::Log::GetCoreLogger()->warn(__VA_ARGS__)
#define RT_CORE_INFO(...)  ::Rits::Log::GetCoreLogger()->info(__VA_ARGS__)
#define RT_CORE_TRACE(...) ::Rits::Log::GetCoreLogger()->trace(__VA_ARGS__)
#define RT_CORE_FATAL(...) ::Rits::Log::GetCoreLogger()->fatal(__VA_ARGS__)

//Client log macros
#define RT_ERROR(...)      ::Rits::Log::GetClientLogger()->error(__VA_ARGS__)
#define RT_WARN(...)       ::Rits::Log::GetClientLogger()->warn(__VA_ARGS__)
#define RT_INFO(...)       ::Rits::Log::GetClientLogger()->info(__VA_ARGS__)
#define RT_TRACE(...)      ::Rits::Log::GetClientLogger()->trace(__VA_ARGS__)
#define RT_FATAL(...)      ::Rits::Log::GetClientLogger()->fatal(__VA_ARGS__)
