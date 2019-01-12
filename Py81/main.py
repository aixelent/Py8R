from Crypto.Util import number

length = 2048
prime = number.getPrime(length, randfunc=None)

print(prime)
