letters = ['m', 'r', 'o', 't', 's']
letters[0]='q' #before froze
fSet = frozenset(letters)
letters[2]='n' #after froze

print('Frozen set is:', fSet)
print('Empty frozen set is:', frozenset())