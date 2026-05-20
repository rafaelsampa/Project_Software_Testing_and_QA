"""Interface de linha de comando do sistema de pedidos do restaurante."""
from app.models import Pedido
from app import services
from app import repository


CABECALHO_MENU = """
====== SISTEMA RESTAURANTE ======
1 - Ver cardápio
2 - Ver cardápio Vegetariano
3 - Adicionar item
4 - Remover item
5 - Ver itens do pedido
6 - Aplicar cupom
7 - Ver subtotal
8 - Enviar para cozinha
9 - Cancelar pedido
10 - Solicitar fechamento
11 - Dividir conta
12 - Pagar conta
13 - Avaliar atendimento
14 - Reservar mesa
0 - Sair"""


def _formatar_produto(produto):
    return f"{produto.id} - {produto.nome} | R${produto.preco:.2f}"


def mostrar_cardapio(somente_vegetariano=False):
    """Exibe o cardápio completo ou apenas opções vegetarianas."""
    print("\n--- CARDÁPIO ---")
    produtos = (
        repository.listar_vegetarianos()
        if somente_vegetariano
        else repository.listar_cardapio()
    )
    for produto in produtos:
        print(_formatar_produto(produto))


def mostrar_itens(pedido):
    """Exibe os itens atualmente no pedido."""
    print("\n--- ITENS DO PEDIDO ---")
    if not pedido.itens:
        print("Pedido vazio")
        return
    for item in pedido.itens:
        obs = f" ({item.get('observacao')})" if "observacao" in item else ""
        print(f'{item["id"]} - {item["nome"]} R${item["preco"]:.2f}{obs}')


def _acao_ver_cardapio(_pedido):
    mostrar_cardapio(somente_vegetariano=False)


def _acao_ver_cardapio_vegetariano(_pedido):
    mostrar_cardapio(somente_vegetariano=True)


def _acao_adicionar_item(pedido):
    mostrar_cardapio(somente_vegetariano=False)
    id_item = int(input("ID do item: "))
    obs = input("Observação (opcional): ")
    services.adicionar_item(pedido, id_item, obs if obs else None)


def _acao_remover_item(pedido):
    mostrar_itens(pedido)
    id_item = int(input("ID do item para remover: "))
    services.remover_item(pedido, id_item)
    print("Item removido")


def _acao_ver_itens(pedido):
    mostrar_itens(pedido)


def _acao_aplicar_cupom(pedido):
    codigo = input("Código do cupom: ")
    services.aplicar_cupom(pedido, codigo)


def _acao_ver_subtotal(pedido):
    print(f"Subtotal: R${services.calcular_subtotal(pedido):.2f}")


def _acao_enviar_cozinha(pedido):
    services.enviar_para_cozinha(pedido)
    print("Pedido enviado!")


def _acao_cancelar_pedido(pedido):
    services.cancelar_pedido(pedido)
    print("Pedido cancelado (se permitido).")


def _acao_solicitar_fechamento(pedido):
    services.solicitar_fechamento(pedido)
    print("Fechamento solicitado.")


def _acao_dividir_conta(pedido):
    pessoas = int(input("Quantidade de pessoas: "))
    valor = services.dividir_conta(pedido, pessoas)
    print(f"Cada pessoa paga: R${valor:.2f}")


def _acao_pagar_conta(pedido):
    valor = float(input("Valor entregue: "))
    troco = services.pagar_conta(pedido, valor)
    print(f"Troco: R${troco:.2f}")


def _acao_avaliar_atendimento(pedido):
    estrelas = int(input("Avaliação (1-5): "))
    services.avaliar_atendimento(pedido, estrelas)
    print("Obrigado pela avaliação!")


def _acao_reservar_mesa(pedido):
    data = input("Data e hora: ")
    pessoas = int(input("Quantidade de pessoas: "))
    services.reservar_mesa(pedido, data, pessoas)
    print("Reserva realizada!")


ACOES = {
    "1": _acao_ver_cardapio,
    "2": _acao_ver_cardapio_vegetariano,
    "3": _acao_adicionar_item,
    "4": _acao_remover_item,
    "5": _acao_ver_itens,
    "6": _acao_aplicar_cupom,
    "7": _acao_ver_subtotal,
    "8": _acao_enviar_cozinha,
    "9": _acao_cancelar_pedido,
    "10": _acao_solicitar_fechamento,
    "11": _acao_dividir_conta,
    "12": _acao_pagar_conta,
    "13": _acao_avaliar_atendimento,
    "14": _acao_reservar_mesa,
}


def menu():
    """Loop principal: lê a opção do usuário e despacha para a ação correspondente."""
    pedido = Pedido()
    while True:
        print(CABECALHO_MENU)
        opcao = input("Escolha: ")

        if opcao == "0":
            print("Saindo...")
            break

        acao = ACOES.get(opcao)
        if acao is None:
            print("Opção inválida.")
            continue

        try:
            acao(pedido)
        except ValueError as erro:
            print("Erro:", erro)


if __name__ == "__main__":
    menu()
