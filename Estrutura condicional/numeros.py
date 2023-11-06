# escreva um programa que leia dois numeros inteiros e compare-os mostrandi na tela uma mensaguem: 
# 0 primeiro valor é maior
# O segundo valor é maior
# O Não existe valor maior, os dois são iguais
n1 = int(input())
n2 = int(input())
if n1 > n2:
    print('O primeiro valor é maior')
elif n1 < n2:
    print('O segundo valor é maior')
elif  n1 == n2:
    print('São iguais')