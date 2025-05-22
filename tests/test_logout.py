from pages.login import username, password,signIn, openLoginPage, forgetPassword, createNweAccount
from pages.logout import userMenuLogo, openDashboardPage

def test_logout():
    openLoginPage()
    username("rashmiranjan4546@gmail.com")
    password("Nist@12345")
    signIn()
    openDashboardPage()
    userMenuLogo()




