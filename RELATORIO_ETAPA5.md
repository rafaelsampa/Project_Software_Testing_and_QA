# Relatório — Etapa 5: Refatoração Orientada a Testes

**Grupo:** Gabriel Martins | Lucas Mourato | Rafael Sampaio

## 1. Problemas identificados na Etapa 4

A análise da Etapa 4 (pytest-cov + pylint) indicou um conjunto pontual de
problemas, com nota final do pylint em **7.90/10**:

- **`menu()` em `app/cli.py` — "God Function".** 18 ramos condicionais
  (limite 12) e 74 instruções (limite 50). Concentrava entrada, despacho,
  apresentação e tratamento de erros num único bloco.
- **`except Exception` genérico** em `cli.py:118` (W0718), mascarando o tipo
  real do erro.
- **Atributo/parâmetro `id`** em `Produto` (`models.py:2`) redefinindo a
  built-in `id()` do Python (W0622).
- **Ausência de docstrings** em todos os módulos, classes e funções
  (C0114, C0115, C0116) — apontada como principal causa da nota baixa.
- **Ausência de newline final** em `services.py`, `models.py`, `cli.py`
  e `repository.py` (C0304).
- **Acoplamento implícito** no `menu()` ao depender de constantes mágicas
  (`mostrar_cardapio(0)` / `mostrar_cardapio(1)`) em vez de um booleano
  nomeado.

## 2. Refatorações realizadas

Todas as alterações são estruturais; nenhuma muda o comportamento observável
do sistema (verificado pelos 42 testes existentes).

### 2.1. Quebra da `menu()` em handlers + tabela de despacho (`cli.py`)
Cada opção do menu virou uma função pequena de responsabilidade única
(`_acao_ver_cardapio`, `_acao_adicionar_item`, `_acao_pagar_conta`, ...).
A função `menu()` agora apenas exibe o cabeçalho, lê a entrada e despacha
através de um dicionário `ACOES`. Resultado: a `menu()` deixou de violar
os limites de `too-many-branches` e `too-many-statements`.

### 2.2. Estreitamento do tratamento de exceção (`cli.py`)
`except Exception` foi substituído por `except ValueError`, o único tipo
realmente levantado pelo `services` (e por `int()`/`float()` em entradas
inválidas). Comportamento preservado: o teste
`test_divisao_invalida_cli` e demais testes de erro continuam passando.

### 2.3. Renomeação do parâmetro `id` em `Produto` (`models.py`)
`id` foi renomeado para `produto_id` no `__init__`. O atributo `self.id`
foi mantido para não quebrar nenhum consumidor (todos os testes acessam
`.id`). Resolve W0622 sem efeito colateral.

### 2.4. Parâmetro booleano nomeado em `mostrar_cardapio` (`cli.py`)
A assinatura passou de `mostrar_cardapio(vegetariano: int)` para
`mostrar_cardapio(somente_vegetariano: bool = False)`. Elimina o número
mágico (`0`/`1`) das chamadas internas e melhora legibilidade.

### 2.5. Documentação e formatação
- Docstring de módulo em `cli.py`, `services.py`, `repository.py`,
  `models.py`.
- Docstring de classe em `Produto` e `Pedido`.
- Docstring curta em cada função pública.
- Newline final adicionado nos quatro arquivos.

### 2.6. Imports mais explícitos (`cli.py`)
Substituídos `import app.services as s` e `import app.repository as r`
por `from app import services` / `from app import repository`. As chamadas
ficam mais legíveis (`services.adicionar_item(...)` em vez de
`s.adicionar_item(...)`), reduzindo o ônus cognitivo para quem lê.

## 3. Justificativas técnicas

| Refatoração | Princípio aplicado |
|---|---|
| Handlers + dispatch dict no `menu()` | SRP, redução de complexidade ciclomática |
| `except ValueError` específico | Falhar com precisão; não esconder bugs reais |
| `produto_id` no lugar de `id` | Evitar shadowing de built-in (PEP 8) |
| Boolean nomeado no cardápio | Eliminar número mágico, melhorar legibilidade |
| Docstrings + newlines finais | PEP 257 / PEP 8 |
| Imports nominais | Reduzir aliases obscuros, aumentar legibilidade |

A escolha do **dicionário de despacho** (em vez de polimorfismo via classes
ou strategy pattern) foi proposital: o projeto é pequeno, o conjunto de
opções é fechado e estável, e introduzir hierarquias geraria mais código do
que o problema justifica. Refatoração proporcional ao tamanho do sistema.

## 4. Impacto das melhorias

### 4.1. Nota do pylint
- **Antes:** 7.90/10
- **Depois:** **9.87/10** (+1.97)
- Únicos avisos remanescentes: `R0903 (too-few-public-methods)` em
  `Produto` e `Pedido`, esperado para classes de dados e já reconhecido
  como aceitável no relatório da Etapa 4.

### 4.2. Cobertura de testes
- **Antes:** 99.38% (162 stmts, 1 miss)
- **Depois:** 99% (152 stmts, 1 miss) — o miss continua sendo apenas o
  `menu()` dentro de `if __name__ == "__main__":`, já excluído via
  `pytest.ini`. Nenhum trecho testável ficou de fora.

### 4.3. Testes
- **42/42 testes passando** após a refatoração (incluindo os cenários BDD
  e os testes de interface).
- Pipeline CI/CD (`.github/workflows/testeauto1.yaml`) inalterado e
  funcional — continua exigindo cobertura mínima de 90%.

### 4.4. Complexidade da `menu()`
- **Antes:** 18 ramos / 74 instruções em uma única função.
- **Depois:** `menu()` com ~15 instruções e 3 ramos (saída, opção inválida,
  execução); cada handler com 1–4 instruções e responsabilidade única.

### 4.5. Manutenibilidade
Adicionar uma nova opção ao menu agora requer apenas:
1. escrever uma função `_acao_xxx(pedido)`;
2. registrar a chave no dicionário `ACOES`;
3. ajustar o texto do `CABECALHO_MENU`.

Antes, exigia editar a cadeia de `if/elif` e arriscar quebrar a numeração.

## 5. Evidências

- **Relatório pylint pós-refatoração:** `python3 -m pylint app/` → 9.87/10.
- **Relatório pytest pós-refatoração:** `python3 -m pytest --cov=app
  --cov-report=term-missing` → 42 passed, 99% cobertura.
- **Diff dos arquivos modificados:** `cli.py`, `models.py`, `services.py`,
  `repository.py` (visível no histórico do git).
