from app.models import Produto

# Simulando banco de dados (cardápio)
cardapio = [
    Produto(1, "Hamburguer", 35.0, False),
    Produto(2, "Salada", 25.0, True),
    Produto(3, "Suco", 10.0, True),
    Produto(4, "Fritas", 15.0, True)
]


def listar_cardapio():
    return cardapio


def listar_vegetarianos():
    return [item for item in cardapio if item.vegetariano]


def buscar_produto_por_id(id_item):
    return next((i for i in cardapio if i.id == id_item), None)