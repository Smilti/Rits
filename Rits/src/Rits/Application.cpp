#include "Application.h"

#include "Rits/Events/ApplicationEvent.h"
#include "Rits/Log.h"

namespace Rits {



    Application::Application()
    {
    }

    Application::~Application()
    {
    }

    void Application::Run()
    {
        WindowResizeEvent e(1280, 720);
        if (e.IsInCategory(EventCategoryApplication))
        {
            RT_TRACE(e);
        }
        if (e.IsInCategory(EventCategoryInput))
        {
            RT_TRACE(e);
        }

        while (true);
    }

}