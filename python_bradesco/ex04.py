prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))

media = (prova1+prova2)/2

if media > 7:
    print("Parabens vode foi aprovado sua média foi {}".format(media))
else:
    print("Infelizmente voce nao foi aprovado sua média foi {}".format(media))