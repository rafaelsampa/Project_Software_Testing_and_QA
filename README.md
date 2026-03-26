# Project_Software_Testing_and_QA
By: Lucas Mourato & Rafael Sampaio


# Estratégia de Testes -> Restaurante

## Objetivo

Garantir que o sistema do restaurante seja bom e funcional para os clientes, permitindo que eles possam reservar mesas com antecedência, visualizar o cardápio e realizar pedidos. Além disso, garantir que os funcionários consigam receber e entregar os pedidos corretamente para as respectivas mesas.

------------------------------------------------------------------------

## Tipos de Teste

### Teste de Requisitos

Verificar se cada requisito funcional e não funcional está implementado
corretamente.

### Histórias de Usuário

Validar as funcionalidades principais do sistema:

<!-- -   Consultar o cardápio.
-   Editar o cardápio.
-   Registrar pedido.
-   Reservar mesa. -->
1. Cliente visualiza os itens disponíveis no cardápio.

2. Cliente adiciona um item ao carrinho do pedido.

3. Cliente remove um item previamente adicionado ao carrinho.

4. Cliente adiciona uma observação de preparo a um item (exemplo: sem cebola).

5. Cliente visualiza o subtotal da conta atualizado ao adicionar novos itens.

6. Cliente aciona o botão de chamar o garçom para a mesa.

7. Cliente solicita o fechamento da conta.

8. Cliente aplica um código de cupom de desconto no subtotal.

9. Cliente divide o valor total da conta por um número específico de pessoas.

10. Cliente reserva uma mesa para um horário futuro no sistema.

11. Cliente realiza o pagamento simulado da refeição.

12. Cliente adiciona uma avaliação em estrelas ao final do atendimento.

13. Cliente cancela um pedido que ainda está com status "Aguardando Preparo".

14. Cliente filtra o cardápio para exibir apenas opções vegetarianas.

### Teste de Regras de Negócio

Garantir que regras importantes sejam respeitadas:

-   Garantir a ordem de preparo dos pedidos.
-   Garantir a identificação correta do dono do pedido (mesa ou endereço de entrega).
-   Garantir a validação da forma de pagamento.
-   Garantir que uma mesa já reservada ou ocupada não possa ser utilizada por outros clientes.


### Teste de Aceitação

Validar se o sistema atende às necessidades dos usuários definidos nas
personas.

------------------------------------------------------------------------

## Critérios de Qualidade

-   Integridade dos dados
-   Consistência dos requisitos
-   Confiabilidade do sistema
-   Usabilidade da interface

### Limiar de cobertura

```
pytest --cov=app --cov-report=term-missing --cov-fail-under=90
````

------------------------------------------------------------------------

## Ferramentas

Os testes podem ser realizados utilizando:

-   Testes manuais
-   Checklist de validação
-   Revisão de requisitos
