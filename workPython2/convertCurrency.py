
class convertCurrency:
    
    def __init__(self, valor):
        self.valor = valor

    def real_dolar(self): 

        const_dolarToReal = "5.09"
        valor1 = float(self.valor) * float(const_dolarToReal)
        self.ResultadoDaConversao1 = valor1    
        return self.ResultadoDaConversao1
    
    def dolar_euro(self):
        const_dolarToEuro = "0.83"
        valor2 = float(self.valor) * float(const_dolarToEuro)
        self.ResultadoDaConversao2 = valor2
        return self.ResultadoDaConversao2

    def euro_real(self):  
        const_euroToReal = "6.17"
        valor3 = float(self.valor) / float(const_euroToReal)
        self.ResultadoDaConversao3 = valor3
        return self.ResultadoDaConversao3

    def dolar_real(self): 
        const_dolarToReal = "5.09"
        valor11 = float(self.valor) / float(const_dolarToReal)
        self.ResultadoDaConversao11 = valor11
        return self.ResultadoDaConversao11
    
    def euro_dolar(self):
        const_dolarToEuro = "0.83"
        valor22 = float(self.valor) / float(const_dolarToEuro)
        self.ResultadoDaConversao22 = valor22
        return self.ResultadoDaConversao22

    def real_euro(self):  
        const_euroToReal = "6.17"
        valor33 = float(self.valor) * float(const_euroToReal)
        self.ResultadoDaConversao33 = valor33
        return self.ResultadoDaConversao33