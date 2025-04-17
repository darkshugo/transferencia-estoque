# Automação: Transferência Estoque

Este projeto realiza a automação do processo de movimentação 413 no SAP, referente à transferência de ordens de cliente. Ele lê um arquivo mestre e busca e-mails do dia vigente com informações complementares.

## Funcionalidades
- Verifica se o arquivo mestre existe
- Gera log da execução com nome no padrão `YYYY-MMDD-HHhMMmin_log_transf.txt`
- Busca e-mails apenas do dia atual para otimizar performance

## Estrutura
- `scripts/`: Código-fonte da automação
- `log/`: Arquivos de log por execução
- `data/`: Arquivos de entrada ou exemplo

## Requisitos
- Python 3.9+
- Bibliotecas: `pandas`, `openpyxl`, `pywin32`, `datetime`

## Como executar
1. Coloque o arquivo mestre na pasta `data/`
2. Execute o script `transferencia_estoque.py`
3. O log será salvo automaticamente em `Documents\log`

---

Feito com carinho por Renato - Controladoria & Automação Inteligente
