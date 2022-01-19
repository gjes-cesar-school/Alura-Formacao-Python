class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.url_valida(url):
            self.url = url
        else:
            raise LookupError("Url Inválida!")
        
    @staticmethod   
    def url_valida(url):
        if url:
            return True
        else:
            return False
    
    def extrair_argumentos(self):
        origem = "moedaorigem="
        destino = "moedadestino="
        indice_inicial_moeda_origem = self.indice_moeda(origem) 
        indice_final_moeda_origem = self.url.find("&") 
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        if(moeda_origem == "moedadestino"):
            self.trocar_moeda()
            indice_inicial_moeda_origem = self.indice_moeda(origem) 
            indice_final_moeda_origem = self.url.find("&") 
            moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        
        indice_inicial_moeda_destino = self.indice_moeda(destino)
        moeda_destino = self.url[indice_inicial_moeda_destino:]
        return moeda_origem, moeda_destino

    def indice_moeda(self, moeda):
        return self.url.find(moeda)+len(moeda)

    def trocar_moeda (self):
        self.url = self.url.replace("moedadestino", "real", 1)

       