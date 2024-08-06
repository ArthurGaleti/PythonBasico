import pyautogui
import time

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

# entrar no link 
pyautogui.write("https://www.youtube.com")
pyautogui.press("enter")
time.sleep(6)


# Pesquisar conteudo
pyautogui.write("tutorial de tortas")
pyautogui.press("enter")

time.sleep(3)

#iniciar um vídeo
pyautogui.click(x=552, y=639)

time.sleep(3)

pyautogui.press("f")


