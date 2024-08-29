class Avaliacao:
    def __init__(self, estabelecimento, qualidade_comida, atendimento, ambiente, musica, comentario=None):
        self.estabelecimento = estabelecimento
        self.qualidade_comida = qualidade_comida
        self.atendimento = atendimento
        self.ambiente = ambiente
        self.musica = musica
        self.comentario = comentario

    def __str__(self):
        return (f'Estabelecimento: {self.estabelecimento}\n'
                f'Qualidade da Comida: {self.qualidade_comida}\n'
                f'Atendimento: {self.atendimento}\n'
                f'Ambiente: {self.ambiente}\n'
                f'Música: {self.musica}\n'
                f'Comentário: {self.comentario if self.comentario else "Nenhum"}\n')
import os

avaliacoes = []
def coletar_nota(mensagem):
    while True:
        try:
            nota = int(input(mensagem))
            if 1 <= nota <= 5:
                return nota
            else:
                print("A nota deve estar entre 1 e 5. Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número entre 1 e 5.")
            
def coletar_avaliacao():
    estabelecimento = input("Nome do Estabelecimento: ")
    qualidade_comida = coletar_nota("Qualidade da Comida (1-5): ")
    atendimento = coletar_nota("Atendimento (1-5): ")
    ambiente = coletar_nota("Ambiente (1-5): ")
    musica = coletar_nota("Música (1-5): ")
    comentario = input("Comentário (opcional): ")
    avaliacao = Avaliacao(estabelecimento, qualidade_comida, atendimento, ambiente, musica, comentario)
    avaliacoes.append(avaliacao)
    print("\nAvaliação registrada com sucesso!\n")

def exibir_avaliacoes():
    if not avaliacoes:
        print("Nenhuma avaliação registrada ainda.\n")
    else:
        for avaliacao in avaliacoes:
            print(avaliacao)
            print("-" * 30)

def salvar_avaliacoes():
    with open("avaliacoes.txt", "w") as file:
        for avaliacao in avaliacoes:
            file.write(str(avaliacao))
            file.write("-" * 30 + "\n")
    print("Avaliações salvas em 'avaliacoes.txt'\n")

def carregar_avaliacoes():
    if os.path.exists("avaliacoes.txt"):
        with open("avaliacoes.txt", "r") as file:
            aval = file.read().strip().split('-' * 30)
            for avaliacao_texto in aval:
                if avaliacao_texto.strip():
                    linhas = avaliacao_texto.strip().split("\n")
                    dados = [linha.split(": ")[1] for linha in linhas if ": " in linha]
                    if len(dados) == 6:
                        avaliacoes.append(Avaliacao(dados[0], int(dados[1]), int(dados[2]), int(dados[3]), int(dados[4]), dados[5] if dados[5] != "Nenhum" else None))
        print("Avaliações carregadas com sucesso!\n")
    else:
        print("Nenhum arquivo de avaliações encontrado.\n")
def menu():
    carregar_avaliacoes()
    while True:
        print("1. Registrar uma nova avaliação")
        print("2. Exibir todas as avaliações")
        print("3. Salvar avaliações em arquivo")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            coletar_avaliacao()
        elif escolha == '2':
            exibir_avaliacoes()
        elif escolha == '3':
            salvar_avaliacoes()
        elif escolha == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
