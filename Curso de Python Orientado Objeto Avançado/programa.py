from typing import List


class Programa:
    def __init__(self, nome , ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome (self):
        return self._nome

    @nome.setter
    def nome (self, nome):
        self._nome = nome.title()
    
    @property
    def ano (self):
        return self._ano
    
    @ano.setter
    def ano (self, ano):
        self._ano = ano
    
    @property
    def likes (self):
        return self._likes
    
    def dar_likes (self):
        self._likes += 1
    
    def __str__(self):
        return f"Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}"

class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f"Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self.likes}"


class Serie (Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada
    
    def __str__(self):
        return f"Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporada} - Likes: {self.likes}"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem (self):
        return self._programas
    
    def __len__ (self):
        return len(self._programas)

    def __getitem__ (self, item):
        return self._programas[item]
    
 
  


   



vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmp = Filme("todo mundo em pânico", 1999, 100)
demolidor = Serie("demolidor", 2016, 5)
got = Serie("games of thrones", 2011, 10)



vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

tmp.dar_likes()
tmp.dar_likes()

demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

filmes_e_series = [vingadores, atlanta, tmp, demolidor]

playlist_fim_de_semanda = Playlist("Fim de semana", filmes_e_series) 

print(f"Tamanho da Playlist: {len(playlist_fim_de_semanda)}")

for programas in playlist_fim_de_semanda:
    print(programas)

print(playlist_fim_de_semanda[0])
   
print(f"Tá ou não tá? {demolidor in playlist_fim_de_semanda}")

for programas in playlist_fim_de_semanda[1:3]:
    print(programas)


