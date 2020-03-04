# turmaA
This is the base repo for Software Engineering class nº4 (turma A).

Desenvolva um programa que simule o acesso de carros a um estacionamento pago. Deve implementar e testar individualmente cada uma das seguintes alíneas com funções, necessárias a uma correta resolução do problema. 

a.	Escreva uma função para ler o conteúdo de um ficheiro com o nome ep1.csv, que se encontra no seu ambiente de trabalho. Este contém informação sobre os veículos registados no estacionamento. Cada linha contém informação sobre um veículo (matrícula, marca e NIF) e os vários campos estão separados por um ‘;’ como pode ver no ficheiro ep1.csv. Exemplo de uma linha do ficheiro: 00-AA-00;Seat;801401501. Não existem matrículas repetidas, mas é possível várias matrículas estarem associadas a um mesmo NIF. Comece por decidir qual estrutura de dados que vai usar para representar esta informação (lista, dicionário, etc.). A função deverá depois devolver uma variável deste tipo. 

b.	Escreva uma função que imprima no terminal todos os veículos registados no parque. O argumento da função deverá ser uma variável com os veículos registados que resultou da alínea a). A impressão deverá ser ordenada por ordem crescente de NIF e, para NIFs iguais, deverá ser ordenada por ordem crescente da matrícula (ex: 00-AA-00 deverá aparecer antes de 00-ZZ-99). Tenha em consideração o formato de impressão de acordo com o exemplo de interação apresentado no final deste enunciado.

c.	Escreva uma função que imprima no terminal a informação referente a todas as matrículas associadas a cada NIF. O argumento da função deverá ser uma variável com os veículos registados que resultou da alínea a). Tenha em consideração o formato de impressão de acordo com o exemplo de interação apresentado no final deste enunciado.

d.	Escreva uma função que valide se uma string, passada como argumento, representa uma matrícula válida em Portugal. Considere apenas matrículas posteriores a 2005 compostas por letras no meio como no seguinte exemplo: 00-AA-00. A função deverá devolver um valor lógico Verdadeiro se a matrícula for válida e Falso, caso contrário.

e.	Escreva uma função que peça ao utilizador a informação referente à utilização de um parque. Deverá ser introduzida a matrícula e a duração do estacionamento em minutos. Deverá garantir a validação da informação introduzida, isto é, utilizando a função anterior deverá garantir a introdução de uma matrícula válida e o tempo decorrido deverá ser um valor inteiro positivo. Se o utilizador introduzir valores inválidos, deve apresentar uma mensagem de erro e voltar a pedir o valor, como pode ver no exemplo de interação apresentado no final deste enunciado. No final, a função deve devolver a informação introduzida através de uma estrutura de dados à sua escolha (ex. tuplo, lista, etc.). 

f.	Escreva uma função que permita escrever num ficheiro, com o nome “parque.csv”, todos os acessos ao parque, ordenados por ordem inversa da duração do estacionamento. Deverá escrever um acesso por linha, sendo os campos separados por um ‘;’. A função deverá receber como argumento uma variável contendo a informação sobre todos os acessos introduzidos.

g.	Escreva uma função que permita criar uma fatura para um certo NIF, pedido ao utilizador. A fatura deverá conter todos os acessos dos veículos registados para o NIF em questão, bem como o cálculo do total faturado. Considere que o preço por minuto é um cêntimo. A função deverá receber como argumento a informação relativa a todos os veículos registados e a todas as utilizações do parque. Tenha em consideração o formato de impressão de acordo com o exemplo de interação apresentado no final deste enunciado.
```python
Opcoes disponiveis:
0 - Terminar
1 - Ler ficheiro de clientes
2 - Imprimir clientes ordenados
3 - Mostrar matriculas por Cliente
4 - Adicionar acesso ao parque
5 - Gravar acessos ao parque
6 - Gerar fatura para um cliente
Opcao: 3
3
Não existem clientes!

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 5
5
Não existem entradas no Parque!

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 1
Nome do ficheiro: ep1.csv
Foram importados 6 registos.


Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 2
100100100 : ('50-UA-50', 'Honda')
100200300 : ('11-AB-11', 'Ford')
100200300 : ('99-XY-99', 'Lancia')
801401501 : ('00-AA-00', 'Seat')
901401101 : ('00-ZZ-00', 'Mercedes')
901401101 : ('10-CD-10', 'Nissan')

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 3
801401501 : ['00-AA-00']
901401101 : ['00-ZZ-00', '10-CD-10']
100200300 : ['11-AB-11', '99-XY-99']
100100100 : ['50-UA-50']

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 4
Matricula: 11-AB-11
Duracao: 30

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 4
Matricula: AA1748
Invalida! Matricula: 99-XY-99
Duracao: 120

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 4
Matricula: 50-UA-50
Duracao: -60
Invalida! Duracao: 60

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 5
Ficheiro gravado com sucesso!

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 6
NIF: 100200300
Fatura NIF: 100200300
Matricula  Marca             Duracao    Custo
11-AB-11   Ford                   30     0.30
99-XY-99   Lancia                120     1.20
Total:                                   1.50

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 6
NIF: 100100100
[('50-UA-50', 'Honda', '100100100', -60)]
Fatura NIF: 100100100
Matricula  Marca             Duracao    Custo
50-UA-50   Honda                  60     0.60
Total:                                   0.60

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao: 0
Obrigado por usar o nosso software!
```

