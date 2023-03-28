from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, id_conta: int, saldo: float):
        self._id_conta: int = id_conta
        self._saldo: float = saldo

    @property
    def id_conta(self):
        return self._id_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo: float):
        if self._validador(novo_saldo):
            self._saldo = novo_saldo

    @abstractmethod
    def faca_deposito(self, quantia: float):
        pass

    @abstractmethod
    def faca_retirada(self, quantia: float):
        pass

    def _validador(self, valor: float) -> bool:
        return valor >= 0.0
