import os
from datetime import datetime

def verificar_arquivo_mestre(caminho):
    if os.path.exists(caminho):
        print("Arquivo mestre encontrado.")
    else:
        print("Arquivo mestre não encontrado.")

def gerar_log_execucao():
    agora = datetime.now().strftime('%Y-%m%d-%Hh%Mmin')
    log_nome = f"{agora}_log_transf.txt"
    log_caminho = os.path.join(os.path.expanduser("~"), "Documents", "log", log_nome)
    os.makedirs(os.path.dirname(log_caminho), exist_ok=True)
    with open(log_caminho, "w") as f:
        f.write("Execução realizada com sucesso.")
    print(f"Log salvo em: {log_caminho}")

if __name__ == "__main__":
    arquivo_mestre = "Q:/financeira/custos/2025/Actual/Ajustes/Mov 413 Transferência Ordem Cliente.xlsx"
    verificar_arquivo_mestre(arquivo_mestre)
    gerar_log_execucao()
