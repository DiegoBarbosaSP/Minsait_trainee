from Conta import Conta


class Current_account(Conta):
    def __init__(self, id_conta: int, saldo: float, limite_conta: float):
        super().__init__(id_conta, saldo)
        self.limite_conta = limite_conta

    @property
    def limite_conta(self):
        return self._limite_conta

    @limite_conta.setter
    def limite_conta(self, novo_limite):
        if self._validador(novo_limite):
            self._limite_conta = novo_limite

    def faca_deposito(self, quantia: float):
        if self._validador(quantia):
            self.saldo += quantia
        else:
            raise ValueError("Quantia não pode ser negativa")

    def faca_retirada(self, quantia: float):
        try:
         if not self._validador(quantia):
            raise ValueError("Quantia não pode ser negativa")

         if quantia <= self.saldo:
            self.saldo -= quantia
         else:
            raise Exception("Quantia excede seu saldo")
        except ValueError as ve:
         print(ve)
        except Exception as e:
         print(f"Erro: {e}")
