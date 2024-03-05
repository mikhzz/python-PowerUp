# Passo a passo do projeto
#Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui -> para instalar via terminal.
import pyautogui
import time

pyautogui.PAUSE = 0.5
#pyautogui.click -> clicar em algum lugar da tela
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar 1 tecla do teclado
#pyautogui.hotkey("ctrl", "v") -> exemplo de combinação de teclas
#abrir navegador -> passando como parâmetro a tecla correspondente e dps o navegador desejado

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)

pyautogui.press("enter")

#dar uma pausa um pouco maior de 3 segundos por exemplo
time.sleep(3)

# Passo 2: Fazer Login
# campo email
pyautogui.click(x=1832, y=421)

time.sleep(3)

pyautogui.write("pythonTeste@gmail.com")

time.sleep(3)

pyautogui.press("tab")

# caso precise da informação do campo senha -> pyautogui.click(x=1789, y=523)

time.sleep(3)

pyautogui.write("1234")

#clicar no botao de logar

pyautogui.click(x=1933, y=577)

time.sleep(3)

# Passo 3: Importar base de dados
# pip install pandas numpy openpyxl -> instalar para trabalhar com base de dados.
import pandas
tabela = pandas.read_csv("produtos.csv")
# print(tabela)
# Passo 4: cadastrar 1 produto
# estrutura de repetição FOR
for linha in tabela.index:
    #clicar no primeiro campo.
   
        
    pyautogui.click(x=1794, y=298)
    #código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    
    #tipo

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #categoria

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preço

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #observação
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs
                        )
    pyautogui.press("tab")

    time.sleep(3)
    #clicar no botão enviar

    pyautogui.press("enter")
    pyautogui.scroll(5000)
# Passo 5: Repetir o processo de cadastro até acabar a base de dados
    if linha == tabela.index[-1]:
        print("Cadastro concluído para todas as linhas.")
    else:
        print("O loop foi interrompido antes de chegar ao final.")
