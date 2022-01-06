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
        if(self.__saldo + self.__limite > valor_sacado):
            self.__saldo -= valor_sacado
        else:
            print("Saldo insuficiente para saque")

    def transferir(self,conta,valor_transferido):
            if(self.__saldo + self.__limite < valor_transferido):
                self.sacar(valor_transferido)
                conta.depositar(valor_transferido)
            else:
                print("Saldo insuficiente para transferencia")
