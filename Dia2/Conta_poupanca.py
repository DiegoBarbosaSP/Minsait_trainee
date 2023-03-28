from Conta import Conta



class conta_poupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_retorno: float):
        super().__init__(id_conta, saldo)
        self.taxa_retorno = taxa_retorno

    @property
    def taxa_retorno(self):
        return self._taxa_retorno

    @taxa_retorno.setter
    def taxa_retorno(self, nova_taxa):
        if self._validador(nova_taxa):
            self._taxa_retorno = nova_taxa

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


    def calcular_rendimento(self, tempo, unidade_tempo):  
    

       if unidade_tempo == "segundos":
          tempo_convertido = tempo / (60*60*24*7*4*12)  
       elif unidade_tempo == "dias":
            tempo_convertido = tempo / 365  
       elif unidade_tempo == "semanas":
            tempo_convertido = tempo / 52  
       elif unidade_tempo == "meses":
            tempo_convertido = tempo / 12  
       elif unidade_tempo == "anos":
            tempo_convertido = tempo
       else:
        
        raise ValueError("Unidade de tempo inválida.")
        
       rendimento = self.saldo * (1 + self.taxa_retorno) ** tempo_convertido - self.saldo
       return rendimento
    
    
    