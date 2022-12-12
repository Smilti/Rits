#include <Rits.h>

class Sandbox : public Rits::Application
{
public:
    Sandbox()
    {

    }
    ~Sandbox()
    {

    }
};

Rits::Application* Rits::CreateApplication()
{
    return new Sandbox();
}