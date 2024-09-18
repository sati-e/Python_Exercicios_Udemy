
# calculadora dois números, +, -, * e /

# função saida
def deseja_sair():
    sair = input("Sair? [s]").lower()
    return sair.startswith('s')

# loop calculadora
while True:
    
    # input e edfinição dde operadores
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    
    operadores = '+-/*'
    
    operacao = input("Digite uma operação +, -, / ou *: ")
    numeros_valios = None
    
    # transformação para float e validação dos números
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
        numeros_validos = True
    except ValueError:
        print("Um ou mais números são inválidos")
        if deseja_sair():
            break
        else:
            continue
    
    # validação dos operadores
    if operacao not in operadores:
        print("operaor inválio")
        continue
    
    if len(operacao) > 1:
        print("Digite apenas um operador")
        continue
    
    # realização das contas        
    print("Realizano a conta: ")
    if operacao == "+":
        print(f"{num_1} + {num_2} = ", num_1 + num_2)        
    
    elif operacao == "-":
        print(f"{num_1} - {num_2} = ", num_1 - num_2)
    
    elif operacao == "*":
        print(f"{num_1} * {num_2} = ", num_1 * num_2)
    
    elif operacao == "/":
        if num_1 == 0:
            print("Divisão impossível")
        else:    
            print(f"{num_1} / {num_2} =", num_1/num_2)
    else:
        print("Alguma coisa não esta certa")
        
    # chama a função de saida
    if deseja_sair():
        break