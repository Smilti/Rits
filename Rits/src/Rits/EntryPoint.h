#pragma once

extern Rits::Application* Rits::CreateApplication();

int main(int argc, char** argv)
{
    Rits::Log::Init();
    RT_CORE_WARN("Initialized Log!");
    int a = 5;
    RT_INFO(a);

    auto app = Rits::CreateApplication();
    app->Run();
    delete app;
}