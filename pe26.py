# project euler 26
# long division
# this is pretty heinous

n = 1000
repeatLens = [0 for i in range(n)]
for i in range(2, n):
  remainders = []
  numerator = 1
  repeating = False
  while numerator != 0:
    while numerator < i: numerator *= 10
    try:
      remainders.index(numerator)
      repeating = True
      break
    except ValueError:
      remainders.append(numerator)
      numerator = numerator - (numerator / i) * i
  if repeating: repeatLens[i] = len(remainders)

longest = max(repeatLens)
print repeatLens.index(longest), longest
