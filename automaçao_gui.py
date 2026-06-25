import pyautogui as at

def aperta_tab(qtd):
    for i in range(qtd):
        at.press("tab")
        at.sleep(0.02)

at.hotkey("win","r")
at.write("chrome",0.2)
at.press("enter")
at.sleep(2)
at.write("www.youtube.com",0.2)
at.press("enter")
at.sleep(4)
aperta_tab(4)
at.write("Neymar jr",0.2)
at.press("enter")