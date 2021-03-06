class Conta:
    # Definindo construtor da classe
    def __init__(self, numero, titular, saldo, limite = 1000):
        print("Construindo objeto {} ".format(self))
        # Definindo atributos da classe
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def mostrar_saldo(self):
        print("Saldo de: {0} e Limte: {1} do Titular: {2}".format(self.__saldo, self.__limite, self.__titular))
    
    def depositar(self, valor_depositado):
        self.__saldo += valor_depositado
    
    def sacar(self, valor_sacado):
        if(self.__pode_sacar(valor_sacado)):
            self.__saldo -= valor_sacado
        else:
            print("Saldo insuficiente para saque")
    
    def __pode_sacar(self, valor_retirar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_disponivel >= valor_retirar

    def transferir(self,conta,valor_transferido):
            if(self.__pode_sacar(valor_transferido)):
                self.sacar(valor_transferido)
                conta.depositar(valor_transferido)
            else:
                print("Saldo insuficiente para transferencia")
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB":'001', "Caixa":"104", "Bradesco":"237"}