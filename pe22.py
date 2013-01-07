# alphebetize a list, calculate scores, sum the scores
# project_euler.com/problem=22


def alphabetize(names):
  names.sort()
  # replace each name with its score
  for i in range(len(names)):
    score = 0
    for l in names[i]:
      if str.isalpha(l):
        score += ord(str.upper(l)) - ord('A') + 1
    score *= (i + 1)
    names[i] = score 
  print sum(names)

def main(file_name = "names.txt"):
  f = open(file_name, 'r')
  names = []
  for line in f:
    names += string.split(line, ',')
  alphabetize(names)





