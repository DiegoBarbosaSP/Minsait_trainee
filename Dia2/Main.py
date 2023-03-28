from Conta_poupanca import conta_poupanca
from Conta_corrente import Current_account

cc = Current_account(id_conta=1, saldo=500, limite_conta=200)


cc.faca_deposito(quantia= 7)
print(cc.saldo)

cc.faca_retirada(508)
print(cc.saldo)



cc.faca_retirada(quantia= -25)
print(cc.saldo)

print(20*("--"))

cp = conta_poupanca(id_conta=321, saldo=100, taxa_retorno=0.05)
cp.faca_deposito(9)
print(cp.saldo)
cp.faca_retirada(quantia= 85)
print(cp.saldo)

rendimento_meses = cp.calcular_rendimento(tempo=1, unidade_tempo="anos")
rendimento_formatado = round(rendimento_meses,2)
print(rendimento_formatado)



