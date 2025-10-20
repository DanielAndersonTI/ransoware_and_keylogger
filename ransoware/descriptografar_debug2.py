# descriptografar_debug2.py
import os
from cryptography.fernet import Fernet, InvalidToken

def carregar_chave():
    chave_path = "chave.key"
    if not os.path.exists(chave_path):
        raise FileNotFoundError(f"Arquivo de chave não encontrado: {chave_path}")
    return open(chave_path, "rb").read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_descriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

def encontrar_arquivos(diretorio):
    arquivos_encontrados = []
    if not os.path.exists(diretorio):
        print(f"⛔ Diretório não existe: {diretorio}")
        return arquivos_encontrados

    for raiz, _, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            if nome_arquivo in ("descriptografar.py", "descriptografar_debug.py", "descriptografar_debug2.py", "chave.key"):
                continue
            caminho_completo = os.path.join(raiz, nome_arquivo)
            arquivos_encontrados.append(caminho_completo)
    return arquivos_encontrados

def info_arquivo(arquivo):
    with open(arquivo, "rb") as f:
        dados = f.read(128)
    return dados

def main():
    print("Iniciando descriptografia — debug v2")
    print("Diretório de trabalho:", os.getcwd())

    try:
        chave = carregar_chave()
        print("✅ chave carregada: chave.key")
        print(" -> len(chave):", len(chave))
        print(" -> repr(chave)[:60]:", repr(chave)[:60])
    except Exception as e:
        print(f"❌ Erro ao carregar chave: {repr(e)}")
        return

    dir_alvo = "arquivos_teste"
    arquivos = encontrar_arquivos(dir_alvo)
    print(f"Arquivos encontrados em '{dir_alvo}': {len(arquivos)}")
    for a in arquivos:
        print(" ->", a)

    if not arquivos:
        print("Nenhum arquivo para descriptografar.")
        return

    for arquivo in arquivos:
        try:
            head = info_arquivo(arquivo)
            print(f"\nTentando descriptografar: {arquivo}")
            print(" -> tamanho (bytes):", os.path.getsize(arquivo))
            print(" -> primeiros bytes (repr, até 128):", repr(head)[:200])

            descriptografar_arquivo(arquivo, chave)
            print(f"✅ Arquivo restaurado: {arquivo}")

        except InvalidToken as e:
            print(f"❌ InvalidToken ao restaurar {arquivo}: {repr(e)}")
            # mostra mais info para diagnosticar
            head = info_arquivo(arquivo)
            print(" -> primeiros bytes do arquivo (repr):", repr(head)[:200])
            print(" -> Isso normalmente indica: chave errada / arquivo não foi criptografado com Fernet / arquivo corrompido.")
        except Exception as e:
            print(f"❌ Erro inesperado ao restaurar {arquivo}: tipo={type(e)} repr={repr(e)}")
            head = info_arquivo(arquivo)
            print(" -> primeiros bytes do arquivo (repr):", repr(head)[:200])

if __name__ == "__main__":
    main()
