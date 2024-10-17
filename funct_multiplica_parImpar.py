
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def MultiplicaArgs(*numeros):
    multiplica = 1
    for num in numeros:
        multiplica *= num
    return multiplica

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def ParImpar():
    print("Digite um número inteiro e direi se é par ou ímpar")
    numero = int(input("Número: "))
    
    par = numero %2 == 0
    
    if par:
        return f"O número {numero} é par"
    return f"O número {numero} é ímpar"
        
if __name__ == "__main__":
    print(MultiplicaArgs(3,6))
    print(ParImpar())
        