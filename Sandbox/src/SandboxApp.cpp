#include <Rits.h>
#include <spdlog/spdlog.h>

class ExampleLayer : public Rits::Layer
{
public:
    ExampleLayer()
        : Layer("Example")
    {
    }

    void OnUpdate() override
    {
        //RT_INFO("ExampleLayer::Update");
    }

    void OnEvent(Rits::Event& event) override
   {
        RT_TRACE("{0}", event);
   }
};

class Sandbox : public Rits::Application
{
public:
    Sandbox()
    {
        PushLayer(new ExampleLayer());
    }
    ~Sandbox()
    {

    }
};

Rits::Application* Rits::CreateApplication()
{
    return new Sandbox();
}