# basicamente um jogo da forca sem enforcar alguém

import random

# lista de palavras
lista_palavras = ['mamao',"árvore", "chocolate", "livro", "correr", "praia", "desenho", "gato", "amigo", "mesa", "jantar", "viagem", "televisão", "esporte", "guitarra", "sorriso", "ceu", "cachorro", "sanduiche", "festa", "fotografia","sol", "lua", "tigre", "brincar", "dancar", "caminhar", "arte", "pintura", "cachoeira", "natureza", "internet", "avo", "biscoito", "sopa", "futuro", "sabio", "fantasia", "violinista", "magica", "relogio", "xicara",'batata', 'futebol', 'feliz', 'jogo', 'comer', 'desenhar', 'filme', 'computador', 'caneca', 'papel', 'correr', 'pular', 'musica', 'amarelo', 'marrom', 'talher', 'documentario',"jardim", "mar", "caneta", "gato", "filme", "aviao", "futebol", "piano", "fruta", "mesa", "teatro", "cachorro", "livro", "bolacha", "sorvete", "bailar", "correr", "pintor", "jogo", "manha", "noite"]

letra_certa = ''

# palavra escolhida randomicamente
palavra = lista_palavras[random.randrange(len(lista_palavras))]

# contador de vidas
vidas = 5

print("ADIVINHE A PALAVRA!\n"
      "Digite letras (uma de cada vez) para tentar achar a palavra.\n"
      "Você tem 10 vidas! 💜")

while True:

      # finalizar se a contagem de vida acabar
      if vidas == 0:
            print("Perdeu!")
            print("A palavra era: ", palavra)
            break
    
      # input de uma letra
      letra = input('Digite a letra: '.lower())
      
      # critica
      if len(letra) > 1:
          print("Digite apenas uma letra")
          continue
      
      # adiciona a letra acertada na "letra_certa"
      if letra in palavra:
          letra_certa += letra
      else:
            # contador
            vidas -= 1
      
      # verifica e adiciona a letra_certa a palavra formada
      palavra_formada = ''
      for l_secreta in palavra:
            if l_secreta in letra_certa:
                  palavra_formada += l_secreta
            else:
                  palavra_formada += '*'
      
      # se a palavra for formada completamente
      if palavra_formada == palavra:
            print("Acertou!\nPalavra: ", palavra_formada)
            break
                  
      print(palavra_formada)
