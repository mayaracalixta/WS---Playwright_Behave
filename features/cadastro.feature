# language: pt

Funcionalidade: Cadastro de usuário

  Cenário: Cadastro de usuario com sucesso
    Dado que o usuário acessa a página "https://automationexercise.com/"
    Quando ir para a página de cadastro de usuário
    E preencher o formulário
    Então uma mensagem de sucesso deve aparecer na tela
