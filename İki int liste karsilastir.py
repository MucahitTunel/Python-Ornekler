liste1 = [1,2,3,4,56,7,8,9,212]

liste2 = [2,34,2,4,6,523,6,3,3,12]

xliste1 = set(liste1)
xliste2 = set(liste2)

print("Benzerlik: {}".format(xliste1.intersection(xliste2)))

print("Fark: {}".format(xliste1.difference(xliste2)))

print("Birleşim: {}".format(xliste1.union(xliste2)))