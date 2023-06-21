import time

def cronometro(segundos):
    for i in range(segundos, 0, -1):
        print(f"Tempo restante: {i} segundos")
        time.sleep(1)
    
    print("Tempo esgotado!")


    #Ao clicar nada acontecia