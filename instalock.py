# CodedBy: Ic3zy
# My İnstagram: lc3zy_

import pyautogui as py
from pynput import keyboard
import threading

possition = []
running = False

def onepossition():
    global possition 
    if len(possition) < 2:
        x, y = py.position()
        print(f"fare Koordinatları: X = {x}, Y = {y}")
        possition.append([x, y])
        print("kaydedilen koordinatlar:", possition)
    else:
        print("2 tane kordinat zaten tanımlı")

def clck(pos, pos2):
    py.moveTo(pos, pos2)
    py.click()

def click_loop():
    while running:
        for pos in possition:
            clck(pos[0], pos[1])

def on_press(key):
    global running 
    global possition  
    try:
        print(f"tusa basıldı: {key.char}")
    except AttributeError:
        print(f"ozel tus: {key}")

    print("len", len(possition)) 

    if key == keyboard.Key.insert:
        if len(possition) < 2:  
            print("Insert")
            onepossition()
        else:
            print("zaten 2 koordinat kaydedildi")
    elif key == keyboard.Key.end:
        if running:
            print("end tuşuna basıldı tıklama durduruluyor")
            running = False
        else:
            print("Tıklama zaten durdurulmuş durumda.")
    elif key == keyboard.Key.delete:
        if not running:
            print("delete tuşuna basıldı tıklama başlıyor")
            running = True
            thread = threading.Thread(target=click_loop)
            thread.start()
        else:
            print("tıklama zaten çalışıyorç")
    elif key == keyboard.Key.home:
        print("possition sıfırlanıyor")
        possition = [] 
        print("pos: ", possition)

def on_release(key):
    if key == keyboard.Key.esc:
        print("esc tuşuna basıldı Çıkmak istiyorsanız terminali kapatın")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
