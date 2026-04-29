from app.repository import buscar_produto_por_id

def adicionar_item(pedido, id_item, observacao=None):
    item = buscar_produto_por_id(id_item)
    if item:
        novo_item = {
            "id": item.id,
            "nome": item.nome,
            "preco": item.preco,
            "vegetariano": item.vegetariano
        }
        if observacao:
            novo_item["observacao"] = observacao
        pedido.itens.append(novo_item)


def remover_item(pedido, id_item):
    for item in pedido.itens:
        if item["id"] == id_item:
            pedido.itens.remove(item)
            break


def calcular_subtotal(pedido):
    total = sum(item["preco"] for item in pedido.itens)
    return total * (1 - pedido.desconto)


def chamar_garcom(pedido):
    pedido.garcom_chamado = True


def aplicar_cupom(pedido, codigo):
    if codigo == "DESCONTO10":
        pedido.desconto = 0.10


def enviar_para_cozinha(pedido):
    if pedido.itens:
        pedido.status = "Aguardando Preparo"


def cancelar_pedido(pedido):
    if pedido.status == "Aguardando Preparo":
        pedido.status = "Cancelado"


def solicitar_fechamento(pedido):
    if pedido.itens:
        pedido.status = "Fechamento Solicitado"


def dividir_conta(pedido, quantidade_pessoas):
    if quantidade_pessoas <= 0:
        raise ValueError("Número de pessoas deve ser maior que zero")
    return calcular_subtotal(pedido) / quantidade_pessoas


def pagar_conta(pedido, valor_entregue):
    valor_devido = calcular_subtotal(pedido)
    if pedido.status == "Fechamento Solicitado" and valor_entregue >= valor_devido:
        pedido.status = "Pago"
        return valor_entregue - valor_devido
    raise ValueError("Pagamento não pode ser processado")


def avaliar_atendimento(pedido, estrelas):
    if 1 <= estrelas <= 5:
        pedido.avaliacao = estrelas
    else:
        raise ValueError("Avaliação deve ser entre 1 e 5 estrelas")


def reservar_mesa(pedido, data_hora, quantidade_pessoas):
    pedido.reserva = {
        "data_hora": data_hora,
        "pessoas": quantidade_pessoas
    }