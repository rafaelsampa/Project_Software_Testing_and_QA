

# Projeto Integrador – Etapa 1: Análise Crítica e Cobertura de Código
**Módulo Avaliado:** Gerenciamento de Pedidos (Sistema de Restaurante)

### 1. Introdução
Esta análise crítica avalia a qualidade do código e a robustez da suíte de testes de um módulo de gerenciamento de pedidos de restaurante (`app/pedido.py`). O módulo é responsável por concentrar a lógica de negócio central do estabelecimento, controlando o cardápio, a montagem do carrinho, a aplicação de descontos, o cálculo do subtotal e as transições de estado do pedido (Aberto, Aguardando Preparo, Cancelado, Pago, etc.).

O objetivo desta etapa foi validar a integridade funcional deste módulo através da implementação de testes unitários e da avaliação da cobertura de código, buscando identificar lacunas, riscos de falhas silenciosas e oportunidades de melhoria na arquitetura do software.

### 2. Metodologia e Cobertura
Os testes foram desenvolvidos utilizando o framework **Pytest**. A estratégia englobou a verificação das histórias de usuário (happy paths) e a inserção de casos limite (edge cases) para estressar a lógica de negócio. 

A cobertura de código foi mensurada utilizando a biblioteca `pytest-cov`. Após a implementação das validações de limites, o relatório indicou uma **cobertura de 100% (`Stmts: 45, Miss: 0`)** do arquivo `app/pedido.py`. Apesar da alta cobertura percentual atestar que todas as linhas de código foram executadas, a análise crítica aprofundada (descrita a seguir) revela que a cobertura lógica de estados ainda possui espaço para amadurecimento.

### 3. Análise Crítica: Lacunas e Riscos Identificados

Apesar de o sistema atender aos requisitos funcionais primários, a análise das rotinas de teste expôs as seguintes fragilidades estruturais e de comportamento:

**A. Falhas Silenciosas no Gerenciamento do Carrinho (Edge Cases)**
Durante a escrita dos testes, notou-se que métodos críticos como `adicionar_item()` e `remover_item()` sofrem de falhas silenciosas. Se o sistema requisitar a adição de um ID de prato inexistente (ex: `id=999`), a busca por list comprehension falha suavemente e retorna `None`, não alterando o estado do carrinho. Da mesma forma, tentar remover um item que não está no pedido encerra o loop sem lançar avisos.
* **Risco:** Em um ambiente de produção, problemas de dessincronização entre o front-end (tablet) e o back-end podem resultar em clientes acreditando que pediram um item que não foi registrado, gerando atrito no atendimento.

**B. Fragilidade na Máquina de Estados (Transições Inválidas)**
O ciclo de vida de um pedido é regido pela variável `self.status`. No entanto, a implementação atual carece de travas (guards) rigorosas. 
* **Risco:** Os testes comprovaram que é possível invocar o método `adicionar_item()` mesmo após o status ser definido como `"Fechamento Solicitado"` ou `"Pago"`. Além disso, o fluxo permite que um pedido passe de `"Aberto"` direto para `"Fechamento Solicitado"`, ignorando a etapa da cozinha. A ausência de validação do estado anterior antes de permitir uma transição pode gerar inconsistências financeiras graves.

**C. Acoplamento e Injeção de Dependência**
A classe `Pedido` inicializa a base de dados do cardápio (`self.cardapio`) diretamente em seu construtor. 
* **Risco:** Isso viola o Princípio da Responsabilidade Única (SRP). O código não está preparado para escalar, pois a adição de novos itens ou a alteração de preços exigiria a modificação direta da classe de negócio. 

### 4. Possíveis Melhorias Futuras
Com base nos riscos mapeados, propõe-se as seguintes refatorações para os próximos ciclos de desenvolvimento:
1. **Implementação de Exceptions Customizadas:** Substituir as falhas silenciosas por exceções de domínio (ex: `ItemNaoEncontradoError`, `TransicaoDeStatusInvalidaError`) para que as camadas superiores possam tratar o erro e avisar o cliente adequadamente.
2. **Desacoplamento do Repositório:** Injetar o cardápio via dependência (padrão Repository), permitindo que a classe `Pedido` consulte uma interface externa em vez de possuir os dados em memória.
3. **Validação Rigorosa de Dados:** Adicionar verificações em métodos estáticos, como impedir reservas para zero pessoas no método `reservar_mesa()`, espelhando a boa prática já implementada no método `dividir_conta()`.

### 5. Conclusão
O exercício de cobertura de código demonstrou que alcançar 100% de linhas testadas é apenas o primeiro passo para a garantia da qualidade (QA). A submissão do código aos cenários de erro evidenciou que a classe `Pedido` precisa de defesas lógicas mais estritas. Os testes criados não apenas comprovaram o funcionamento atual, mas serviram como documentação viva do comportamento do sistema, guiando os próximos passos de refatoração em direção a uma arquitetura mais limpa e resiliente.