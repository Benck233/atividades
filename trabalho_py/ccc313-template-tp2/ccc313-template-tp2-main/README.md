# Trabalho Prático 02 — Estruturas de Dados

**Disciplina:** Algoritmos e Programação  
**Conteúdo:** Aulas 09 a 12 (listas, dicionários, tuplas, conjuntos e estruturas combinadas)  
**Total de pontos:** 100

---

## Como começar

1. Aceite o trabalho pelo link disponibilizado no AVA.
2. Clone o repositório criado para você:
   ```bash
   git clone <url-do-seu-repositorio>
   cd <nome-do-repositorio>
   ```
3. Implemente cada exercício no arquivo `.py` correspondente.
4. Faça `push` ao concluir — a correção automática é acionada a cada envio.

---

## Exercícios

| Arquivo | Exercício | Estrutura principal | Nível | Pontos |
|---------|-----------|---------------------|-------|--------|
| `ex01_estatisticas_notas.py` | Estatísticas de Notas | Lista | Básico | 8 |
| `ex02_compressao_rle.py` | Compressão RLE | Lista | Intermediário | 8 |
| `ex03_janela_maxima.py` | Máximo em Janela Deslizante | Lista | Intermediário | 8 |
| `ex04_frequencia_palavras.py` | Top-K Palavras Frequentes | Dicionário | Intermediário | 8 |
| `ex05_placar_campeonato.py` | Tabela do Campeonato | Dicionário | Intermediário | 8 |
| `ex06_indice_invertido.py` | Índice Invertido | Dicionário de listas | Intermediário | 8 |
| `ex07_anagramas.py` | Agrupador de Anagramas | Tuplas como chaves | Intermediário | 8 |
| `ex08_cobertura_habilidades.py` | Cobertura de Habilidades | Conjuntos | Intermediário | 8 |
| `ex09_pontos_proximos.py` | Par de Pontos Mais Próximos | Tuplas + laços | Avançado | 9 |
| `ex10_biblioteca.py` | Sistema de Biblioteca | Dict + sentinela | Avançado | 9 |
| `ex11_caminho_bfs.py` | Caminho Mínimo — BFS | Dict de conjuntos | Avançado | 9 |
| `ex12_cache_lru.py` | Cache LRU Simplificado | Dict + lista | Desafio | 9 |

O enunciado detalhado de cada exercício está no início do arquivo `.py` correspondente (docstring).

---

## Regras de entrega

- **Não renomeie os arquivos.** A correção automática usa o nome exato de cada arquivo.
- **Use `input()` sem argumento de prompt.** O autograder injeta as entradas diretamente; textos de prompt podem quebrar testes com comparação exata.
- **Saída exata.** Siga o formato de saída especificado no enunciado de cada exercício. Use `:.1f` e `:.2f` onde indicado.
- **Apenas módulos da biblioteca padrão.** Os módulos `math` e `collections` estão liberados quando necessários. Nenhum pacote externo (pip) é permitido.
- **Para ordenação, use `sorted()` conforme indicado nos enunciados.** Não implemente algoritmos de ordenação manualmente neste TP.
- **Cada arquivo deve ser executável de forma independente.** Não crie dependências entre os arquivos.

---

## Estrutura do repositório

```
.
├── ex01_estatisticas_notas.py
├── ex02_compressao_rle.py
├── ex03_janela_maxima.py
├── ex04_frequencia_palavras.py
├── ex05_placar_campeonato.py
├── ex06_indice_invertido.py
├── ex07_anagramas.py
├── ex08_cobertura_habilidades.py
├── ex09_pontos_proximos.py
├── ex10_biblioteca.py
├── ex11_caminho_bfs.py
└── ex12_cache_lru.py
```

---

## Como verificar a correção

Após cada `push`, acesse a aba **Actions** do seu repositório no GitHub para ver o resultado de cada teste. O painel de notas fica disponível no GitHub Classroom pelo link fornecido pelo professor.

Cada exercício tem **2 testes automáticos**:
- Um **caso comum** que verifica a funcionalidade principal.
- Um **caso de borda** que verifica situações especiais (N par, lista vazia, grafo desconexo, etc.).

### Smoke tests públicos (para alunos)

Este repositório inclui testes de fumaça visíveis para validação rápida local:

```bash
python smoke_tests/run_smoke_tests.py
```

Para rodar apenas um exercício:

```bash
python smoke_tests/run_smoke_tests.py --exercise ex04
```

Os smoke tests são apenas uma checagem inicial. A nota oficial vem dos testes
privados do GitHub Classroom.

---

## Dicas gerais

- Leia o enunciado completo de cada exercício antes de começar — ele inclui exemplos de entrada/saída e dicas sobre a abordagem.
- Teste seu código localmente antes de fazer `push`:
  ```bash
  printf "5\n7.0 4.5 9.0 6.5 8.0\n" | python ex01_estatisticas_notas.py
  ```
- Se um teste falhar, compare cuidadosamente sua saída com a saída esperada — incluindo espaços, maiúsculas/minúsculas e quebras de linha.

---

## Dúvidas

Consulte o material das Aulas 09 a 12 no site da disciplina ou poste no fórum do AVA.

---

## Opção bônus — Conecta 4 (facultativa)

Como alternativa aos exercícios **ex09, ex10 e ex11** (27 pontos), você pode
implementar o jogo **Conecta 4** completo.

| Detalhe | Valor |
|---------|-------|
| Pontuação | 27 pontos (substitui ex09 + ex10 + ex11) |
| ex12 | Continua obrigatório |
| Pontos de bônus (IA) | Avaliação manual pelo professor |

### Estrutura do bônus

```
bonus_conecta4/
├── interface.py   ← fornecido pelo professor, NÃO MODIFIQUE
├── main.py        ← fornecido pelo professor, NÃO MODIFIQUE
├── game.py        ← VOCÊ implementa aqui
└── requirements.txt
```

### O que você deve implementar (`game.py`)

| Função | O que faz |
|--------|-----------|
| `criar_tabuleiro()` | Retorna tabuleiro 6×7 vazio |
| `eh_valido(board, col)` | Verifica se a coluna está disponível |
| `fazer_jogada(board, col, peca)` | Insere a peça com gravidade |
| `verificar_vitoria(board, peca)` | Detecta 4 em linha (todas as direções) |
| `tabuleiro_cheio(board)` | Detecta empate |
| `obter_jogada_cpu(board, peca)` | **[BÔNUS]** IA que joga sozinha |

### Executar localmente

1. Instale as dependências do bônus (inclui a biblioteca `rich`):

```bash
pip install -r bonus_conecta4/requirements.txt
```

2. Execute o jogo:

```bash
python bonus_conecta4/main.py
# → informe os nomes dos jogadores: ex. "Alice Bob" ou "Alice CPU"
```

Se preferir executar de dentro da pasta do bônus:

```bash
cd bonus_conecta4
pip install -r requirements.txt
python main.py
```

### Testar o autograder

```bash
echo "J1 J2\n0\n1\n0\n1\n0\n1\n0" | python bonus_conecta4/main.py
# saída deve conter: J1 venceu!
```

### Regra de substituição

Se você submeter o bônus **e** os exercícios ex09/ex10/ex11, o autograder
soma todos os pontos. O professor aplicará a regra de substituição ao calcular
a nota final (prevalece o caminho que resultar em mais pontos, limitado a 100).

