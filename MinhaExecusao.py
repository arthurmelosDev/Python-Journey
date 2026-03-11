import pyautogui
import pandas as pd
import time

# importar a base de produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)

# define o tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo 1: abrir o navegador e o site
# abrir sistema (Vivaldi)
pyautogui.press("win")
pyautogui.write("vivaldi")
pyautogui.press("enter")
pyautogui.click(x=348, y=49)
pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 2: fazer o login
pyautogui.click(x=767, y=362)
pyautogui.write("email@hotmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(4)

# Passo 4: cadastrar os produtos


for linha in tabela.index:  # para cada linha na tabela, procurar pelo índice
    pyautogui.click(x=799, y=242)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # verifica se existe informação em obs, caso contrário não preenche
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    pyautogui.click(x=799, y=242)
