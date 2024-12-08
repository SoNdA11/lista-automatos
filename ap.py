class AutômatoPilha:
    """
    Representa um Autômato a Pilha (AP) para reconhecer cadeias em diferentes formatos.

    Um autômato a pilha é uma máquina de estados finitos que usa uma pilha para auxiliar no reconhecimento de linguagens que não podem ser reconhecidas por autômatos finitos simples. Este modelo de autômato pode ser utilizado para representar linguagens que possuem estrutura recursiva, como a linguagem das palavras balanceadas.

    A classe AutômatoPilha simula o comportamento de um autômato a pilha para reconhecer linguagens específicas, como:
    - Linguagem da forma a^n b c^n
    - Linguagem da forma a^n b^n

    A classe possui métodos para definir estados, símbolos de entrada, símbolos da pilha, estado inicial, estados finais e transições. A função de transição é implementada como um dicionário que mapeia uma tupla (estado_atual, simbolo_entrada, topo_da_pilha) para o próximo estado e a operação a ser realizada na pilha (empilhar ou desempilhar).

    A classe também inclui o método 'simular' que simula a execução do autômato sobre uma cadeia de entrada, verificando se a cadeia é aceita ou rejeitada pelo autômato, de acordo com as transições definidas.

    Atributos:
        estados (set): Conjunto de estados do autômato.
        alfabeto_entrada (set): Conjunto de símbolos de entrada (alfabeto do autômato).
        alfabeto_pilha (set): Conjunto de símbolos que podem ser manipulados na pilha.
        estado_inicial (str): Estado inicial do autômato.
        estados_finais (set): Conjunto de estados finais do autômato.
        transicoes (dict): Função de transição do autômato, representada por um dicionário.

    Métodos:
        simular(cadeia):
            Simula a execução do autômato sobre uma cadeia de entrada. Retorna True se a cadeia for aceita pelo autômato e False caso contrário.

    Exemplos de uso:
        - Linguagem a^n b c^n: Onde o número de 'a's é igual ao número de 'c's, e há pelo menos um 'b'.
        - Linguagem a^n b^n: Onde o número de 'a's é igual ao número de 'b's.

    Exemplo de testes:
        - Linguagem a^n b c^n:
            Cadeias aceitas:
                ['a', 'a', 'b', 'c', 'c']
                ['a', 'b', 'c']
            Cadeias rejeitadas:
                ['a', 'b', 'b', 'c']
                ['a', 'a', 'a', 'b', 'c', 'c', 'c']
                ['a', 'b', 'c', 'a']
        
        - Linguagem a^n b^n:
            Cadeias aceitas:
                ['a', 'a', 'b', 'b']
                ['a', 'b']
                ['a', 'a', 'a', 'b', 'b', 'b']
            Cadeias rejeitadas:
                ['a', 'b', 'b']
                ['a', 'b', 'a', 'b']
    """

    def __init__(self, estados, alfabeto_entrada, alfabeto_pilha, estado_inicial, estados_finais, transicoes):
        """
        Inicializa o autômato a pilha com os parâmetros fornecidos.

        Parâmetros:
            estados (set): Conjunto de estados do autômato.
            alfabeto_entrada (set): Conjunto de símbolos de entrada.
            alfabeto_pilha (set): Conjunto de símbolos da pilha.
            estado_inicial (str): Estado inicial do autômato.
            estados_finais (set): Conjunto de estados finais do autômato.
            transicoes (dict): Função de transição do autômato, representada por um dicionário.
        """
        self.estados = estados
        self.alfabeto_entrada = alfabeto_entrada
        self.alfabeto_pilha = alfabeto_pilha
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def simular(self, cadeia):
        """
        Simula a execução do autômato sobre uma cadeia de entrada e verifica se ela é aceita ou rejeitada.

        Parâmetros:
            cadeia (list): Lista de símbolos que representa a cadeia de entrada a ser processada.

        Retorna:
            bool: True se a cadeia for aceita pelo autômato, False caso contrário.
        """
        pilha = []  # Pilha começa vazia
        estado_atual = self.estado_inicial  # Começa no estado inicial

        # Processa cada símbolo da cadeia de entrada
        for simbolo in cadeia:
            # Verifica se existe uma transição válida para o símbolo atual e o topo da pilha
            if (estado_atual, simbolo, pilha[-1] if pilha else None) in self.transicoes:
                # Obtém o próximo estado e a operação de pilha (empilhar/desempilhar)
                novo_estado, operacao_pilha = self.transicoes[(estado_atual, simbolo, pilha[-1] if pilha else None)]
                estado_atual = novo_estado  # Atualiza o estado atual

                # Executa a operação de pilha (empilhar ou desempilhar)
                if operacao_pilha == 'empilhar':
                    pilha.append('X')  # Empilha um 'X' para cada 'a' lido
                elif operacao_pilha == 'desempilhar' and pilha:
                    pilha.pop()  # Desempilha um 'X' para cada 'c' lido
            else:
                return False  # Se não houver transição válida, rejeita a cadeia

        # Verifica se o autômato terminou em um estado final e a pilha está vazia
        return estado_atual in self.estados_finais and not pilha


# Linguagem a^n b c^n
estados_1 = {'q0', 'q1', 'q2', 'q3'}
alfabeto_entrada_1 = {'a', 'b', 'c'}
alfabeto_pilha_1 = {'X'}
estado_inicial_1 = 'q0'
estados_finais_1 = {'q3'}

# Função de transição para a^n b c^n
transicoes_1 = {
    ('q0', 'a', None): ('q1', 'empilhar'),
    ('q1', 'a', 'X'): ('q1', 'empilhar'),
    ('q1', 'b', 'X'): ('q2', None),
    ('q2', 'c', 'X'): ('q3', 'desempilhar'),
    ('q3', 'c', 'X'): ('q3', 'desempilhar'),
}

# Criando o autômato para a^n b c^n
ap_1 = AutômatoPilha(estados_1, alfabeto_entrada_1, alfabeto_pilha_1, estado_inicial_1, estados_finais_1, transicoes_1)


# Linguagem a^n b^n
estados_2 = {'q0', 'q1', 'q2'}
alfabeto_entrada_2 = {'a', 'b'}
alfabeto_pilha_2 = {'X'}
estado_inicial_2 = 'q0'
estados_finais_2 = {'q2'}

# Função de transição para a^n b^n
transicoes_2 = {
    ('q0', 'a', None): ('q1', 'empilhar'),
    ('q1', 'a', 'X'): ('q1', 'empilhar'),
    ('q1', 'b', 'X'): ('q2', 'desempilhar'),
    ('q2', 'b', 'X'): ('q2', 'desempilhar'),
}

# Criando o autômato para a^n b^n
ap_2 = AutômatoPilha(estados_2, alfabeto_entrada_2, alfabeto_pilha_2, estado_inicial_2, estados_finais_2, transicoes_2)

# Testando com algumas cadeias para a^n b c^n
cadeias_1 = [
    ['a', 'a', 'b', 'c', 'c'],  # Aceita: 2 'a's seguidos de 1 'b' e 2 'c's
    ['a', 'b', 'c'],  # Aceita: 1 'a' seguido de 1 'b' e 1 'c'
    ['a', 'b', 'b', 'c'],  # Rejeita: 1 'a', 2 'b's (excesso de 'b's)
    ['a', 'a', 'a', 'b', 'c', 'c', 'c'],  # Rejeita: 3 'a's e 3 'c's mas excessos de 'b's
    ['a', 'b', 'c', 'a']  # Rejeita: 'a' após o 'b' não é permitido
]

print("Testando para a^n b c^n:")
for cadeia in cadeias_1:
    resultado = ap_1.simular(cadeia)
    print(f"Cadeia {cadeia} é aceita: {resultado}")


# Testando com algumas cadeias para a^n b^n
cadeias_2 = [
    ['a', 'a', 'b', 'b'],  # Aceita: Dois 'a's seguidos de dois 'b's
    ['a', 'b'],  # Aceita: Um 'a' seguido de um 'b'
    ['a', 'b', 'b'],  # Rejeita: Um 'a' seguido de dois 'b's (número de b's não corresponde ao número de a's)
    ['a', 'a', 'a', 'b', 'b', 'b'],  # Aceita: Três 'a's seguidos de três 'b's
    ['a', 'b', 'a', 'b']  # Rejeita: Ordem incorreta de 'a's e 'b's
]

print("\nTestando para a^n b^n:")
for cadeia in cadeias_2:
    resultado = ap_2.simular(cadeia)
    print(f"Cadeia {cadeia} é aceita: {resultado}")
