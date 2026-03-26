


class Pedido:
    def __init__(self):
        self.itens = []
        self.status = "Aberto"
        self.garcom_chamado = False
        self.desconto = 0.0
        self.avaliacao = None
        self.reserva = None
        
        # Simulando um banco de dados de cardápio
        self.cardapio = [
            {"id": 1, "nome": "Hamburguer", "preco": 35.0, "vegetariano": False},
            {"id": 2, "nome": "Salada", "preco": 25.0, "vegetariano": True},
            {"id": 3, "nome": "Suco", "preco": 10.0, "vegetariano": True},
            {"id": 4, "nome": "Fritas", "preco": 15.0, "vegetariano": True}
        ]

    def listar_cardapio(self):
        return self.cardapio

    def listar_vegetarianos(self):
        return [item for item in self.cardapio if item["vegetariano"]]

    def adicionar_item(self, id_item, observacao=None):
        item_cardapio = next((i for i in self.cardapio if i["id"] == id_item), None)
        if item_cardapio:
            novo_item = item_cardapio.copy()
            if observacao:
                novo_item["observacao"] = observacao
            self.itens.append(novo_item)

    def remover_item(self, id_item):
        for item in self.itens:
            if item["id"] == id_item:
                self.itens.remove(item)
                break

    def calcular_subtotal(self):
        total = sum(item["preco"] for item in self.itens)
        return total * (1 - self.desconto)

    def chamar_garcom(self):
        self.garcom_chamado = True

    def aplicar_cupom(self, codigo):
        if codigo == "DESCONTO10":
            self.desconto = 0.10

    def enviar_para_cozinha(self):
        if self.itens:
            self.status = "Aguardando Preparo"

    def cancelar_pedido(self):
        if self.status == "Aguardando Preparo":
            self.status = "Cancelado"

    def solicitar_fechamento(self):
        if self.itens:
            self.status = "Fechamento Solicitado"

    def dividir_conta(self, quantidade_pessoas):
        if quantidade_pessoas <= 0:
            raise ValueError("Número de pessoas deve ser maior que zero")
        return self.calcular_subtotal() / quantidade_pessoas

    def pagar_conta(self, valor_entregue):
        valor_devido = self.calcular_subtotal()
        if self.status == "Fechamento Solicitado" and valor_entregue >= valor_devido:
            self.status = "Pago"
            troco = valor_entregue - valor_devido
            return troco
        raise ValueError("Pagamento não pode ser processado")

    def avaliar_atendimento(self, estrelas):
        if 1 <= estrelas <= 5:
            self.avaliacao = estrelas
        else:
            raise ValueError("Avaliação deve ser entre 1 e 5 estrelas")

    def reservar_mesa(self, data_hora, quantidade_pessoas):
        self.reserva = {"data_hora": data_hora, "pessoas": quantidade_pessoas}










        