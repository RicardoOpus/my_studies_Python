# Class types:
a = 5
b = 5.0
c = 'Hello'
d = ('one', 1)
e = {'one': 1}
f = {'one', 'two', 'three'}
g = frozenset(['one', 'two'])
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))


# Help for a command: 
# help(list)


# Lists:
death_metal = ['Morbid Angel', 'Obituary', 'Death']
print('All list:', death_metal)
print('By index:',death_metal[1])
death_metal.append('Cannibal Corpse')
death_metal.remove('Obituary')
print('Actual list:', death_metal)
more_death_metal = ['Pestilence', 'Krisiun']
death_metal.extend(more_death_metal)
print('New list:', death_metal)
print('Index of element Krisiun:', death_metal.index('Krisiun'))
death_metal.sort()
print('Sort list', death_metal)


# Tuple:
best_death_band = ('Death', 1)
greatest_death_bands = [best_death_band]
greatest_death_bands.append(('Krisiun', 2))
greatest_death_bands.extend(
    [
      (death_metal[0], 3),
      (death_metal[3], 4),
      (death_metal[2], 5)
    ]
)
print(greatest_death_bands)


# Dict:
metal_bands = {'Pestilence': 'Death', 'Obituary': 'Death', 'Pentagram': 'Doom'}
print(metal_bands['Pestilence'])
metal_bands['Saint Vitus'] = 'Doom'
print('After add:', metal_bands)
del metal_bands['Pestilence']
print('After remove:', metal_bands)


# Set:
death_albuns = {'Leprosy', 'Altars of Madness', 'Consuming Impulse'}
morbid_angel_albuns = {'Blessed Are The Sick', 'Altars of Madness'}
print('intersection of two sets: ', death_albuns.intersection(morbid_angel_albuns))
print('difference of death_albuns: ', death_albuns.difference(morbid_angel_albuns))
all_albuns = death_albuns.union(morbid_angel_albuns)
print('union of sets: ', all_albuns)
all_albuns.add('Scream Bloody Gore')
print('After add: ', all_albuns)


# Range:
range5 = list(range(5))
print('just the stop: ', range5)
range2To6 = list(range(2,6))
print('start at 2, stop at 6: ', range2To6)
range1To8step2 = list(range(1,8,2))
print('start at 1, stop at 8, setp 2: ', range1To8step2)