# Autômato com Pilha
Implementação de software para carregar e processar Autômato com Pilha

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

- `pilha`: Uma lista que representa uma pilha. Caso a pilha esteja vazia, possui o valor de `['-']`.

### Métodos:

- `empilha`: Adiciona um elemento no final da 
