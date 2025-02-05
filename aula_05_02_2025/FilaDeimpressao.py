#Vamo simular como funciona o algoritimo de uma impressora que pode receber impressao de diversos computadores, vamos pensar em uma fila.

#funçoes de interação com o usuario
def menu()
    fila_impressao=FilaDeImpressao()
    #criando uma instancia para a classe
    
    fila_impressao.configurar_iniciar()
    #configurar os atributos de entrada
    
    while True:
        #opçoes para nosso usuario
        print("opções:")
        print("1 - Adicionar um trabalho na fila de impressão")
        print("2 - imprimir o proximo trabalho da fila")
        print("3 - mostrar a fila de impressão")
        print("4 - sair")
        escolha = input("Escolha uma opção de 1 até 4: ")
        #aqui vai ser lido a escolha do usuario
    
        if escolha == "1":
            trabalho=input("digite o nome do trabalho a ser impresso: ") 
            #maquina da pessoa que esta imprimindo
            fila_impressao.adicionar_trabalho(trabalho)
        elif escolha == "2":
            fila_impressao.processar_trabalho()
        elif escolha == "3":
            fila_impressao.mostrar_fila()
        elif escolha == "4":
            print("flw mano tmj")
            break
        else:
            print("opção inválida")