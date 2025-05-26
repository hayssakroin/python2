from banco import Conta

conta1 = Conta(123, "10050-10", "franciscocisco", 7.0, 1234)
conta2 = Conta(143, "10040-19", "haysiti", 7.0, 1234)



conta1.pix(200, conta2)
print(conta1.extrato())
print(conta2.extrato())