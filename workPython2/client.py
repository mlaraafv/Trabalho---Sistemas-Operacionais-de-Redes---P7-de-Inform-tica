import socket
from is_number import *

# cria um objeto do tipo socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1" #Endereço IP do servidor
port = 9999 #Porta que conecta o cliente ao servidor
s.connect((host, port)) # conecta a porta ao IP
i=0
print("\nConexão estabelecida\n") 

while True:

    if i==1:
        msg = s.recv(4096)
        s.send("Send from client to server\n".encode('ascii'))

    while True:

        if i == 0:
            msg = s.recv(4096)
            print("+==========================+\n")
            print ("%s\n" % msg.decode('ascii'))

        print("+==========================+")
        print("+ 1 - PARA CONVERTER MOEDA +")
        print("+ 2 - PARA CONVERTER TEMPO +")
        print("+ 3 - SAIR                 +")
        print("+==========================+")

        optionMenu = str(input("\nEscolha uma opção de conversão: "))

        i=1
        while True:

            if optionMenu == "1":
                # OPÇÃO DE COVERSÃO DE MOEDAS

                print("\n1 - DOLAR | 2 - REAL | 3 - EURO | 4 - VOLTAR PARA O MENU \n")

                optionMenuMOEDA1 = str(input("\nEscolha a moeda que você deseja conveter: "))

                if ( optionMenuMOEDA1.isnumeric() == True):
                    optionMenuMOEDA1 = int(optionMenuMOEDA1)
                else:
                    print("Digite somente números\n") 
                    break

                # validação
                if ( (optionMenuMOEDA1 > 4) or (optionMenuMOEDA1 < 1) ): 
                    print("\n* Opção inválida\n") 
                    break
                
                # validação
                if ( optionMenuMOEDA1 == 4 ): 
                    #saindo...
                    break       

                values = 'currency#'
                values = str(values) + str(optionMenuMOEDA1) + "#"

                valueMoeda1 = str(input("Digite o valor: "))

                if ( is_number(valueMoeda1) == True):
                    valueMoeda1 = float(valueMoeda1)
                else:
                    print("Digite somente números\n") 
                    break

                values = str(values) + str(valueMoeda1) + "#"


                print("\n1 - DOLAR | 2 - REAL | 3 - EURO | 4 - VOLTAR PARA O MENU\n")

                optionMenuMOEDA2 = str(input("Pra qual moeda você deseja converter: "))

                if ( optionMenuMOEDA2.isnumeric() == True):
                    optionMenuMOEDA2 = int(optionMenuMOEDA2)
                else:
                    print("Digite somente números\n") 
                    break

                # validação
                if ( (optionMenuMOEDA2 > 4) or (optionMenuMOEDA2 < 1) ): 
                    print("\n* Opção inválida\n") 
                    break

                # validação
                if ( optionMenuMOEDA1 == optionMenuMOEDA2 ):
                    print("\nNão faz sentido você converter para a mesma moeda  \n") 
                    break

                # validação
                if ( optionMenuMOEDA2 == 4 ): 
                    #saindo..
                    break
                
                values = str(values) + str(optionMenuMOEDA2) + "#"

                i=0
                s.send(values.encode('ascii'))

                break

            elif optionMenu == "2":
                # OPÇÃO DE CONVERSÃO DE HORA

                print("\n1 - HORA | 2 - MINUTO | 3 - SEGUNDO | 4 - VOLTAR PARA O MENU\n")

                optionMenuTime1 = str(input("\nEscolha a 1ª unidade que você deseja converter: "))

                if ( optionMenuTime1.isnumeric() == True):
                    optionMenuTime1 = int(optionMenuTime1)
                else:
                    print("Digite somente números\n") 
                    break

                values = 'time#'
                values = str(values) + str(optionMenuTime1) + "#"


                # validação
                if ( (optionMenuTime1 > 4) or (optionMenuTime1 < 0) ): 
                    print("\n* Opção inválida\n") 
                    break

                # validação
                if ( optionMenuTime1 == 4 ): 
                    break

                valueTime1 = str(input("\nEscolha o valor à converter: "))

                if ( is_number(valueTime1) == True):
                    valueTime1 = float(valueTime1)
                else:
                    print("Digite somente números\n") 
                    break

                values = str(values) + str(valueTime1) + "#"

                print("\n1 - HORA | 2 - MINUTO | 3 - SEGUNDO | 4 - VOLTAR PARA O MENU\n")

                optionMenuTime2 = str(input("\nEscolha a unidade a ser convertida: "))

                if ( optionMenuTime2.isnumeric() == True):
                    optionMenuTime2 = int(optionMenuTime2)
                else:
                    print("Digite somente números\n") 
                    break

                # validação
                if ( (optionMenuTime2 > 4) or (optionMenuTime2 < 1) ): 
                    print("\n* Opção inválida\n") 
                    break

                # validação
                if ( optionMenuTime1 == optionMenuTime2 ):
                    print("\nNão faz sentido você converter para a mesma unidade de tempo \n") 
                    break

                # validação
                if ( optionMenuTime2 == 4 ): 
                    #saindo..
                    break

                values = str(values) + str(optionMenuTime2) + "#"
                
                i=0
                s.send(values.encode('ascii'))

                break

                # enviar request para o servidor tcp
            elif optionMenu == "3":

                #sair
                s.close()
                exit()
            else:

                # validação
                print("\n* Opção inválida\n")
                break

print("\nConexão encerrada \n\n") 
s.close()