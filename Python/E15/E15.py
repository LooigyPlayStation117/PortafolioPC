import pyautogui, subprocess, time
import webbrowser

url = "https://forms.office.com/pages/responsepage.aspx?id=EZDKymp73kSGHwlaLKiDt4wXC_YfIWlGrUcWrbkA4-NUOVNHMk5FT1k3VVJRRVpKUVlJSElIVE02TC4u"
refran = "Camaron que se duerme, perdio su silla. La verdad no me acuerdo como iva."
correofalso = "SalesMan1997@hotmail.com"
print(url)
print(correofalso)
print(refran)
#cuenta = input("Esribe tu correo univercitario: ")
#contraseña = input("Esribe tu contraseña: ")
# luis.ramoscstn@uanl.edu.mx

#subprocess.call(["cmd", "/c", "start", "/max", 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'])
webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)
#abrir el link
#pyautogui.click(150,50)
#pyautogui.typewrite(link)
#pyautogui.press('enter')
#ingresar la cuenta
#pyautogui.click(670,485)
#pyautogui.typewrite(cuenta)
#pyautogui.press('enter')
#ingrear la contraseña
#pyautogui.click(670,485)
#pyautogui.typewrite(contraseña)
#pyautogui.press('enter')

time.sleep(1)

#hacer la pagina mas pequeña
pyautogui.keyDown('ctrl')
pyautogui.keyDown('-')
pyautogui.keyUp('-')
pyautogui.keyUp('ctrl')

#Escoger Mrvl/DC
pyautogui.click(528,437)

#Escribir refran
pyautogui.click(532,640)
pyautogui.typewrite(refran)

#Escoger mejor hora para el pastel
pyautogui.click(540,775)
pyautogui.click(540,814)

#Direccion de correo falsa
pyautogui.click(530,913)
pyautogui.typewrite(correofalso)

#Envio de formulario 
pyautogui.click(570,995)



#pyautogui.press('tab')
#pyautogui.typewrite('Bye!')
#pyautogui.keyDown('ctrl')
#pyautogui.keyDown('s')
#pyautogui.keyUp('s')
#pyautogui.keyUp('ctrl')
#pyautogui.click(100,100)
#pyautogui.typewrite('test.txt')
#pyautogui.press('tab')
#pyautogui.press('enter')

