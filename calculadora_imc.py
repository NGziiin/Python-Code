imc = "imc"

while(imc):

    #inicio
    sim = 1
    nao = 2
    volta = 3

    continua = int(input("deseja continuar?\n Sim(1) Cancelar(2)\npara voltar para a calculadora digite (3)\nDigite o número: "))

    #selecionando opção
    if continua == nao:
        break

    #abrindo calculadora
    elif continua == volta:
        print("-------------------------")
        print("abrindo calculadora...")
        print("-------------------------")
        exec(open("calculadora.py").read())
        break
    
    #selecionando opção / erro
    elif continua == sim:

        #calculadora IMC
        peso = float(input("digite seu peso: "))
        altura = float(input("digite sua altura: "))

        resultado = peso / (altura * altura)
        print("seu IMC é:", resultado)

        #comentando sobre seu IMC
        if resultado <= 18.5:
            print("Vamos comer? você está abaixo do peso")
        elif resultado <= 24.9 and resultado >= 18.6:
            print("Parabéns! seu peso está ideal")
        elif resultado <= 29.9 and resultado >= 25:
            print("Cuidado! você está ficando gordinho(a)")
        elif resultado <= 34.9 and resultado >= 30:
            print("Vamos nos cuidar? você está obeso!")
        elif resultado <= 39.9 and resultado>= 30.1:
            print("Você está com obesidade grau 2")
        else:
            resultado >= 40
            print("Academia de segunda a sexta! \ndas 08:00 às 23:00 \nte aguardo lá")
    
    #mensagem de erro
    else:
        continua != sim, nao, volta
        print("não reconhecido! tente novamente.")