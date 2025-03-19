import time


def compteur(n):
    while n <= 1000:
        print(f"Compteur : {n}")
        n += 1
        time.sleep(1)
compteur(0)
    