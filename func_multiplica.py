# Exercícios
# Crie funções que multiplicam os números

def multiplicador(parametro):
    numeroMulti = int(input("Quantas vezes deseja multiplicar o número? "))
    resultado = parametro * numeroMulti
    print(resultado)
    
if __name__ == "__main__":
    multiplicador(int(input("Qual número deseja multiplicar? ")))

