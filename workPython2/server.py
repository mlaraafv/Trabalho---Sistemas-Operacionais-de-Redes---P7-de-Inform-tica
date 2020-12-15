import socket

from convertCurrency import convertCurrency
from convertTime import convertTime

# cria um objeto do tipo socket
serversocket = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)

host = "127.0.0.1" #Endereço IP do servidor
port = 9999 #Porta que conecta o cliente ao servidor
serversocket.bind((host, port)) # Junta a porta ao IP

serversocket.listen(5) #Quantidade de conexões que ele escuta simultaneamente
while True:
    
    clientsocket, addr = serversocket.accept() #aceita a conexão solicitada pelo cliente
    print("\nConexão estabelecida de %s" % str(addr))

    clientsocket.send("Send from server to client".encode('ascii')) 

    while True:
        msg = clientsocket.recv(4096)
        if not msg: break
        print ("%s" % msg.decode('ascii')) 

        values = msg.decode('ascii')
        value = str(values).split("#")

        while True:

            if ( len(value) > 3 and value[0] == 'currency'):

                # conversao da moeda

                moeda1 = value[1]
                valorMoeda1 = value[2]
                moeda2 = value[3]

                err = {}

                err['1'] = " DOLAR(es)"
                err['2'] = " REAL(is)"
                err['3'] = " EURO(s)"

                print("\n\nO cliente requisitou uma conversão de moeda, " + str(valorMoeda1) + str(err[moeda1]) + " para" + str(err[moeda2]))


                if ( moeda1 == "1" and  moeda2 == "2" ):

                    op = convertCurrency(valorMoeda1)
                    result = "Em reais e: " + str(op.real_dolar())                

                elif ( moeda1 == "1" and  moeda2 == "3" ):

                    op = convertCurrency(valorMoeda1)
                    result = "Em euros e: " + str(op.euro_dolar())                     

                elif ( moeda1 == "2" and  moeda2 == "1" ):

                    op = convertCurrency(valorMoeda1)
                    result = "Em dolares e: " + str(op.dolar_real())     

                elif ( moeda1 == "2" and  moeda2 == "3" ):

                    op = convertCurrency(valorMoeda1)
                    result = "Em euros e: " + str(op.real_euro())     

                elif ( moeda1 == "3" and  moeda2 == "1" ):

                    op = convertCurrency(valorMoeda1)
                    result = "Em dolares e: " + str(op.dolar_euro())  

                elif ( moeda1 == "3" and  moeda2 == "2" ):

                    op = convertCurrency(valorMoeda1)
                    result = "Em reais e: " + str(op.real_euro())                  

                else:
                    clientsocket.send("Nao foi possivel fazer a conversao! ".encode('ascii')) 
                    break

                clientsocket.send(result.encode('ascii')) 
                break


            elif ( len(value) > 3 and value[0] == 'time'):

                #conversao do tempo

                unid1 = value[1]
                valorUnid1 = float(value[2])
                unid2 = value[3]
                err = {}

                err['1'] = " HORA(s)"
                err['2'] = " MINUTO(s)"
                err['3'] = " SEGUNDO(s)"

                print("O cliente requisitou uma conversão de tempo, " + str(valorUnid1) + str(err[unid1]) + " para " + str(err[unid2]))

                if ( unid1 == "1" and  unid2 == "2" ):

                    op = convertTime(valorUnid1)
                    result = "Em minutos e: " + str(op.minuto_hora())                

                elif ( unid1 == "1" and  unid2 == "3" ):

                    op = convertTime(valorUnid1)
                    result = "Em segundos e: " + str(op.segundo_hora())                     

                elif ( unid1 == "2" and  unid2 == "1" ):

                    op = convertTime(valorUnid1)
                    result = "Em horas e: " + str(op.hora_minuto())     

                elif ( unid1 == "2" and  unid2 == "3" ):

                    op = convertTime(valorUnid1)
                    result = "Em segundos e: " + str(op.segundo_minuto())     

                elif ( unid1 == "3" and  unid2 == "1" ):

                    op = convertTime(valorUnid1)
                    result = "Em horas e: " + str(op.hora_segundo())  

                elif ( unid1 == "3" and  unid2 == "2" ):

                    op = convertTime(valorUnid1)
                    result = "Em minutos e: " + str(op.minuto_segundo())                  

                else:
                    clientsocket.send("Nao foi possivel fazer a conversao! ".encode('ascii')) 
                    break

                clientsocket.send(result.encode('ascii')) 
                break

            else:
                clientsocket.send(("Opcoes invalidas %s" % value[0]).encode('ascii')) #cores
                break

    clientsocket.send("Send from server to client".encode('ascii')) 

    
print ('\nConexão encerrada!', clientsocket)
clientsocket.close()