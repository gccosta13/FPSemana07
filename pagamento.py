class Pagamento:

    def processar_pagamento(self, valor):
        pass

class CartaoCredito(Pagamento):
    num_cartao = ""
    titular = ""
    validade = ""
    ccv = ""

    def __init__(self, numero_cartao, nome_titular, validade, ccv):
        super().__init__()
        self.num_cartao = numero_cartao
        self.titular = nome_titular
        self.validade = validade
        self.ccv = ccv

    def processar_pagamento(self, valor):
        print(f"€{valor:.2f} com Cartão de Crédito ({self.num_cartao})")

class PayPal(Pagamento):
    email = ""

    def __init__(self, email):
        super().__init__()
        self.email = email

    def processar_pagamento(self, valor):
        print(f"€{valor:.2f} com PayPal (email: {self.email})")

class TransferenciaBancaria(Pagamento):
    banco = ""
    agencia = ""
    conta = ""

    def __init__(self, banco, agencia, conta):
        super().__init__()
        self.banco = banco
        self.agencia = agencia
        self. conta = conta

    def processar_pagamento(self, valor):
        print(f"€{valor:.2f} com Tranferência Bancária (banco: {self.banco}, conta: {self.conta})")

def realizar_pagamento(TipoPagamento: Pagamento, valor):
    TipoPagamento.processar_pagamento(valor)

cartao_credito = CartaoCredito(numero_cartao="1234 5678 9012 3456", nome_titular="Jo~ao Silva", validade="12/25", ccv="123")
paypal = PayPal(email="joao.silva@email.com")
transferencia = TransferenciaBancaria(banco="Banco Central", agencia="1234", conta="12345678")

realizar_pagamento(cartao_credito, 150.00)
realizar_pagamento(paypal, 200.00)
realizar_pagamento(transferencia, 300.00)