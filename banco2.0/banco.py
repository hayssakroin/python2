class Conta:
    def __init__(self, agencia, numero, titular, saldo, senha):
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def extrato(self):
        return self.__saldo

    def saque(self, valor):
        if self.__saldo >= valor > 0:
            self.__saldo -= valor
            return True
        else: 
            return False


    def deposito(self, valor):
        if valor > 0:
            self.__saldo += -valor
            return True
        else: 
            return False


 
    def pix(self, valor, conta):
        if self.__saldo >= valor and valor > 0:
                                       