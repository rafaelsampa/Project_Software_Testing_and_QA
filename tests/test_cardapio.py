import pytest
from app.pedido import Pedido

# História 1: Cliente visualiza o cardápio
def test_visualizar_cardapio():
    pedido = Pedido()
    cardapio = pedido.listar_cardapio()
    assert len(cardapio) == 4
    assert cardapio[0]["nome"] == "Hamburguer"

# História 2: Cliente filtra opções vegetarianas
def test_filtrar_menu_vegetariano():
    pedido = Pedido()
    opcoes_veg = pedido.listar_vegetarianos()
    assert len(opcoes_veg) == 3
    assert all(item["vegetariano"] for item in opcoes_veg)

# História 15: Cliente reserva uma mesa
def test_reservar_mesa():
    pedido = Pedido()
    pedido.reservar_mesa("2026-04-10 20:00", 4)
    assert pedido.reserva["pessoas"] == 4
    assert pedido.reserva["data_hora"] == "2026-04-10 20:00"