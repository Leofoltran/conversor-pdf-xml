import pyautogui as pa
import time
import pyperclip
pa.PAUSE = 1

pa.press('win')
pa.write("Brave")
pa.press('ENTER')
pa.write("youtube.com")
pa.press('ENTER')
time.sleep(2.8)
pa.click(x=891, y=138)
pyperclip.copy("Legião Urbana")
pa.hotkey('ctrl', 'v')
pa.press('ENTER')