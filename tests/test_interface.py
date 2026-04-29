import builtins
from app.cli import menu

def test_menu_existe():
    assert callable(menu)

def test_ver_cardapio(monkeypatch, capsys):
    inputs = iter([
        "1",  # ver cardápio
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "CARDÁPIO" in output
    assert "Hamburguer" in output

def test_ver_cardapio_vegetariano(monkeypatch, capsys):
    inputs = iter([
        "2",  # ver cardápio vegetariano
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "CARDÁPIO" in output
    assert "Hamburguer" not in output
    assert "Salada" in output

def test_adicionar_e_ver_itens(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "3",  # adicionar item
        "2",  # ID do item (Salada)
        "",  # sem observação
        "5",  # ver itens do pedido
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "ITENS DO PEDIDO" in output
    assert "Hamburguer" in output
    assert "Salada" in output

def test_remover_item(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "4",  # remover item
        "1",  # ID do item para remover
        "5",  # ver itens do pedido
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "ITENS DO PEDIDO" in output
    parte = output.split("Item removido")
    depois = parte[1] 
    assert "Hamburguer" not in depois

def test_ver_itens_pedido_vazio(monkeypatch, capsys):
    inputs = iter([
        "5",  # ver itens do pedido
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Pedido vazio" in output

def test_cupom_aplicado(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "6",  # aplicar cupom
        "DESCONTO10",  # código do cupom
        "7",  # ver subtotal
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Subtotal" in output
    assert "R$31.50" in output

def test_ver_subtotal(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "7",  # ver subtotal
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Subtotal" in output
    assert "R$10.00" in output

def test_ver_subtotal_sem_itens(monkeypatch, capsys):
    inputs = iter([
        "7",  # ver subtotal
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Subtotal" in output
    assert "R$0.00" in output

def test_enviar_para_cozinha_com_itens(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "8",  # enviar para cozinha
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Pedido enviado!" in output

def test_cancelar_pedido(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "9",  # cancelar pedido
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Pedido cancelado" in output


def solicitar_fechamento(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "10", # solicitar fechamento
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Fechamento solicitado." in output

def test_dividir_conta(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "11", # dividir conta
        "2",  # dividir entre 2 pessoas
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Cada pessoa paga: R$17.50" in output

def test_divisao_invalida_cli(monkeypatch, capsys):
    inputs = iter([
        "11",  # dividir conta
        "0",   # inválido
        "0"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu()

    out = capsys.readouterr().out
    assert "Erro" in out

def test_pagar_conta(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "10", # solicitar fechamento
        "12", # pagar conta
        "35", # valor entregue
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Troco: R$0.00" in output

def test_pagar_conta_com_troco(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "10", # solicitar fechamento  
        "12", # pagar conta
        "40", # valor entregue
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Troco: R$5.00" in output

def test_pagar_conta_valor_inferior(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "12", # pagar conta
        "30", # valor entregue inferior ao total
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Pagamento não pode ser processado" in output

def test_avaliar_atendimento(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "13", # avaliar atendimento
        "5",  # avaliação de 5 estrelas
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Obrigado pela avaliação" in output

def test_avaliar_atendimento_entrada_invalida(monkeypatch, capsys):
    inputs = iter([
        "3",  # adicionar item
        "1",  # ID do item (Hamburguer)
        "",   # sem observação
        "13", # avaliar atendimento
        "6",  # avaliação inválida
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Erro" in output

def test_reservar_mesa(monkeypatch, capsys):
    inputs = iter([
        "14", # reservar mesa
        "2026-04-10 20:00",  # data e hora
        "4",  # quantidade de pessoas
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Reserva realizada" in output

def test_sair(monkeypatch, capsys):
    inputs = iter([
        "0"   # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Saindo" in output

def test_opcao_invalida(monkeypatch, capsys):
    inputs = iter([
        "99",  # opção inválida
        "0"    # sair
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    menu()

    output = capsys.readouterr().out

    assert "Opção inválida" in output
