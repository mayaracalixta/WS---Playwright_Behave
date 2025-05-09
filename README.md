# 📘 Guia de Instalação e Execução: Playwright + Behave + Python

## ✅ 1. Instale o Python

- Acesse: https://www.python.org/downloads/
- Baixe e instale o Python 3.8 ou superior.
- **Importante**: Marque a opção **"Add Python to PATH"** durante a instalação.

Para verificar se está instalado corretamente, abra o terminal/cmd e digite:

```bash
python --version
```

## 📦 2. Instale as dependências
- Com o Python instalado, rode:

```bash
pip install behave playwright pandas faker
python -m playwright install
```

## 📦 3. Estrutura de arquivos recomendada

```bash
projeto-playwright-behave/
├── features/
│   ├── cadastro.feature
│   └── steps/
│       └── step_definitions.py
├── locators/
│   └── home_page_locators.py
├── utils/
│   └── browser_setup.py
├── requirements.txt
└── README.md

```
## ▶️ 4. Como executar os testes
- Navegue até a pasta do projeto no terminal e rode:

```bash
behave
```

## 📘 Documentação Oficial e Tutoriais

- Playwright Python Docs: https://playwright.dev/python
- Behave: https://behave.readthedocs.io/en/stable/