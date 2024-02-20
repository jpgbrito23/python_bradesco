n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
print("Os valores de cada variavel em ordem sao {} e {}".format(n1,n2))

resposta = str(input("Deseja fazer uma mágica: "))

if resposta.lower() == "sim":
    n3=n1;
    n1=n2;
    n2=n3;
    print("agora o valor da variavel 1 é {} e o da 2 é {}".format(n1,n2))
else:
    print("que pena!")