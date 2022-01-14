class Funcionario:
    def __init__(self, nome) -> None:
        self.nome = nome
    def registra_horas(self, horas):
        print("Horas registradas...")
    
    def mostrar_tarefas(self):
        print("Fez muita coisa...")
    
class Caelum (Funcionario):
    def mostrar_tarefas(self):
        print("Fez muita coisa... Caelumer")
    
    def busca_curso_do_mes(self, mes = None):
        print(f"Mostrando cursos - {mes}" if mes else "Mostrando cursos desse mês")

class Alura (Funcionario):
    # def mostrar_tarefas(self):
    #     print("Fez muita coisa... Alurete")
    
    def busca_perguntas_sem_respostas(self):
        print("mostrando perguntas não respondidas do fórum")

class Hipster:
    def __str__(self) -> str:
        return f"Hispter, {self.nome}"
    

class Junio(Alura):
    pass

class Pleno(Alura,Caelum):
    pass

class Senior (Alura, Caelum, Hipster):
    pass


# luan = Pleno()
# luan.mostrar_tarefas()
# # luan.busca_perguntas_sem_respostas()
# # luan.busca_curso_do_mes()

# print("\n\n") #mro

# jose = Junio()
# jose.mostrar_tarefas()
# # jose.busca_perguntas_sem_respostas()

ze = Senior("Zé")
print(ze)



