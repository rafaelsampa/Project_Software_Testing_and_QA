from app.models import Pedido
import app.services as s
import app.repository as r


def mostrar_cardapio(vegetariano):
    print("\n--- CARDÁPIO ---")
    if vegetariano:
        for p in r.listar_vegetarianos():
            print(f"{p.id} - {p.nome} | R${p.preco:.2f}")
    else:
        for p in r.listar_cardapio():
            print(f"{p.id} - {p.nome} | R${p.preco:.2f}")

def mostrar_itens(pedido):
    print("\n--- ITENS DO PEDIDO ---")
    if not pedido.itens:
        print("Pedido vazio")
        return

    for item in pedido.itens:
        obs = f" ({item.get('observacao')})" if "observacao" in item else ""
        print(f'{item["id"]} - {item["nome"]} R${item["preco"]:.2f}{obs}')


def menu():
    pedido = Pedido()

    while True:
        print("\n====== SISTEMA RESTAURANTE ======")
        print("1 - Ver cardápio")
        print("2 - Ver cardápio Vegetariano")
        print("3 - Adicionar item")
        print("4 - Remover item")
        print("5 - Ver itens do pedido")
        print("6 - Aplicar cupom")
        print("7 - Ver subtotal")
        print("8 - Enviar para cozinha")
        print("9 - Cancelar pedido")
        print("10 - Solicitar fechamento")
        print("11 - Dividir conta")
        print("12 - Pagar conta")
        print("13 - Avaliar atendimento")
        print("14 - Reservar mesa")
        print("0 - Sair")

        op = input("Escolha: ")

        try:
            if op == "1":
                mostrar_cardapio(0)

            elif op == "2":
                mostrar_cardapio(1)

            elif op == "3":
                mostrar_cardapio(0)
                id_item = int(input("ID do item: "))
                obs = input("Observação (opcional): ")
                s.adicionar_item(pedido, id_item, obs if obs else None)

            elif op == "4":
                mostrar_itens(pedido)
                id_item = int(input("ID do item para remover: "))
                s.remover_item(pedido, id_item)
                print("Item removido")

            elif op == "5":
                mostrar_itens(pedido)

            elif op == "6":
                codigo = input("Código do cupom: ")
                s.aplicar_cupom(pedido, codigo)

            elif op == "7":
                print(f"Subtotal: R${s.calcular_subtotal(pedido):.2f}")

            elif op == "8":
                s.enviar_para_cozinha(pedido)
                print("Pedido enviado!")

            elif op == "9":
                s.cancelar_pedido(pedido)
                print("Pedido cancelado (se permitido).")

            elif op == "10":
                s.solicitar_fechamento(pedido)
                print("Fechamento solicitado.")

            elif op == "11":
                pessoas = int(input("Quantidade de pessoas: "))
                valor = s.dividir_conta(pedido, pessoas)
                print(f"Cada pessoa paga: R${valor:.2f}")

            elif op == "12":
                valor = float(input("Valor entregue: "))
                troco = s.pagar_conta(pedido, valor)
                print(f"Troco: R${troco:.2f}")

            elif op == "13":
                estrelas = int(input("Avaliação (1-5): "))
                s.avaliar_atendimento(pedido, estrelas)
                print("Obrigado pela avaliação!")

            elif op == "14":
                data = input("Data e hora: ")
                pessoas = int(input("Quantidade de pessoas: "))
                s.reservar_mesa(pedido, data, pessoas)
                print("Reserva realizada!")

            elif op == "0":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)


if __name__ == "__main__":
    menu()