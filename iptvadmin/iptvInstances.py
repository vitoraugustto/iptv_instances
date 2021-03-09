import PySimpleGUI as sg
# import subprocess
import pyautogui
import time

# subprocess.call([ 'runas', '/user:Administrator', '/password:123', 'C:/Program Files/IP.TV Studio HD 518/iptv.exe' ])

sg.theme('DarkGrey12')


layout = [
    [sg.Text("Quantidade de Instâncias IPTV:", size=(23, 0)), sg.Input(size=(8, 0), key="qty")],
    [sg.Button("OK", size=(10, 1))]
]

window = sg.Window("Abrir Instâncias IPTV", icon='references/iconcmsp.ico', element_justification='center').layout(layout)

event, values = window.read()

qty = values['qty']

class IPTV():
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def open_instance(self):
        if (int(qty) < 9):
            for i in range(int(qty)):
                iptv = pyautogui.locateCenterOnScreen('iptvadmin/references/iptv.png', confidence=0.8)
                pyautogui.keyDown('shift')
                pyautogui.click(iptv, button='right')
                pyautogui.keyUp('shift')
                time.sleep(.7)
                pyautogui.press('f')
                pyautogui.press('enter')
                pyautogui.press('up')
                pyautogui.write(self.user)
                pyautogui.press('tab')
                pyautogui.write(self.password)
                pyautogui.press('enter')

        else:
            pyautogui.alert('para de tentar crashar o pc')


if event == 'OK':
    window.Hide()

    vitu = IPTV('administrador', '123')
    vitu.open_instance()
