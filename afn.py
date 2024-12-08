from collections import defaultdict

class AFN:
    def __init__(self, num_estados, estado_inicial, estados_finais):
        """
        Inicializa um Autômato Finito Não Determinístico (AFN).

        Parâmetros:
        - num_estados (int): Número total de estados do AFN.
        - estado_inicial (int): Estado inicial do AFN.
        - estados_finais (set): Conjunto de estados finais do AFN.
        """
        # Atributos que armazenam o número de estados, o estado inicial e os estados finais
        self.num_estados = num_estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        
        # Estrutura de dados para armazenar as transições: 
        # defaultdict de dicionários de conjuntos de estados
        self.transicoes = defaultdict(lambda: defaultdict(set))

    def adicionar_transicao(self, estado_origem, simbolo, estado_destino):
        """
        Adiciona uma transição ao autômato.

        Parâmetros:
        - estado_origem (int): O estado de onde a transição se origina.
        - simbolo (str): O símbolo que aciona a transição.
        - estado_destino (int): O estado de destino da transição.
        """
        # A transição é armazenada, considerando que o símbolo pode ser "lambda" ou um símbolo normal
        self.transicoes[estado_origem][simbolo].add(estado_destino)

    def _fecho_lambda(self, estados):
        """
        Calcula o fecho-lambda de um conjunto de estados.

        O fecho-lambda é o conjunto de estados que podem ser alcançados a partir de 
        um conjunto de estados, considerando apenas transições "lambda" (sem consumir símbolos).

        Parâmetros:
        - estados (set): Conjunto de estados a partir dos quais calcular o fecho-lambda.

        Retorna:
        - set: Conjunto de estados alcançados através de transições "lambda".
        """
        # Inicializa o fecho com os estados passados
        fecho = set(estados)
        pilha = list(estados)  # Pilha para armazenar os estados a serem processados

        while pilha:
            estado = pilha.pop()
            # Verifica se há transições "lambda" a partir do estado atual
            for prox_estado in self.transicoes[estado].get('lambda', set()):
                if prox_estado not in fecho:
                    fecho.add(prox_estado)  # Adiciona o novo estado ao fecho
                    pilha.append(prox_estado)  # Adiciona o estado à pilha para continuar a busca
        return fecho

    def aceitar_cadeia(self, cadeia):
        """
        Verifica se a cadeia fornecida é aceita pelo AFN.

        O método simula a execução do autômato para a cadeia dada, considerando 
        as transições de cada símbolo da cadeia e o fecho-lambda de cada conjunto de estados.

        Parâmetros:
        - cadeia (str): A cadeia de símbolos a ser verificada.

        Retorna:
        - bool: True se a cadeia é aceita pelo AFN, False caso contrário.
        """
        # Inicializa os estados atuais com o fecho-lambda do estado inicial
        estados_atuais = self._fecho_lambda({self.estado_inicial})

        # Processa cada símbolo da cadeia
        for simbolo in cadeia:
            novos_estados = set()
            # Para cada estado atual, verifica as transições possíveis para o símbolo
            for estado in estados_atuais:
                novos_estados.update(self.transicoes[estado].get(simbolo, set()))
            # Calcula o fecho-lambda dos novos estados
            estados_atuais = self._fecho_lambda(novos_estados)

        # Verifica se algum estado final é alcançado
        return bool(estados_atuais & self.estados_finais)


# Definição dos parâmetros do AFN
num_estados = int(input("Digite o número de estados no AFN: "))
estado_inicial = int(input(f"Digite o estado inicial (0 a {num_estados - 1}): "))
num_estados_finais = int(input("Digite o número de estados finais: "))
estados_finais = set(int(input(f"Estado final {i + 1}: ")) for i in range(num_estados_finais))

# Inicializar o AFN
afn = AFN(num_estados, estado_inicial, estados_finais)

# Definir transições
num_transicoes = int(input("Digite o número de transições: "))
for i in range(num_transicoes):
    estado_origem = int(input(f"Transição {i + 1} - Estado origem: "))
    simbolo = input(f"Transição {i + 1} - Símbolo (deixe em branco para lambda): ")
    if simbolo == "":
        simbolo = "lambda"  # Representação de transição vazia
    estado_destino = int(input(f"Transição {i + 1} - Estado destino: "))
    afn.adicionar_transicao(estado_origem, simbolo, estado_destino)

# Cadeia de teste
cadeia = input("Digite a cadeia para verificar: ")

# Verificar se a cadeia é aceita
print(f"Cadeia '{cadeia}' é {'aceita' if afn.aceitar_cadeia(cadeia) else 'rejeitada'} pelo AFN.")