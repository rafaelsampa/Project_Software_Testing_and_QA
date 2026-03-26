from pytest_bdd import scenarios, given, when, then
from app.pedido import Pedido

# Diz ao pytest onde ler o texto
scenarios('features/pedido.feature')

@given("um pedido em aberto", target_fixture="pedido")
def pedido_aberto():
    return Pedido()

@when("o cliente adiciona o item de ID 1")
def adicionar_item(pedido):
    pedido.adicionar_item(1)

@then("o carrinho deve conter 1 item")
def verificar_carrinho(pedido):
    assert len(pedido.itens) == 1