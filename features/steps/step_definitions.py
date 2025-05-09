from imports import *

# Carrega os dados do arquivo JSON
def carregar_dados():
    with open('features/data/cadastro.json', 'r') as f:
        return json.load(f)

dados = (carregar_dados())

@given('que o usuário acessa a página "{url}"')
def step_impl(context, url):
    #Navega até a tela 
    context.playwright, context.browser, context.page = start_browser()
    context.page.goto(url)
    
    #Valida se a pagina está totalmente carregada
    expect(context.page.locator(HomePageLocators.BOTAO_LOGIN)).to_be_visible()


@when('ir para a página de cadastro de usuário')
def step_impl(context):     
    #Clica no botão
    context.page.click(HomePageLocators.BOTAO_LOGIN)

    #Preencher Formulário parte1
    context.page.fill(HomePageLocators.INPUT_NAME_LOGIN,fake.name())
    context.page.fill(HomePageLocators.INPUT_EMAIL_LOGIN,fake.email())
    context.page.click(HomePageLocators.BOTAO_SIGNUP)
    expect(context.page.locator('text=Enter Account Information')).to_be_visible()



@when('preencher o formulário')
def step_impl(context):

    #Preencher Formulário parte2
    context.page.fill(HomePageLocators.INPUT_PASSWORD,fake.password())
    context.page.check('#id_gender1')
    context.page.select_option(HomePageLocators.INPUT_DAYS, str(dados["dia"]))
    context.page.select_option(HomePageLocators.INPUT_MONTHS, dados["mes"])
    context.page.select_option(HomePageLocators.INPUT_YEARS, str(dados["ano"]))
    context.page.fill(HomePageLocators.INPUT_FIRST_NAME,fake.first_name())
    context.page.fill(HomePageLocators.INPUT_LAST_NAME,fake.last_name())
    context.page.fill(HomePageLocators.INPUT_COMPANY,fake.company())
    context.page.fill(HomePageLocators.INPUT_ADDRESS1,fake.address())
    context.page.fill(HomePageLocators.INPUT_ADDRESS2,fake.address())
    context.page.select_option(HomePageLocators.INPUT_COUNTRY, dados["country"])
    context.page.fill(HomePageLocators.INPUT_STATE, fake.state())
    context.page.fill(HomePageLocators.INPUT_CITY, fake.city())
    context.page.fill(HomePageLocators.INPUT_ZIPCODE, fake.postcode())
    context.page.fill(HomePageLocators.INPUT_MOBILE_NUMBER, fake.phone_number())
    context.page.click(HomePageLocators.BOTAO_CREATE)


@then('uma mensagem de sucesso deve aparecer na tela')
def step_impl(context):
    expect(context.page.locator('text=Account Created!')).to_be_visible()


