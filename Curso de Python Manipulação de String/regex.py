import re
celular1 = "(63)98146-6313"
celular2 = "(62)98166-6783"
celular3 = "(77)93146-8u13"


padrao = "[(][0-9]{2}[)][0-9]{5}[-][0-9]{4}"

retorno = re.search(padrao,celular1)

print(retorno.group())
