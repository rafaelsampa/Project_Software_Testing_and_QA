class Produto:
    def __init__(self, id, nome, preco, vegetariano):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.vegetariano = vegetariano


class Pedido:
    def __init__(self):
        self.itens = []
        self.status = "Aberto"
        self.garcom_chamado = False
        self.desconto = 0.0
        self.avaliacao = None
        self.reserva = None