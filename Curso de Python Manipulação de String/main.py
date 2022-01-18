argumento = "www.bytebank.com.br/cambio?moedaorigem=real"

index = argumento.find("?")
sub_string = argumento[index + 1 : ]
print(sub_string)

sub_string2 = argumento.split("?")
print(sub_string2)

