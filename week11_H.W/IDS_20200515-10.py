primes = {2, 3, 5, 7, 11, 13}
odds = {1, 3, 5, 7, 9, 11, 13}
#交集(.intersection)
print(primes & odds)
print(primes.intersection(odds))
#聯集(.union)
print(primes | odds)
print(primes.union(odds))
#差異(.difference)
print(primes - odds)
print(odds - primes)
print(primes.difference(odds))
print(odds.difference(primes))
#對稱差異(.symmetric_difference)
print((primes - odds) | (odds - primes))
print(primes ^ odds)
print(primes.symmetric_difference(odds))