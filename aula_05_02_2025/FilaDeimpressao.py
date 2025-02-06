#Vamo simular como funciona o algoritimo de uma impressora que pode receber impressao de diversos computadores, vamos pensar em uma fila.
class FilaDeImpressao:
    
    def configurar_iniciar(self):
        self.fila = []
        #isso daqui vai guardar a fila de impressao no vetor fila
    
    def adicionar_trabalho(self, trabalho):
        self.fila.append(trabalho)
        print(F"Trabalho '{trabalho}' adicionado na fila de impressão")
    
#remover o trabalho da lista (embaixo)
    
    def processar_trabalho(self):
        if not self.esta_vazia(): #verifica se a lista nao está vazia
            trabalho = self.fila.pop(0) #remove o primeiro elemento da lista
            print(f" o trabalho '{trabalho}' está sendo processado")
        else:
            print ("A fila esta vazia paizão")
        
#mostrar a fila de impressao
    def mostrar_fila(self):
        if self.esta_vazia():
            print("A fila esta vazia!")
        else: 
            print("fila atual de impressao: ")
            for trabalho in self.fila:
                print(f"-{trabalho}") #impremir cada trabalho da lista
                
            def esta_vazia(self):
                return len(self.fila) == 0
            #len verifica se o tamanho do vetor fila está zerado   

    #funçoes de interação com o usuario
def menu():
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
                
menu( )