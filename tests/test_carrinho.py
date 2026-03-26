import pytest
from app.pedido import Pedido

# História 3: Cliente adiciona item ao carrinho
def test_adicionar_item_carrinho():
    pedido = Pedido()
    pedido.adicionar_item(1)
    assert len(pedido.itens) == 1
    assert pedido.itens[0]["nome"] == "Hamburguer"

# História 4: Cliente remove item do carrinho
def test_remover_item_carrinho():
    pedido = Pedido()
    pedido.adicionar_item(1)
    pedido.adicionar_item(3)
    pedido.remover_item(1)
    assert len(pedido.itens) == 1
    assert pedido.itens[0]["nome"] == "Suco"

# História 5: Cliente adiciona observação ao prato
def test_adicionar_item_com_observacao():
    pedido = Pedido()
    pedido.adicionar_item(1, observacao="Sem cebola")
    assert pedido.itens[0]["observacao"] == "Sem cebola"

# História 8: Cliente envia pedido para a cozinha
def test_enviar_pedido_cozinha():
    pedido = Pedido()
    pedido.adicionar_item(1)
    pedido.enviar_para_cozinha()
    assert pedido.status == "Aguardando Preparo"

# História 9: Cliente cancela pedido antes do preparo
def test_cancelar_pedido_aguardando_preparo():
    pedido = Pedido()
    pedido.adicionar_item(1)
    pedido.enviar_para_cozinha()
    pedido.cancelar_pedido()
    assert pedido.status == "Cancelado"