#bibliotecas necessarias
import pyautogui
import time
import pandas as pd

#time.sleep = o tempo de espera para realizar a ultima ação
#pyautogui.write = escreve um texto
#pyautogui.press = aperta uma tecla
#pyautogui.click = clicka em um lugar da tela 
#pyautogui.hotkey = combinaçoes de teclas --> pyautogui.hotkey("crtl", "c")
#pyautogui.PAUSE = o tempo de espera para realizar cada comando
#observação para parar o programa basta colocar seu mouse no canto superior esquerdo

pyautogui.PAUSE = 0.4

#comando para abrir o local necessario desde que ele apareça na sua aba de pesquisa do windows
pyautogui.press("win")
pyautogui.write("Opera GX")
pyautogui.press("enter")

#entrar no link 
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

#fazer login no site/empresa
#selecionar o campo de login, varia de monitor e resolução
pyautogui.click(x=845, y=486)
#escreve seu email
pyautogui.write("exemplo@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")

#importar a base de produtos a cadastrar
#redifine o tipo do seu banco de dados

tabela = pd.read_csv("produtos.csv")
print(tabela)
pyautogui.PAUSE = (0.5)
#realizar o cadastro de produtos
for linha in tabela.index:
    #clique no primeiro campo
    pyautogui.click(x=837, y=340)
    #preencher o campo
    codigo = tabela.loc[linha, "codigo"]

    pyautogui.write(str(codigo))
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
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    time.sleep(2)
    #scrollar tudo para cima para reiniciar o processo  








