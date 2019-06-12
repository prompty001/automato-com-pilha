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
        
    def analisar(self, estado, palavra, pilha=None):
        p = Pilha() if pilha is None else pilha
        
        # se o estado a ser analisado esta
        # entre os estados finais e a palavra
        # estiver vazia, a palavra eh aceita
        if estado in self.estadosFinais and palavra == '-':
            yield True

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
                
                yield from self.analisar(regra.estadoFinal, novaPalavra, novaPilha)
                                        
        if not flag: yield False
            
    def verifica(self, palavra):
        for res in self.analisar('q0', palavra):
            if res: return True
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

def main():
    import itertools as it
    
    a = Automato()
    for i in range(2, 7, 2):
        for item in it.product('ab', repeat=i):
            palavra = ''.join(item)
            if a.verifica(palavra): print("A palavra {} foi aceita.".format(palavra))
            else: print("A palavra {} foi recusada.".format(palavra))

if __name__ == '__main__': main()
