from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "www.bitbank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
argumento = ExtratorArgumentosUrl(url)
print(f"Url validada: {ExtratorArgumentosUrl.url_valida(url)}")
moeda_origem, moeda_destino = argumento.extrair_argumentos()
print(f"Moeada de Origem: {moeda_origem} e Moeda de Destino: {moeda_destino}")








# argumento = "www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
# index = argumento.find("?")
# sub_string = argumento[index + 1 : ]
# print(sub_string)
# sub_string2 = argumento.split("?")
# print(sub_string2)


# index = url.find("moedadestino")
# sub_string = url[index +len("moedadestino") +1:]
# print(sub_string)

