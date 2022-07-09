from Carro import Carro
from Drone import Drone
from Fila import Fila

lista_de_carro = Fila()
lista_de_drone = Fila()

def main():
    while True:
        menu = int(input(''' Escolha uma das opções:
            [0] - Fechar
            [1] - Adicionar Carros na fila
            [2] - Adicionar Drones na fila
            [3] - Remover Carros da fila
            [4] - Remover Drones da fila
            [5] - Imprimir Carros da fila
            [6] - Imprimir Drones da fila
            Opção: 
        '''))


        if menu == 0:
            print("Você finalizou o programa!!")
            exit()


        elif menu == 1:
            print("Você escolheu a opção cadastrar carro: ")
            marcaCarro = input("Digite o nome da marca do Carro: ")
            modeloCarro = input("Digite o modelo do Carro: ")
            portasCarro = int(input("Digite a Quantidade de Portas do Carro: "))
            carro = Carro(marcaCarro, modeloCarro, portasCarro)
            lista_de_carro.adicionar(carro)
            print("Carro Adicionado com Sucesso!!")

        elif menu == 2:
            print("Você escolheu a opção cadastrar drone: ")
            marcaDrone = input("Digite o nome da marca do Drone: ")
            modeloDrone = input("Digite o modelo do Drone: ")
            qtdeHelicesDrone = int(input("Digite a Quantidade de Hélices do Drone: "))
            drone = Drone(marcaDrone, modeloDrone, qtdeHelicesDrone)
            lista_de_drone.adicionar(drone)
            print("Drone Adicionado com Sucesso!!")

        elif menu == 3:
          print("Você escolheu a opção para remover Carro da fila:")
          print("Você removeu o carro com sucesso!\nCarros disponíveis na fila:")
          lista_de_carro.remover()

        elif menu == 4:
          print("Você escolheu a opção para remover Drone da fila:")
          print("Você removeu o drone com sucesso!\nDrones disponíveis na fila:")
          lista_de_drone.remover()
            
        elif menu == 5:
          print("Você escolheu a opção para imprimir Carros da fila:")
          lista_de_carro.imprimir()

        elif menu == 6:
          print("Você escolheu a opção para imprimir Drone da fila:")
          lista_de_drone.imprimir()
        
        else:
            print('-'*30)
            print("Escolha uma opção que seja válida! Ou aperta '0' para sair...")
            print('-'*30)
            main()
main()