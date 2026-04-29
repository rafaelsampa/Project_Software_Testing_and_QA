

# Projeto Integrador 
## Etapa 1: Análise Crítica e Cobertura de Código
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

___________
<br>

# Projeto Integrador: Etapa 2 - Testes de Integração
**Módulo Avaliado:** Integração entre Interface (CLI), Serviços, Modelos e Repositório (Sistema de Restaurante)

### 1. Introdução
Esta etapa avalia o comportamento do sistema de gerenciamento de restaurante quando seus diferentes módulos interagem. O objetivo é garantir que as funcionalidades operem corretamente de forma integrada, validando a comunicação entre as camadas de interface, lógica de negócio e persistência de dados.

### 2. Fluxos Testados
Os testes de integração simulam o uso real do sistema de ponta a ponta. Os seguintes fluxos foram cobertos na suíte de testes:
* **Integração Front-to-Back:** Navegação pelo menu principal do CLI acionando os métodos corretos na camada de serviço.
* **Fluxo de Pedido Completo:** Adição de múltiplos itens válidos ao carrinho, consultando o repositório e atualizando o estado do modelo.
* **Tratamento de Exceções Integrado:** Tentativa de inserção de itens com IDs inexistentes, validando se o erro é corretamente propagado do serviço para a interface.
* **Cálculo de Totais:** Verificação do cálculo do subtotal e total com taxas, integrando as regras de negócio do modelo com os dados do repositório.

### 3. Identificação e Correção de Falhas (Problemas e Soluções)
Durante a implementação da integração, falhas mapeadas anteriormente foram corrigidas para garantir a robustez da comunicação entre os módulos:

**A. Correção de Falhas Silenciosas em IDs Inválidos**
* **Problema Encontrado:** Adicionar um item inexistente (`id=999`) retornava `None` silenciosamente na classe de pedido. Na integração com o CLI, isso deixava o usuário sem feedback.
* **Solução Aplicada:** A camada de serviço foi alterada para validar a existência do item ativamente. O serviço agora lança um erro (`ValueError`). O CLI captura essa exceção em um bloco `try/except` e exibe uma mensagem de erro para o usuário, impedindo falhas silenciosas.

**B. Resolução de Acoplamento (Refatoração para Repository)**
* **Problema Encontrado:** A classe modelo instanciava o banco de dados do cardápio internamente, misturando regra de negócio com acesso a dados. Isso impedia testes de integração limpos.
* **Solução Aplicada:** O sistema foi reestruturado em camadas. Criou-se o módulo de repositório para isolar os dados e o módulo de serviços para orquestrar as operações. Os modelos agora lidam apenas com estado.

### 4. Estratégia de Mocks
Para manter a fidelidade da validação de ponta a ponta, o uso de stubs e mocks foi restrito ao estritamente necessário. O recurso `monkeypatch` foi utilizado apenas para interceptar e simular o input do usuário no CLI. As interações internas entre Services, Repositories e Models utilizam instâncias reais do sistema.

### 5. Execução dos Testes e Evidências
A suíte pode ser executada garantindo a consistência dos resultados com o comando:
`pytest tests/ -v`

As evidências de execução (prints do terminal comprovando o sucesso dos testes e a comunicação entre as camadas) foram anexadas junto a esta entrega.
