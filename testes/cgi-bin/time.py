
import cgitb, cgi
cgitb.enable()
form = cgi.FieldStorage()
ValorTempo = int(form.getvalue('ValorTempo'))
Tempo1=form.getvalue("Tempo1")
Tempo2=form.getvalue("Tempo2")
Valorfinal1=0

if Tempo1=="Hora":
    if Tempo2=="Minuto":
        Valorfinal1=ValorTempo*60
    elif Tempo2=="Segundo":
         Valorfinal1=ValorTempo*3600
    else:
        Valorfinal1='Ops, nao pode converter para a mesma unidade, retorne para a tabela'
if Tempo1=="Minuto":
    if Tempo2=="Hora":
        Valorfinal1=ValorTempo/60
    elif Tempo2=="Segundo":
         Valorfinal1=ValorTempo*60
    else:
        Valorfinal1='Ops, nao pode converter para a mesma unidade, retorne para a tabela' 
if Tempo1=="Segundo":
    if Tempo2=="Hora":
        Valorfinal1=ValorTempo/3600
    elif Tempo2=="Minuto":
         Valorfinal1=ValorTempo/60
    else:
        Valorfinal1='Ops, nao pode converter para a mesma unidade, retorne para a tabela'       

print("Content-type:text/html\r\n\r\n")
print("""<html>
            <head>
                <meta charset=\"UTF-8\">
                <title>Sistema de Conversão de Medidas</title>
            </head>
            <body>""")
print(f'<h1>O Resultado da conversao e: </h1>')
print(f'<h2> {Valorfinal1}</h2></body></html>')
    

