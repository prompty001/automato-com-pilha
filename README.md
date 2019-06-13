# Autômato com Pilha

Trabalho da disciplina de Linguagens Formais, Autômatos e Computabilidade que realiza a simulação de um autômato com pilha.

## Atividade proposta

A-Pilha (Autômato com Pilha) são um tipo de autômato específico para trabalhar com linguagens livres do contexto. Esses autômatos são conhecidos por utilizar uma estrutura auxiliar do tipo pilha para leitura e escrita de dados.

Nesse trabalho, será implementado um software em qualquer linguagem de programação para carregar um A-Pilha a partir de um arquivo e em seguida verificar se determinada palavra é aceita ou recusada pelo autômato.

O arquivo que descreverá o A-Pilha terá a seguinte forma geral descrita abaixo. Na primeira linha serão apresentados os componentes do autômato, a exemplo do que foi apresentado em aula, conforme abaixo:

    (∑︀ , Q, 𝛿, q0, F, V)

Os componentes serão apresentados como conjuntos. Um exemplo da primeira linha do arquivo seria:

    ({a, b}, {q0, q1, q2, q3}, D, q0, {q3}, {A, B})

A partir da segunda linha, estarão listadas as regras de transição segundo o esquema:

    estado_origem, símbolo_lido_palavra, símbolo_lido_pilha, estado_final, símbolo_escrito_pilha

Por exemplo:

    q0, a, A, q1, A
    q1, a, A, qf, -
    q0, b, B, q2, B
    q1, b, B, q2, -
    q2, ?, ?, q3, -

Cabe ressaltar que os elementos do trabalho seguirão estritamente o padrão apresentado acima: estados com “q” seguido de números (podem ser dezenas), símbolos com letras, os conjuntos definidos por { e }, o conjunto de regras de produção com “D”, e a separação dos componentes via vírgula e espaço.

Os símbolos exclusivos da pilha serão letras maiúsculas, enquanto símbolos vazios serão representados por “-”. O teste da pilha vazia será indicado pela transição que utiliza “?” para leitura da palavra e pilha, conforme no exemplo anterior.

Após carregar o arquivo com o A-Pilha, o autômato receberá uma palavra e deverá apresentar a ordem de estados processados e o estado da pilha em cada um deles, além de indicar se a palavra foi ou não aceita.

## Código-fonte

O arquivo foi desenvolvido na linguagem Python.

### Classe `Pilha`

Representação da estrutura auxiliar do tipo pilha utilizada pelo autômato.

#### Argumentos:

- `lista`: Primeiro parâmetro. Caso não seja passado, possui valor de `None`.

#### Atributos:

- `pilha`: Uma lista que representa uma pilha. Uma pilha vazia é representada por `['-']`. O topo da pilha representa o último elemento da lista.

#### Métodos:

- `empilha`: Adiciona um elemento `n` passado como parâmetro no topo da pilha.
- `desempilha`: Remove o elemento que está no topo da pilha.

------

### Classe `RegraTrans`

Representa uma regra de transição do autômato.

#### Argumentos:

- `string`: Primeiro parâmetro. A partir desse parâmetro serão interpretados os atributos da classe.

#### Atributos:

- `estadoOrigem`: Representa o estado de origem.
- `simboloLidoPalavra`: Representa o símbolo lido pela palavra inserida como entrada.
- `simboloLidoPilha`: Representa o símbolo a ser lido pela pilha.
- `estadoFinal`: Representa o estado final, ou seja, o estado para que o autômato vai caso a palavra seja aceita.
- `simboloEscritoPilha`: Representa o símbolo a ser escrito na pilha.

A execução da regra de transição leva o autômato a consumir o prefixo `simboloLidoPalavra` da entrada, consumir o prefixo `simboloLidoPilha` da pilha, produzir `simboloEscritoPilha` no topo da pilha e passar do estado `estadoOrigem` para o estado `estadoFinal`.

#### Métodos:

- `printAtributos`: Mostra na tela os atributos da regra de transição.

------

### Classe `Automato`

Representa um autômato com pilha.

#### Argumentos:

TBA

#### Atributos:

- `alfabeto`: Representa um conjunto finito de símbolos, denominado alfabeto de entrada.
- `estados`: Representa um conjunto finito de estados.
- `simbRegrasTrans`: Representa o símbolo da regra de transição.
- `estadoInicial`: Representa o estado inicial.
- `estadosFinais`: Representa o conjunto de estados finais.
- `alfabetoPilha`: Representa um conjunto finito de símbolos, denominado alfabeto da pilha.
- `regrasTrans`: Representa uma lista de objetos da classe `RegraTrans`.

#### Métodos:

- `analisar`: Analisa uma palavra e pode gerar `True` ou `False` de acordo com os estados percorridos. Possui como parâmetros `estado`, que representa o estado atual em que o autômato se encontra, `palavra`, que representa a palavra atual que está sendo analisada pelo autômato, `pilha`, que representa a condição atual da pilha e `estados`, que representa todos os estados que o autômato já percorreu até o momento atual.
- `verificar`: Analisa a saída do método `analisar` e retorna `True` caso algum valor gerado pelo método seja `True` (significando que a palavra foi aceita) e retorna `False` caso contrário (significando que a palavra não foi aceita). Também é mostrado ao usuário quais foram os estados percorridos pelo autômato até que a palavra fosse aceita.

