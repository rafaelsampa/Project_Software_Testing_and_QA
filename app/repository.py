"""Acesso aos dados do cardápio (simulação de banco de dados em memória)."""
from app.models import Produto

cardapio = [
    Produto(1, "Hamburguer", 35.0, False),
    Produto(2, "Salada", 25.0, True),
    Produto(3, "Suco", 10.0, True),
    Produto(4, "Fritas", 15.0, True),
    Produto(5, "Pizza", 40.0, False)
]


def listar_cardapio():
    """Retorna todos os produtos disponíveis no cardápio."""
    return cardapio


def listar_vegetarianos():
    """Retorna apenas os produtos vegetarianos do cardápio."""
    return [item for item in cardapio if item.vegetariano]


def buscar_produto_por_id(id_item):
    """Busca um produto pelo ID. Retorna None se não encontrado."""
    return next((i for i in cardapio if i.id == id_item), None)
