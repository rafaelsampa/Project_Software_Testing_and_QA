Feature: Gerenciamento de Pedidos no Tablet
  Como um cliente do restaurante
  Eu quero usar o tablet
  Para fazer e gerenciar meus pedidos

  Scenario: Cliente adiciona item ao carrinho
    Given um pedido em aberto
    When o cliente adiciona o item de ID 1
    Then o carrinho deve conter 1 item