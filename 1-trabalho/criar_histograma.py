import sys

def ler_arquivo(nome_arquivo):
    dados = {}
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            palavra, frequencia = linha.strip().split()
            dados[palavra] = int(frequencia)
    return dados


def criar_histograma_textual(dados):
    max_freq = max(dados.values())
    intervalo = max_freq / 10

    for i in range(10):
        menor = i * intervalo
        maior = (i + 1) * intervalo
        bar = sum(1 for freq in dados.values() if menor <= freq < maior)
        print(f"{menor:.0f} - {maior:.0f} | {bar}")


arquivo = sys.argv[1]  


dados = ler_arquivo(arquivo)

criar_histograma_textual(dados)
