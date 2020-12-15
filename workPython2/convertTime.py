
class convertTime:

    def __init__(self, valor):
        self.valor = float(valor)

    def hora_minuto(self):

        const_hourToMinute = "60"
        resultado1 = self.valor / float(const_hourToMinute)
        self.ResultadoDaConversaoTempo1 = resultado1
        return self.ResultadoDaConversaoTempo1

    def minuto_segundo(self):

        const_MinutesToSegs = "60"
        resultado2 = self.valor / float(const_MinutesToSegs)
        self.ResultadoDaConversaoTempo2 = resultado2
        return self.ResultadoDaConversaoTempo2

    def hora_segundo(self):

        const_HourToSegs = "3600"
        resultado3 = float(self.valor) / float(const_HourToSegs)
        self.ResultadoDaConversaoTempo3 = resultado3
        return self.ResultadoDaConversaoTempo3

    def minuto_hora(self):

        const_MinutesToHour = "60"
        resultado1 = self.valor * float(const_MinutesToHour)
        self.ResultadoDaConversaoTempo11 = resultado1
        return self.ResultadoDaConversaoTempo11

    def segundo_minuto(self):

        const_SegsToMinutes = "60"
        resultado2 = self.valor * float(const_SegsToMinutes)
        self.ResultadoDaConversaoTempo22 = resultado2
        return self.ResultadoDaConversaoTempo22

    def segundo_hora(self):

        const_SegsToHour = "3600"
        resultado3 = self.valor * float(const_SegsToHour)
        self.ResultadoDaConversaoTempo33 = resultado3
        return self.ResultadoDaConversaoTempo33