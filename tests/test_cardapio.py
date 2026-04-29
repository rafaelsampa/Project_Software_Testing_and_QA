import pytest
from app.models import Pedido
from app import repository as r
from app import services as s

# História 1: Cliente visualiza o cardápio
def test_visualizar_cardapio():
    cardapio = r.listar_cardapio()
    assert len(cardapio) == 4
    assert cardapio[0].nome == "Hamburguer"

# História 2: Cliente filtra opções vegetarianas
def test_filtrar_menu_vegetariano():
    opcoes_veg = r.listar_vegetarianos()
    assert len(opcoes_veg) == 3
    assert all(item.vegetariano for item in opcoes_veg)

# História 15: Cliente reserva uma mesa
def test_reservar_mesa():
    pedido = Pedido()
    s.reservar_mesa(pedido, "2026-04-10 20:00", 4)
    assert pedido.reserva["pessoas"] == 4
    assert pedido.reserva["data_hora"] == "2026-04-10 20:00"




# pytest
# pytest -v
# pytest --cov=app
# pytest --cov=app --cov-report=term-missing


