# alphebetize a list, calculate scores, sum the scores
# project_euler.com/problem=22


def alphabetize(file_name = "names.txt"):
  f = open(file_name, 'r')
  names = []
  for line in f:
    names = str.split(str.replace(str.replace(line, '\"', ''), '\r', ''), ',')
  names.sort()
  # replace each name with its score
  alphaval = dict(zip([chr(x) for x in range(65, 91)], range(1, 27)))
  for i in range(len(names)):
    names[i] = sum(alphaval[l] for l in names[i]) * (i + 1)
  print sum(names)





