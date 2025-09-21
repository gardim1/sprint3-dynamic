# Relatório – Consumo de Insumos (implementação do zero)
Este relatório foi gerado automaticamente pelo `app.py`.

## Resumo Executivo dos Dados Coletados
- Total de registros processados: **44** movimentações
- Maior saída individual identificada: **50** unidades de **Seringa 5ml** registrada em **2025-09-21**
- Insumo com prazo de validade mais crítico: **Seringa 5ml** (vencimento em **2025-11-16**)

## Metodologia de Controle Implementada

### 1. Sistema de Processamento Sequencial (Fila)
O controle cronológico das movimentações permite rastreamento temporal preciso dos consumos. A ordenação por data garante que possamos analisar padrões de uso ao longo do período de coleta, essencial para planejamento de reposição.

### 2. Consulta de Histórico Recente (Pilha)
Para auditoria e verificação rápida, mantemos acesso imediato aos últimos registros inseridos no sistema. Isso facilita a confirmação de lançamentos recentes e correção de eventuais inconsistências.

### 3. Localização de Insumos Específicos
- **Busca por similaridade**: Útil quando há incerteza sobre a nomenclatura exata do produto ou para localizar famílias de insumos relacionados
- **Busca exata otimizada**: Após organização alfabética dos dados, permite localização instantânea de produtos específicos, reduzindo tempo de consulta em grandes volumes de dados

### 4. Organização dos Dados por Critérios Clínicos
- **Por volume de consumo**: Identifica os insumos de maior rotatividade, auxiliando no dimensionamento de estoques
- **Por prazo de validade**: Prioriza produtos próximos ao vencimento, reduzindo perdas por expiração e otimizando o giro de estoque

Esta estrutura de controle permite maior precisão no acompanhamento do consumo diário, reduzindo as discrepâncias identificadas no processo manual anterior.

