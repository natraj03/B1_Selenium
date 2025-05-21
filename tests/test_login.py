from pages.login import username, password,signIn, openLoginPage, forgetPassword, createNweAccount


def test_success():
    openLoginPage()
    username("rashmiranjan4546@gmail.com")
    password("Nist@12345")
    signIn()


def test_emptyField():
    openLoginPage()
    username("")
    password("")
    signIn()

def test_wrongCredential():
    openLoginPage()
    username("1rashmiranjan4546@gmail.com")
    password("Nist@12345")
    signIn()

def test_Emptysubmit():
    openLoginPage()
    signIn()

def test_openForget():
    openLoginPage()
    forgetPassword()

def test_Createaccount():
    openLoginPage()
    createNweAccount()