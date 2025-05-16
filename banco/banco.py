def cria_conta(agencia, numero, titular, saldo, limite, senha):
    conta = {
        "agencia": agencia,
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite,
        "senha": senha
    }
    return conta

conta2 = cria_conta(123, "2002-2", "ciclano", 200.0, 500.0, 1234)
print(f"agencia: {conta2['agencia']}, conta: {conta2['numero']} - saldo: {conta2['saldo']}")

