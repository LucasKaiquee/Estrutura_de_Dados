from PilhaSequencialNumPy import *
#from PilhaSimplesmenteEncadeada import PilhaException, Pilha

p1 = Pilha()

print(p1)

if p1.estaVazia():
    print('p1 esta vazia.')

print('Tamanho da pilha:', len(p1))

for i in range(1,11):
    p1.empilha(i*10)

print('Tamanho da pilha:', len(p1))

print(p1)

try:
    conteudo = p1.elemento(3)
    print(f'Elemento(3): {conteudo}')
    posicao = p1.busca(50)
    print(f'Posicao do elemento 50: {posicao}')
    print('Topo: ', p1.topo())

    for i in range(15):
        print('Desempilhando:', p1.desempilha())
    print(p1)
except PilhaException as ae:
    print(ae)
print(p1)

print('Tamanho de P1:', len(p1))






