import pytest
from app.pedido import Pedido

# História 6: Cliente visualiza o subtotal atualizado
def test_calcular_subtotal():
    pedido = Pedido()
    pedido.adicionar_item(1)
    pedido.adicionar_item(3)
    assert pedido.calcular_subtotal() == 45.0

# História 7: Cliente chama o garçom
def test_chamar_garcom():
    pedido = Pedido()
    assert pedido.garcom_chamado is False
    pedido.chamar_garcom()
    assert pedido.garcom_chamado is True

# História 10: Cliente aplica cupom de desconto
def test_aplicar_cupom_desconto():
    pedido = Pedido()
    pedido.adicionar_item(1)
    pedido.aplicar_cupom("DESCONTO10")
    assert pedido.calcular_subtotal() == 31.5

# História 11: Cliente solicita fechamento da conta
def test_solicitar_fechamento():
    pedido = Pedido()
    pedido.adicionar_item(1)
    pedido.solicitar_fechamento()
    assert pedido.status == "Fechamento Solicitado"

# História 12: Cliente divide o valor da conta
def test_dividir_conta():
    pedido = Pedido()
    pedido.adicionar_item(1)
    pedido.adicionar_item(4)
    valor_por_pessoa = pedido.dividir_conta(2)
    assert valor_por_pessoa == 25.0

# História 13: Cliente realiza o pagamento com troco
def test_pagar_conta_com_troco():
    pedido = Pedido()
    pedido.adicionar_item(2)
    pedido.solicitar_fechamento()
    troco = pedido.pagar_conta(30.0)
    assert pedido.status == "Pago"
    assert troco == 5.0

# História 14: Cliente avalia o atendimento
def test_avaliar_atendimento():
    pedido = Pedido()
    pedido.avaliar_atendimento(5)
    assert pedido.avaliacao == 5

# História 16: Cliente tenta dividir a conta por zero pessoas
def test_dividir_conta_erro():
    pedido = Pedido()
    with pytest.raises(ValueError, match="Número de pessoas deve ser maior que zero"):
        pedido.dividir_conta(0)

# História 17: Cliente tenta pagar um valor menor que o devido
def test_pagar_conta_erro():
    pedido = Pedido()
    pedido.adicionar_item(1)
    pedido.solicitar_fechamento()
    with pytest.raises(ValueError, match="Pagamento não pode ser processado"):
        pedido.pagar_conta(20.0)

# História 18: Cliente tenta dar uma nota inválida
def test_avaliar_atendimento_erro():
    pedido = Pedido()
    with pytest.raises(ValueError, match="Avaliação deve ser entre 1 e 5 estrelas"):
        pedido.avaliar_atendimento(6)