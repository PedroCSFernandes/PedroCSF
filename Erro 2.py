import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.jogador_atual = 'X'
        self.tabuleiro = [['', '', ''],
                          ['', '', ''],
                          ['', '', '']]

    def clicar_celula(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == '':
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogador_atual)
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de jogo", f"O jogador {self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.alternar_jogador()

    def verificar_vitoria(self):
        # Verificar linhas
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != '':
                return True
        # Verificar colunas
        for i in range(3):
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != '':
                return True
        # Verificar diagonais
        if (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != '') or \
           (self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ''):
            return True
        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            for celula in linha:
                if celula == '':
                    return False
        return True

    def alternar_jogador(self):
        if self.jogador_atual == 'X':
            self.jogador_atual = 'O'
        else:
            self.jogador_atual = 'X'

    def reiniciar_jogo(self):
        self.jogador_atual = 'X'
        self.tabuleiro = [['', '', ''],
                          ['', '', ''],
                          ['', '', '']]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text='')

janela = tk.Tk()
janela.title("Jogo da Velha")

jogo_da_velha = JogoDaVelha()

jogo_da_velha.botoes = []
for i in range(3):
    linha_botoes = []
    for j in range(3):
        botao = tk.Button(janela, text='', width=10, height=5,
                          command=lambda linha=i, coluna=j: jogo_da_velha.clicar_celula(linha, coluna))
        botao.grid(row=i, column=j)
        linha_botoes.append(linha_botoes)
    jogo_da_velha.botoes.append(linha_botoes)

janela.mainloop()

# Não aparece os X e as O 