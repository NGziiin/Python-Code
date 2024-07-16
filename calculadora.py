calculadora = 'calculadora'

while (calculadora):
    
    #inicio
    escolha = int(input("qual vai ser o tipo de calculo?\nSoma(1), Subtração(2), Multiplicação(3), Divisão(4), Cancelar(0)\nPara calculadora IMC digite (5)\nDigite o número de acordo:"))
    multiplicacao = 3
    soma = 1
    divisao = 4
    subtracao = 2
    cancel = 0
    imc = 5
    
    #calculadora
    if escolha == multiplicacao:
        nu1 = int(input("digite o numero:"))
        nu2 = int(input("digite o segundo numero:"))
        re1 = nu1 * nu2
        print("o resultado é:",re1)
    elif escolha == soma:
        nu1 = int(input("digite o numero:"))
        nu2 = int(input("digite o segundo numero:"))
        re1 = nu1 ++ nu2
        print("o resultado é:",re1)
    elif escolha == divisao:
        nu1 = float(input("digite o numero:"))
        nu2 = float(input("digite o segundo numero:"))
        re1 = nu1/nu2
        print("o resultado é:",re1)
    elif escolha == subtracao:
        nu1 = int(input("digite o numero:"))
        nu2 = int(input("digite o segundo numero:"))
        re1 = nu1 - nu2
        print("o resultado é:",re1)
    
    #chamando calculadora imc
    elif escolha == imc:
        print("--------------------------")
        print("abrindo Calculadora IMC...")
        print("--------------------------")
        exec(open("imc.py").read())
        break

    #cancelar / erro
    elif escolha == cancel:
        break
    else:
        escolha!=multiplicacao, soma, divisao, subtracao, imc
        print("não reconhecido! tente novamente")