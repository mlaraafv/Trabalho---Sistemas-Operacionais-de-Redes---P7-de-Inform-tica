import cgitb, cgi
cgitb.enable()
form= cgi.FieldStorage()
valor=float(form.getvalue("valor"))
Moeda1=form.getvalue("Moeda1")
Moeda2=form.getvalue("Moeda2")
Valorfinal=0
if Moeda1=="Euro":
    if Moeda2=="Dolar":
        Valorfinal=valor*1.2
    elif Moeda2=="Real":
         Valorfinal=valor*6.5
    else:
        Valorfinal='Ops, nao pode converter para a mesma unidade, retorne para a tabela'   
if Moeda1=="Dolar":
    if Moeda2=="Euro":
        Valorfinal=valor*0.83
    elif Moeda2=="Real":
         Valorfinal=valor*5.37
    else:
        Valorfinal='Ops, nao pode converter para a mesma unidade, retorne para a tabela' 
if Moeda1=="Real":
    if Moeda2=="Dolar":
        Valorfinal=valor*0.19
    elif Moeda2=="Euro":
        Valorfinal=valor*0.15
    else:
        Valorfinal='Ops, nao pode converter para a mesma unidade, retorne para a tabela'     
                                                      
print("Content-type:text/html\r\n\r\n")
print("""<html>
            <head>
                <meta charset=\"UTF-8\">
                <title> Sistema de Conversão de Medidas</title>
            </head>
            <body>""")

print(f'<h1>O Resultado da conversao e: </h1>')
print(f'<h2> {Valorfinal}</h2></body></html>')
    
