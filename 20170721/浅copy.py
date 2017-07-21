Anndy = ['Anndy',['age',24]]
Tom = Anndy[:]
Cindy = list(Anndy)

print(Anndy,id(Anndy))
print(Tom,id(Tom))
print(Cindy,id(Cindy))

Tom[0] = 'Tom'
Cindy[0] = 'Cindy'

print('Anndy:',Anndy,'Tom:',Tom,'Cindy:',Cindy)

Tom[1][1] = 12
print('Anndy:',Anndy,'Tom:',Tom,'Cindy:',Cindy)
