from banco import Conta

conta1 = Conta(123, "10050-10", "franciscocisco", 7.0, 1234)
print(f'saldo em conta corrente: {conta1.extrato()}')

