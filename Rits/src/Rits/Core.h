#pragma once


#ifdef RT_ENABLE_ASSERTS
	#define RT_ASSERT(x, ...) { if(!(x)) { RT_ERROR("Assertion Failed: {0}", __VA_ARGS__); /*__debugbreak();*/ } }
	#define RT_CORE_ASSERT(x, ...) { if(!(x)) { RT_CORE_ERROR("Assertion Failed: {0}", __VA_ARGS__); /*__debugbreak();*/ } }
#else
	#define RT_ASSERT(x, ...)
	#define RT_CORE_ASSERT(x, ...)
#endif

#define BIT(x) (1 << x)