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
    def __init__(self):
        self.alfabeto = ['a', 'b']
        self.estados = ['q0', 'q1', 'q2']
        self.simbRegrasTrans = 'D'
        self.estadoInicial = 'q0' 
        self.estadosFinais = ['q2']
        self.alfabetoPilha = ['A', 'B']
        
        # regras de transicao que aceitam um
        # palindromo com um numero par de digitos
        regras = ['q0, a, -, q0, A',
                  'q0, b, -, q0, B',
                  'q0, -, -, q1, -',
                  'q1, a, A, q1, -',
                  'q1, b, B, q1, -',
                  'q1, ?, ?, q2, -']
                 
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
                                        
        if not flag: yield False, []
            
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

# gera uma palavra aleatoria usando os caracteres 
# 'dig' com um comprimento de 'num' caracteres
def geraPalavra(dig, num):
    import itertools, random
    palavras = [''.join(item) for item in itertools.product(dig, repeat=num)]
    return random.choice(palavras)

def main():
    a = Automato()
    palavra = 'abba'
    #palavra = geraPalavra('ab', 4)
    
    if a.verifica(palavra): print("A palavra '{}' foi aceita.".format(palavra))
    else: print("A palavra '{}' foi recusada.".format(palavra))

if __name__ == '__main__': main()
