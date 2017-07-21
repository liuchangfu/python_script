import copy

Anndy = ['Anndy', ['age', 24]]
Tom = copy.deepcopy(Anndy)
Cindy = copy.deepcopy(Anndy)


Tom[0] = 'Tom'
Cindy[0] = 'Cindy'

Tom[1][1] = 12
print (Anndy, Tom, Cindy)

print ([id(x) for x in Anndy])
print ([id(x) for x in Tom])
print ([id(x) for x in Cindy])