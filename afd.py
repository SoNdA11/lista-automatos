# Classe que representa um Autômato Finito Determinístico (AFD).
class AFD:
    """
    A classe permite a definição de um AFD, a adição de transições entre estados e a verificação de aceitação de uma cadeia.
    """

    def __init__(self, num_estados, estado_inicial, estados_finais):
        """
        Construtor da classe AFD.
        
        Inicializa um AFD com a quantidade de estados, o estado inicial e os estados finais.
        
        Parâmetros:
        - num_estados: Número total de estados no AFD.
        - estado_inicial: O estado inicial do AFD (índice do estado).
        - estados_finais: Lista de estados finais (índices dos estados finais).
        """
        self.num_estados = num_estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        
        # Inicializa a matriz de transições com None para simular transições não definidas (-1)
        # O índice 0-255 é usado para representar os 256 possíveis valores ASCII de símbolos.
        self.transicoes = [[None] * 256 for _ in range(num_estados)]

    def adicionar_transicao(self, estado_origem, simbolo, estado_destino):
        """
        Adiciona uma transição entre estados no AFD.
        
        Este método armazena uma transição do estado de origem para o estado de destino, dado um símbolo.
        
        Parâmetros:
        - estado_origem: O estado de origem da transição.
        - simbolo: O símbolo que aciona a transição (caractere).
        - estado_destino: O estado de destino após a transição.
        """
        self.transicoes[estado_origem][ord(simbolo)] = estado_destino

    def estado_final(self, estado):
        """
        Verifica se um estado é final.
        
        Parâmetros:
        - estado: O estado a ser verificado.
        
        Retorna:
        - True se o estado é final, False caso contrário.
        """
        return estado in self.estados_finais

    def aceitar_cadeia(self, cadeia):
        """
        Verifica se uma cadeia é aceita pelo AFD.
        
        Este método processa a cadeia símbolo por símbolo e verifica se o autômato chega a um estado final.
        
        Parâmetros:
        - cadeia: A cadeia de símbolos a ser verificada.
        
        Retorna:
        - True se a cadeia for aceita (chegar a um estado final válido).
        - False caso contrário (se houver transição inválida ou não alcançar um estado final).
        """
        estado_atual = self.estado_inicial
        print(f"Estado inicial: q{estado_atual}")

        for simbolo in cadeia:
            # Processa cada símbolo da cadeia e segue a transição
            print(f"Processando símbolo '{simbolo}' no estado q{estado_atual} -> ", end="")
            estado_atual = self.transicoes[estado_atual][ord(simbolo)]
            
            if estado_atual is None:
                print("transição inválida.")
                return False  # Transição inválida, cadeia rejeitada
            
            print(f"Novo estado: q{estado_atual}")

        # Verifica se o estado final é um estado de aceitação
        resultado = self.estado_final(estado_atual)
        print(f"Estado final q{estado_atual} é {'um estado final' if resultado else 'não é um estado final'}")
        return resultado

# Função principal para inicializar o AFD e realizar testes
def main():
    """
    Função principal que inicializa o AFD e permite ao usuário testar uma cadeia.
    
    A função pede informações ao usuário sobre o número de estados, transições e a cadeia a ser verificada.
    """
    num_estados = int(input("Digite o número de estados no AFD: "))
    estado_inicial = int(input(f"Digite o estado inicial (0 a {num_estados - 1}): "))
    num_estados_finais = int(input("Digite o número de estados finais: "))
    estados_finais = [int(input(f"Estado final {i+1}: ")) for i in range(num_estados_finais)]

    # Inicializar o AFD com os dados fornecidos
    afd = AFD(num_estados, estado_inicial, estados_finais)

    # Definir transições
    num_transicoes = int(input("Digite o número de transições: "))
    for i in range(num_transicoes):
        estado_origem = int(input(f"Transição {i + 1} - Estado origem: "))
        simbolo = input(f"Transição {i + 1} - Símbolo: ")
        estado_destino = int(input(f"Transição {i + 1} - Estado destino: "))
        afd.adicionar_transicao(estado_origem, simbolo, estado_destino)

    # Cadeia de teste
    cadeia = input("Digite a cadeia para verificar: ")

    # Verificar se a cadeia é aceita ou rejeitada
    print(f"Cadeia '{cadeia}' é {'aceita' if afd.aceitar_cadeia(cadeia) else 'rejeitada'} pelo AFD.")

# Executar o programa principal
if __name__ == "__main__":
    main()