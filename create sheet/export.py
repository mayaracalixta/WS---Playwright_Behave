import os
import pandas as pd

def extrair_cenarios_de_features(pasta, arquivos_escolhidos=None):
    dados = []

    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".feature"):
            if arquivos_escolhidos and arquivo not in arquivos_escolhidos:
                continue

            caminho = os.path.join(pasta, arquivo)
            with open(caminho, 'r', encoding='utf-8') as f:
                linhas = f.readlines()

            funcionalidade = ""
            cenario_atual = ""
            steps = []

            for linha in linhas:
                linha = linha.strip()
                
                if linha.startswith("Funcionalidade:"):
                    funcionalidade = linha.replace("Funcionalidade:", "").strip()
                
                elif linha.startswith("Cenário:"):
                    if cenario_atual and steps:
                        dados.append([arquivo, funcionalidade, cenario_atual, "\n".join(steps), "", "Em andamento"])  
                        
                        steps = []

                    cenario_atual = linha.replace("Cenário:", "").strip()
                
                elif any(linha.startswith(s) for s in ["Dado", "Quando", "Então", "E", "Mas"]):
                    steps.append(linha)

            if cenario_atual and steps:
                dados.append([arquivo, funcionalidade, cenario_atual, "\n".join(steps),""])  # Coluna Status com valor inicial

    # Criando o DataFrame com a nova coluna de status
    return pd.DataFrame(dados, columns=["Arquivo", "Funcionalidade", "Cenário", "Casos de Teste (Passo ou Gherkin)", "Status"])

def gerar_nome_arquivo(base="cenarios_de_teste"):
    i = 1
    while True:
        nome = f"{base}_{i:02d}.xlsx"
        if not os.path.exists(nome):
            return nome
        i += 1

# Caminho para a pasta com os arquivos .feature
pasta = "features"

# Opção do usuário
todos = input("\nExportar todos os arquivos? (s/n): ").strip().lower()

if todos == 's':
    arquivos_escolhidos = None
else:
    print("\nArquivos disponíveis na pasta:")
    arquivos = [f for f in os.listdir(pasta) if f.endswith(".feature")]
    for i, nome in enumerate(arquivos):
        print(f"{i+1}: {nome}")
    
    indices = input("\nDigite os números dos arquivos separados por vírgula (ex: 1,3): ")
    escolhidos = [arquivos[int(i.strip()) - 1] for i in indices.split(',') if i.strip().isdigit()]
    arquivos_escolhidos = escolhidos

# Gera e salva o arquivo com nome único
df = extrair_cenarios_de_features(pasta, arquivos_escolhidos)
nome_arquivo = gerar_nome_arquivo()
df.to_excel(nome_arquivo, index=False)

print(f"\nPlanilha '{nome_arquivo}' criada com sucesso!")
