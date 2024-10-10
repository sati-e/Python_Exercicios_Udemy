# calcular primeiro digito cpf:
# coletar soma dos 9 primeiros digitos 456.231.345-34
# multiplicando cada um dos digitos por uma contagem regressiva de 10
# 10=4, 9=5, 8=6..., somar todos e multiplicar por 10.
# obter o resto da divisao da conta anterior por 11, e se for maior q 9:
# resultado = 0, se n o resultado é o valor da conta

# calculo do segundo digito:
# Exatamente igual o do primeiro
# mas adicionar mais o primeiro dígito do cpf na conta
# se o resultado anterior for maior que 9:
# o resultado é 0, caso contrário é o valor da conta

import re
import sys

input_cpf = input("Digite os números do cpf: ")   # imput numero do cpf

# retirar characteres entre os números
cpf = re.sub(
    r'[^0-9]',
    '',
    input_cpf
)

# verifica se é uma sequência de numeros repetida
ver_repeticao = input_cpf == input_cpf[0] * len(input_cpf)
if ver_repeticao:
    print("CPF inválido")
    sys.exit()

# selecionar os digitos até 9
nove_digitos = cpf[:9]

multip_sum = 0
soma = 0

# loop do cálculo, "i" é a posição (utilizado para a contagem regressiva de 10, que multiplicará os digitos) e "num" o número
for i, num in enumerate(nove_digitos):
    multip_sum += int(num) * (10 - i)       # multiplicação de cada numero pela contagem regressiva de 10, e soma de todos eles

digito = (multip_sum * 10) % 11     # multiplicação do resultado (multip_sum) por 10 e acha o resto da divizão do número por 11
    
# verificação e criação do primeiro dígito
primeiro_digito = digito if digito <= 9 else 0

# cálculo do segundo dígito:
dez_digitos = nove_digitos + str(primeiro_digito)    # adicionar o primeiro dígito no cálculo

for i, num in enumerate(dez_digitos):
    multip_sum += int(num) * (11 - i)

digito = (multip_sum * 10) % 11
    
segundo_digito = digito if digito <= 9 else 0

# juntar os dígitos
cpf_final = nove_digitos + str(primeiro_digito) + str(segundo_digito)

# verifica se é verdadeiro
if cpf_final == cpf:
    print(f'O CPF: {cpf} é válido')
else:
    print(f'O CPF: {cpf_final} é inválido')