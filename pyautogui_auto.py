import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

# time.sleep(1)

# print(pyautogui.position())

# pyautogui.click(x=3062, y=1062)

# pyautogui.click(x=3324, y=962)

# pyautogui.hotkey("ctrl", "t")

# pyautogui.write("https://novosolar.defensoria.df.gov.br/")

# pyautogui.press("enter")

tabela = pd.read_csv("usuarios.csv", encoding="latin1", sep=";")

nome1 = tabela.loc[2, "email"]

print(nome1)
