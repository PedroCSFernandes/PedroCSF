import random

def jogar():
    print("Bem-vindo ao jogo de Pedra, Papel, Tesoura, Lagarto e Spock!")
    print("Escolha o nível de dificuldade:")
    print("1. Fácil")
    print("2. Médio")
    print("3. Difícil")

    nivel = int(input("Digite o número do nível de dificuldade: "))
    if nivel < 1 or nivel > 3:
        print("Nível inválido. Tente novamente.")
        return

    print("Escolha uma opção:")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    print("4. Lagarto")
    print("5. Spock")

    opcoes = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
    escolha_jogador = int(input("Digite o número da sua escolha: ")) - 1

    if escolha_jogador < 0 or escolha_jogador >= len(opcoes):
        print("Escolha inválida. Tente novamente.")
        return

    escolha_computador = random.randint(0, 4)

    print("Você escolheu:", opcoes[escolha_jogador])
    print("O computador escolheu:", opcoes[escolha_computador])

    resultado = verificar_vencedor(escolha_jogador, escolha_computador)

    if nivel == 1:
        print("Você está jogando no nível Fácil.")
    elif nivel == 2:
        print("Você está jogando no nível Médio.")
    elif nivel == 3:
        print("Você está jogando no nível Difícil.")

    if resultado == 0:
        print("Empate!")
    elif resultado == 1:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

    
def verificar_vencedor(escolha_jogador, escolha_computador):
    if escolha_jogador == escolha_computador:
        return 0
    elif (escolha_jogador == 0 and (escolha_computador == 2 or escolha_computador == 3)) or \
            (escolha_jogador == 1 and (escolha_computador == 0 or escolha_computador == 4)) or \
            (escolha_jogador == 2 and (escolha_computador == 1 or escolha_computador == 3)) or \
            (escolha_jogador == 3 and (escolha_computador == 1 or escolha_computador == 4)) or \
            (escolha_jogador == 4 and (escolha_computador == 0 or escolha_computador == 2)):
        return 1
    else:
        return -1

jogar()

#mudar a ordem que estava o codigo