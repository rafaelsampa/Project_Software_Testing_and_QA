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

**Lista Completa das Histórias de Usuário:**
1. Cliente visualiza o cardápio
2. Cliente filtra opções vegetarianas
3. Cliente adiciona item ao carrinho
4. Cliente remove item do carrinho
5. Cliente adiciona observação ao prato
6. Cliente visualiza o subtotal atualizado
7. Cliente chama o garçom
8. Cliente envia pedido para a cozinha
9. Cliente cancela pedido antes do preparo
10. Cliente aplica cupom de desconto
11. Cliente solicita fechamento da conta
12. Cliente divide o valor da conta
13. Cliente realiza o pagamento com troco
14. Cliente avalia o atendimento
15. Cliente reserva uma mesa
16. Cliente tenta dividir a conta por zero pessoas
17. Cliente tenta pagar um valor menor que o devido
18. Cliente tenta dar uma nota inválida


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
