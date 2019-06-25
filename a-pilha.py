class Pilha:
    def __init__(self, lista=None):
        self.pilha = ['-'] if lista is None else lista.copy()
        
    def empilha(self, n):
        if self.pilha[-1] == '-':
            self.pilha[-1] = n
        else: self.pilha.append(n)
            
    def desempilha(self):
        if len(self.pilha) == 1:
            if self.pilha[0] != '-':
                self.pilha[0] = '-'
        else: del self.pilha[-1]

class Automato:
    def __init__(self, componentes, producoes):
        self.alfabeto = componentes[0]
        self.estados = componentes[1]
        self.simbRegrasTrans = componentes[2]
        self.estadoInicial = componentes[3]
        self.estadosFinais = componentes[4]
        self.alfabetoPilha = componentes[5]
        regras = producoes
      
        self.regrasTrans = [RegraTrans(i) for i in regras]
        
    def analisar(self, estado, palavra, pilha=None, estados=None):
        p = Pilha() if pilha is None else pilha
        estados = [] if estados is None else estados.copy()
        
        # se o estado a ser analisado esta
        # entre os estados finais e a palavra
        # estiver vazia, a palavra eh aceita
        if estado in self.estadosFinais and palavra == '-':
            yield True, estados

        # a variavel indica se alguma regra de
        # transicao foi aceita, caso contrario a
        # palavra nao eh aceita pelo automato
        flag = False
        
        for regra in self.regrasTrans:
            # verificacao de pilha vazia
            cond01 = regra.simboloLidoPilha == '?'
            cond02 = p.pilha[0] == '-' 
            
            # verificacao de palavra vazia        
            cond03 = regra.simboloLidoPalavra == '?'
            cond04 = palavra == '-'
            
            # verifica se o estado de origem
            # da regra eh o mesmo estado atual
            cond05 = regra.estadoOrigem == estado
            
            # verifica se o simbolo lido da palavra
            # pela regra eh o mesmo simbolo da primeira
            # letra da palavra analisada ou eh vazio
            cond06 = regra.simboloLidoPalavra == palavra[0]
            cond07 = regra.simboloLidoPalavra == '-'
            
            # verifica se o simbolo lido da pilha
            # pela regra eh o mesmo simbolo que
            # esta no topo da pilha ou eh vazio
            cond08 = regra.simboloLidoPilha == p.pilha[-1]
            cond09 = regra.simboloLidoPilha == '-'
                
            if ((cond01 and cond02) and (cond03 and cond04)) or (cond05
                and (cond06 or cond07) and (cond08 or cond09)):
                flag = True
                
                # cria uma nova pilha para ser analisada
                # na recursao, empilhando ou desempilhando
                # conforme definido pela regra de transicao
                novaPilha = Pilha(p.pilha)
                if regra.simboloLidoPilha not in ['-', '?']:
                    novaPilha.desempilha()
                if regra.simboloEscritoPilha not in ['-', '?']:
                    novaPilha.empilha(regra.simboloEscritoPilha)
                
                # cria uma nova palavra para ser analisada
                # na recursao, consumindo uma letra da palavra
                # de acordo com o definido pela regra de transicao
                novaPalavra = palavra
                if regra.simboloLidoPalavra not in ['-', '?']:
                    novaPalavra = palavra[1:] if len(palavra) > 1 else '-'

                estados.append(regra)

                # caso seja produzido True, o programa para a execução
                # caso seja produzido False, significa que o último estado
                # não analisou a palavra com sucesso, portanto terá de ser deletado
                yield from self.analisar(regra.estadoFinal, novaPalavra, novaPilha, estados)
                del estados[-1]
                                        
        if not flag: yield False, estados
            
    def verifica(self, palavra):
        for res in self.analisar('q0', palavra):
            if res[0]:
                auxPilha = Pilha()
                for i, regra in enumerate(res[1]):
                    if regra.simboloLidoPilha not in ['-', '?']:
                        auxPilha.desempilha()
                    if regra.simboloEscritoPilha not in ['-', '?']:
                        auxPilha.empilha(regra.simboloEscritoPilha)
                        
                    print('REGRA {}:'.format(i+1))
                    regra.printAtributos()
                    print('PILHA: {}\n'.format(auxPilha.pilha))
                return True
            
        # caso o programa alcance esta parte do código,
        # isso significa que a palavra nao foi aceita
        # portanto será mostrado na tela a primeira
        # ocorrência de falha da palavra no automato

        novosValores = self.analisar('q0', palavra)
        res = next(novosValores)
        auxPilha2 = Pilha()
        for i, regra in enumerate(res[1]):
            if regra.simboloLidoPilha not in ['-', '?']:
                auxPilha2.desempilha()
            if regra.simboloEscritoPilha not in ['-', '?']:
                auxPilha2.empilha(regra.simboloEscritoPilha)
                
            print('REGRA {}:'.format(i+1))
            regra.printAtributos()
            print('PILHA: {}\n'.format(auxPilha2.pilha))
        return False
            
class RegraTrans:
    def __init__(self, string):
        string = string.replace(' ', '')
        regras = string.split(',')
        self.estadoOrigem = regras[0]
        self.simboloLidoPalavra = regras[1]
        self.simboloLidoPilha = regras[2]
        self.estadoFinal = regras[3]
        self.simboloEscritoPilha = regras[4]

    def printAtributos(self):
        print('Estado de origem:      {}'.format(self.estadoOrigem))
        print('Símbolo lido palavra:  {}'.format(self.simboloLidoPalavra))
        print('Símbolo lido pilha:    {}'.format(self.simboloLidoPilha))
        print('Estado final:          {}'.format(self.estadoFinal))
        print('Símbolo escrito pilha: {}'.format(self.simboloEscritoPilha))

# lê o arquivo que contém a gramática
# e as regras de produção do autômato
def lerArquivo(file):
    prod = []
    abrirArquivo = open(file, 'r')
    gramatica = abrirArquivo.readline()
    prodAutomato = abrirArquivo.readlines()
    abrirArquivo.close()

    for elem in range(0, len(prodAutomato)):
        if elem < len(prodAutomato) - 1:
            prod += [prodAutomato[elem][:-1]]
        else:
            prod += [prodAutomato[elem]]

    gramatica = gramatica[1:-2]
    gramatica = gramatica.replace('{', '')
    gramatica = gramatica.replace('}', '')
    gramatica = gramatica.split(', ')
    return gramatica, prod

# trata os elementos da gramática
# (como o conjunto de estados iniciais)
# para que sejam recebidos na classe autômato
def tratarS(gram):
    alf = []; est = []; est_finais = []; L1 = []; comp = []
    elem = 0
    while gram != []:
        gram[elem] = str(gram[elem])
        if len(gram[elem]) == 1 and (gram[elem].islower() or gram[elem].isnumeric()):
            alf += [gram[elem]]
        if len(gram[elem]) == 2:
            if gram[elem] not in est:
                est += [gram[elem]]
            else:
                est_finais += [gram[elem]]
        if gram[elem].isupper():
            L1 += [gram[elem]]
            if elem + 1 < len(gram):
                L1 += [gram[elem + 1]]
                gram.pop(elem + 1)
        gram.pop(elem)
    comp += [alf, est, L1[0], L1[1], est_finais, L1[2:len(L1)]]
    return comp

arquivoAutomato = input('Qual o nome do arquivo? ')
gramaticaAutomato, producoes = lerArquivo(arquivoAutomato)
componentes = tratarS(gramaticaAutomato)

a = Automato(componentes, producoes)
palavra = input('Qual a palavra a ser analisada? ')
print(a.alfabeto)
# verifica se alguma letra na palavra nao esta no
# conjunto de simbolos do alfabeto de entrada do automato
while not all([letra in a.alfabeto for letra in list(set(palavra))]):
    print('A palavra possui símbolos que não estão no alfabeto do autômato.')
    palavra = input('Insira a palavra para ser analisada pelo autômato: ')

print()
if a.verifica(palavra): print("A palavra '{}' foi aceita.".format(palavra))
else: print("A palavra '{}' foi recusada.".format(palavra))
