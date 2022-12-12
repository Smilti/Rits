#pragma once

extern Rits::Application* Rits::CreateApplication();

int main(int argc, char** argv)
{
    auto app = Rits::CreateApplication();
    app->Run();
    delete app;
}