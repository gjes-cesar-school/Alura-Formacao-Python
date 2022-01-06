class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def imprimir_data_formatada(self):
        print("{0}/{1}/{2}".format(self.dia, self.mes, self.ano))