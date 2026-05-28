"""Regras de negócio do sistema de pedidos."""
from app.repository import buscar_produto_por_id


def adicionar_item(pedido, id_item, observacao=None):
    """Adiciona um item do cardápio ao pedido, opcionalmente com observação."""
    item = buscar_produto_por_id(id_item)
    if item:
        novo_item = {
            "id": item.id,
            "nome": item.nome,
            "preco": item.preco,
            "vegetariano": item.vegetariano,
        }
        if observacao:
            novo_item["observacao"] = observacao
        pedido.itens.append(novo_item)


def remover_item(pedido, id_item):
    """Remove a primeira ocorrência do item com o ID informado."""
    for item in pedido.itens:
        if item["id"] == id_item:
            pedido.itens.remove(item)
            break


def calcular_subtotal(pedido):
    """Calcula o subtotal aplicando o desconto vigente do pedido."""
    total = sum(item["preco"] for item in pedido.itens)
    return total * (1 - pedido.desconto)


def chamar_garcom(pedido):
    """Marca o pedido como tendo solicitado atendimento."""
    pedido.garcom_chamado = True


def aplicar_cupom(pedido, codigo):
    """Aplica um cupom de desconto reconhecido ao pedido."""
    if codigo == "DESCONTO10":
        pedido.desconto = 0.10


def enviar_para_cozinha(pedido):
    """Envia o pedido para preparo se houver itens."""
    if pedido.itens:
        pedido.status = "Aguardando Preparo"


def cancelar_pedido(pedido):
    """Cancela o pedido se ele ainda estiver aguardando preparo."""
    if pedido.status == "Aguardando Preparo":
        pedido.status = "Cancelado"


def solicitar_fechamento(pedido):
    """Solicita o fechamento da conta se houver itens."""
    if pedido.itens:
        pedido.status = "Fechamento Solicitado"


def dividir_conta(pedido, quantidade_pessoas):
    """Divide o subtotal entre N pessoas. Levanta ValueError se N <= 0."""
    if quantidade_pessoas <= 0:
        raise ValueError("Número de pessoas deve ser maior que zero")
    return calcular_subtotal(pedido) / quantidade_pessoas


def pagar_conta(pedido, valor_entregue):
    """Processa o pagamento e retorna o troco. Levanta ValueError se inválido."""
    valor_devido = calcular_subtotal(pedido)
    if pedido.status == "Fechamento Solicitado" and valor_entregue >= valor_devido:
        pedido.status = "Pago"
        return valor_entregue - valor_devido
    raise ValueError("Pagamento não pode ser processado")


def avaliar_atendimento(pedido, estrelas):
    """Registra a avaliação do atendimento entre 1 e 5 estrelas."""
    if 1 <= estrelas <= 5:
        pedido.avaliacao = estrelas
    else:
        raise ValueError("Avaliação deve ser entre 1 e 5 estrelas")


def reservar_mesa(pedido, data_hora, quantidade_pessoas):
    """Registra uma reserva de mesa associada ao pedido."""
    pedido.reserva = {
        "data_hora": data_hora,
        "pessoas": quantidade_pessoas,
    }
