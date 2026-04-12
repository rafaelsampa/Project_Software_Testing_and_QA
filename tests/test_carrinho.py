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

# História: Cliente tenta adicionar um item que não existe no cardápio
def test_adicionar_item_inexistente():
    pedido = Pedido()
    pedido.adicionar_item(999) # ID inexistente
    assert len(pedido.itens) == 0 # O carrinho deve continuar vazio

# História: Cliente tenta remover um item de um carrinho vazio ou item não listado !!! Edge case !!!
def test_remover_item_inexistente_ou_carrinho_vazio():
    pedido = Pedido()
    pedido.remover_item(1) # Não deve quebrar o código
    assert len(pedido.itens) == 0
    
    pedido.adicionar_item(2)
    pedido.remover_item(999) # Tenta remover item que não está no carrinho
    assert len(pedido.itens) == 1 # O item 2 deve continuar lá


