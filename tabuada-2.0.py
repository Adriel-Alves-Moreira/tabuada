num = int(input("Digite um numero para ver sua tabuada: "))
print('--=-' *5)
for c in range (1, 11):
    print("{} x {:2} = {}".format(num, c, num*c))
print('--=-' *5)
