class Pilha:
    def __init__(self, lista=None):
        self.pilha = ['-'] if lista is None else lista.copy()

    def copy(self):
        return Pilha(self.pilha.copy())     
    
    def empilha(self, n):
        if self.pilha[-1] == '-':
            self.pilha[-1] = n
        else:
            self.pilha.append(n)
            
    def desempilha(self):
        if len(self.pilha) == 1:
            if self.pilha[0] != '-':
                self.pilha[0] = '-'
        else:  
            del self.pilha[-1]

class Automato:
    def __init__(self):
        self.alfabeto = ['a', 'b']
        self.estados = ['q0', 'q1', 'q2']
        self.simbRegrasTrans = 'D'
        self.estadoInicial = 'q0' 
        self.estadosFinais = ['q2']
        self.alfabetoPilha = ['A', 'B']
        
        regras = ['q0, a, -, q0, B',
                  'q0, b, B, q1, -',
                  'q0, ?, ?, q2, -',
                  'q1, b, B, q1, -',
                  'q1, ?, ?, q2, -']
                 
        self.regrasTrans = [RegraTrans(i) for i in regras]
        
    def analisar(self, estado, palavra, pilha=None):
        p = Pilha() if pilha is None else pilha
         
        if estado in self.estadosFinais and palavra == '-':
            yield True
        
        flag = False
        
        for regra in self.regrasTrans:
            cond01 = regra.simboloLidoPilha == '?'
            cond02 = p.pilha[0] == '-'
            cond03 = regra.simboloLidoPalavra == '?'
            cond04 = palavra == '-'
            
            if cond01 and cond02 and cond03 and cond04:
                yield True
            
            cond11 = regra.estadoOrigem == estado
            cond12 = regra.simboloLidoPalavra == palavra[0]
            cond13 = regra.simboloLidoPalavra == '-'
            cond14 = regra.simboloLidoPilha == p.pilha[-1]
            cond15 = regra.simboloLidoPilha == '-'
                
            if cond11 and (cond12 or cond13) and (cond14 or cond15):
                flag = True
                
                novaPilha = Pilha(p.pilha)
                if regra.simboloLidoPilha != '-':
                    novaPilha.desempilha()
                if regra.simboloEscritoPilha != '-':
                    novaPilha.empilha(regra.simboloEscritoPilha)
                    
                novaPalavra = palavra
                if regra.simboloLidoPalavra != '-':
                    novaPalavra = palavra[1:] if len(palavra) > 1 else '-'

                yield from self.analisar(regra.estadoFinal, novaPalavra, novaPilha)
                                        
        if not flag: yield False
            
class RegraTrans:
    def __init__(self, string):
        string = string.replace(' ', '')
        regras = string.split(',')
        self.estadoOrigem = regras[0]
        self.simboloLidoPalavra = regras[1]
        self.simboloLidoPilha = regras[2]
        self.estadoFinal = regras[3]
        self.simboloEscritoPilha = regras[4]

a = Automato()
