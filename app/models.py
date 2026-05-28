"""Modelos de dados do sistema de pedidos do restaurante."""


class Produto:
    """Item disponível no cardápio."""

    def __init__(self, produto_id, nome, preco, vegetariano):
        self.id = produto_id
        self.nome = nome
        self.preco = preco
        self.vegetariano = vegetariano


class Pedido:
    """Pedido em aberto com itens, status e dados associados."""

    def __init__(self):
        self.itens = []
        self.status = "Aberto"
        self.garcom_chamado = False
        self.desconto = 0.0
        self.avaliacao = None
        self.reserva = None
