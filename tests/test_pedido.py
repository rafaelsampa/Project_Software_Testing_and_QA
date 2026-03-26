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

# História 3: Cliente adiciona item ao carrinho
def test_adicionar_item_carrinho():
    pedido = Pedido()
    pedido.adicionar_item(1) # Adiciona Hamburguer
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

# História 6: Cliente visualiza o subtotal atualizado
def test_calcular_subtotal():
    pedido = Pedido()
    pedido.adicionar_item(1) # 35.0
    pedido.adicionar_item(3) # 10.0
    assert pedido.calcular_subtotal() == 45.0

# História 7: Cliente chama o garçom
def test_chamar_garcom():
    pedido = Pedido()
    assert pedido.garcom_chamado is False
    pedido.chamar_garcom()
    assert pedido.garcom_chamado is True

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

# História 10: Cliente aplica cupom de desconto
def test_aplicar_cupom_desconto():
    pedido = Pedido()
    pedido.adicionar_item(1) # 35.0
    pedido.aplicar_cupom("DESCONTO10")
    assert pedido.calcular_subtotal() == 31.5 # 10% de desconto

# História 11: Cliente solicita fechamento da conta
def test_solicitar_fechamento():
    pedido = Pedido()
    pedido.adicionar_item(1)
    pedido.solicitar_fechamento()
    assert pedido.status == "Fechamento Solicitado"

# História 12: Cliente divide o valor da conta
def test_dividir_conta():
    pedido = Pedido()
    pedido.adicionar_item(1) # 35.0
    pedido.adicionar_item(4) # 15.0, total 50.0
    valor_por_pessoa = pedido.dividir_conta(2)
    assert valor_por_pessoa == 25.0

# História 13: Cliente realiza o pagamento com troco
def test_pagar_conta_com_troco():
    pedido = Pedido()
    pedido.adicionar_item(2) # 25.0
    pedido.solicitar_fechamento()
    troco = pedido.pagar_conta(30.0)
    assert pedido.status == "Pago"
    assert troco == 5.0

# História 14: Cliente avalia o atendimento
def test_avaliar_atendimento():
    pedido = Pedido()
    pedido.avaliar_atendimento(5)
    assert pedido.avaliacao == 5

# História 15: Cliente reserva uma mesa
def test_reservar_mesa():
    pedido = Pedido()
    pedido.reservar_mesa("2026-04-10 20:00", 4)
    assert pedido.reserva["pessoas"] == 4
    assert pedido.reserva["data_hora"] == "2026-04-10 20:00"

# Com o objetivo de falhar, vamos criar testes para as seguintes histórias extras: =============================== //

# História 16: Cliente tenta dividir a conta por zero pessoas
def test_dividir_conta_erro():
    pedido = Pedido()
    with pytest.raises(ValueError, match="Número de pessoas deve ser maior que zero"):
        pedido.dividir_conta(0)

# História 17: Cliente tenta pagar um valor menor que o devido ou sem fechar a conta
def test_pagar_conta_erro():
    pedido = Pedido()
    pedido.adicionar_item(1) # Custa 35.0
    pedido.solicitar_fechamento()
    with pytest.raises(ValueError, match="Pagamento não pode ser processado"):
        pedido.pagar_conta(20.0) # Valor insuficiente

# História 18: Cliente tenta dar uma nota inválida
def test_avaliar_atendimento_erro():
    pedido = Pedido()
    with pytest.raises(ValueError, match="Avaliação deve ser entre 1 e 5 estrelas"):
        pedido.avaliar_atendimento(6)