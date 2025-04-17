---
title: Automação Transferência Estoque
---

# 💼 Automação Transferência Estoque - SAP

Bem-vindo à documentação da automação desenvolvida por **Renato Comelli** para o processo de movimentação **413 no SAP**, referente à **transferência de ordens de cliente**.

Este projeto foi criado para **agilizar tarefas manuais**, reduzir erros operacionais e gerar logs automáticos com base no dia da execução.

---

## ⚙️ Funcionalidades principais

- ✔️ Verificação automática do arquivo mestre
- ✔️ Geração de log com nome padrão `YYYY-MMDD-HHhMMmin_log_transf.txt`
- ✔️ Foco em e-mails recebidos apenas no dia vigente
- ✔️ Estrutura leve e adaptável para outros processos SAP

---

## 🧱 Estrutura do Projeto

```plaintext
/scripts/      → Código Python da automação  
/log/          → Logs de execução gerados automaticamente  
/data/         → Arquivos de entrada ou templates de SAP  
