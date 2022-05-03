import math
arg = input()
n, k = arg.split()

binomial_coefficient = math.comb(int(n), int(k))
print(binomial_coefficient)
