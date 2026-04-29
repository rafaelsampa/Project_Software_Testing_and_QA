import pytest
from app.models import Pedido
from app import repository as r
from app import services as s

# História 6: Cliente visualiza o subtotal atualizado
def test_calcular_subtotal():
    pedido = Pedido()
    s.adicionar_item(pedido, 1)
    s.adicionar_item(pedido, 3)
    assert s.calcular_subtotal(pedido) == 45.0

# História 7: Cliente chama o garçom
def test_chamar_garcom():
    pedido = Pedido()
    assert pedido.garcom_chamado is False
    s.chamar_garcom(pedido)
    assert pedido.garcom_chamado is True

# História 10: Cliente aplica cupom de desconto
def test_aplicar_cupom_desconto():
    pedido = Pedido()
    s.adicionar_item(pedido, 1)
    s.adicionar_item(pedido, 3)
    s.aplicar_cupom(pedido, "DESCONTO10")
    assert s.calcular_subtotal(pedido) == 40.5

# História 11: Cliente solicita fechamento da conta
def test_solicitar_fechamento():
    pedido = Pedido()
    s.adicionar_item(pedido, 1)
    s.solicitar_fechamento(pedido)
    assert pedido.status == "Fechamento Solicitado"

# História 12: Cliente divide o valor da conta
def test_dividir_conta():
    pedido = Pedido()
    s.adicionar_item(pedido, 1)
    s.adicionar_item(pedido, 4)
    valor_por_pessoa = s.dividir_conta(pedido, 2)
    assert valor_por_pessoa == 25.0

# História 13: Cliente realiza o pagamento com troco
def test_pagar_conta_com_troco():
    pedido = Pedido()
    s.adicionar_item(pedido, 2)
    s.solicitar_fechamento(pedido)
    troco = s.pagar_conta(pedido, 30.0)
    assert pedido.status == "Pago"
    assert troco == 5.0

# História 14: Cliente avalia o atendimento
def test_avaliar_atendimento():
    pedido = Pedido()
    s.avaliar_atendimento(pedido, 5)
    assert pedido.avaliacao == 5

# História 16: Cliente tenta dividir a conta por zero pessoas
def test_dividir_conta_erro():
    pedido = Pedido()
    with pytest.raises(ValueError, match="Número de pessoas deve ser maior que zero"):
        s.dividir_conta(pedido, 0)

# História 17: Cliente tenta pagar um valor menor que o devido
def test_pagar_conta_erro():
    pedido = Pedido()
    s.adicionar_item(pedido, 1)
    s.solicitar_fechamento(pedido)
    with pytest.raises(ValueError, match="Pagamento não pode ser processado"):
        s.pagar_conta(pedido, 20.0)

# História 18: Cliente tenta dar uma nota inválida
def test_avaliar_atendimento_erro():
    pedido = Pedido()
    with pytest.raises(ValueError, match="Avaliação deve ser entre 1 e 5 estrelas"):
        s.avaliar_atendimento(pedido, 6)