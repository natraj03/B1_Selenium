from pages.login import *


def test_success():
    openLoginPage()
    username("rashmiranjan4546@gmail.com")
    password("Nist@12345")
    signIn()
    openDashboardPage()
    userMenuLogo()
    signout()


# def test_open_project():
#     openLoginPage()
#     username("rashmiranjan4546@gmail.com")
#     password("Nist@12345")
#     signIn()
#     openMyproject()
#     clickWorkSpace()
#     clickCreatebutton()
#     clickCreatebutton_task()

# def test_logout():
#     openDashboardPage()
#     userMenuLogo()
#     signout()


# def test_emptyField():
#     openLoginPage()
#     username("")
#     password("")
#     signIn()
#
# def test_wrongCredential():
#     openLoginPage()
#     username("1rashmiranjan4546@gmail.com")
#     password("Nist@12345")
#     signIn()
#
# def test_Emptysubmit():
#     openLoginPage()
#     signIn()
#
# def test_openForget():
#     openLoginPage()
#     forgetPassword()
#
# def test_Createaccount():
#     openLoginPage()
#     createNweAccount()