from random import randrange as r, shuffle as sh, sample as sam

# véletlen egész szám 1..20 között:
print(r(1,21))

# 10 véletlen egész számból álló lista:
print([r(1,21) for i in range(10)])

# véletlen egész számbokból álló véletlen elemszámú lista:
print([r(1,21) for i in range(r(1,21))])

# 10 véletlen egész számból álló monoton növekvő (mn) lista:
print(sorted([r(50) for i in range(10)]))

# 10 véletlen egész számból álló szigorúan monoton növekvő (szmn) lista:
l = set()
while len(l) < 10: l.add(r(1,50))
print(sorted(list(l)))

# számok összekeverése
l = list(range(1, 11))
sh(l)
print(l)

#vagy
print(sam(list(range(1, 11)), 10))

#lottószámgenerátor (5-ös lottó)
print(sorted(sam(list(range(1, 91)), 5)))