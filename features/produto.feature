# language: pt

Funcionalidade: Pesquisar produto

  Cenário: Pesquisar produto com sucesso
    Dado que o usuário acessa a página "https://automationexercise.com/"
    Quando ir para a página de pesquisar produto
    E informar o produto 
    Então o produto deve ser apresentado na tela