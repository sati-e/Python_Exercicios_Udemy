# contar quantas vezes a mesma letra apareceu no texto
# qual letra aparece mais vezes

# frase
frase = "I wish I hadn't done what I did. Mama meant well. She had a hard life." # - Pearl monologue

# declarando variáveis
i = 0
qtd_apareceu_mais = 0
letra_apareceu_mais = ''

# loop para a contagem de letras
while i < len(frase):
    letra_atual = frase[i]
    
    # elimina caracteres que não são letras
    if letra_atual == ' ' or letra_atual == '.' or letra_atual == "'":
        i += 1
        continue
        
    # conta a quantidade de letras e armazena o resultado em uma variável
    qtd_letra = frase.count(letra_atual)
    
    if qtd_apareceu_mais < qtd_letra:
        qtd_apareceu_mais = qtd_letra
        letra_apareceu_mais = letra_atual
    
    # contador
    i += 1
    
print(f"Apareceu mais: {letra_apareceu_mais} = {qtd_apareceu_mais} vezes")