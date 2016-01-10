__author__ = 'caleb'

weapons = {'dagger': [8, 4, 0],
           'shortsword': [10, 5, 0],
           'warhammer': [25, 6, 0],
           'longsword': [40, 7, 0],
           'greataxe': [74, 8, 0]
           }
armor = {'leather': [13, 0, 1],
         'chainmail': [31, 0, 2],
         'splintmail': [53, 0, 3],
         'bandedmail': [75, 0, 4],
         'platemail': [102, 0, 5],
         'noneArmor': [0, 0, 0]}

rings = {'Damage1': [25, 1, 0],
         'Damage2': [50, 2, 0],
         'Damage3': [100, 3, 0],
         'Defense1': [20, 0, 1],
         'Defense2': [40, 0, 2],
         'Defense3': [80, 0, 3],
         'noneLeft': [0, 0, 0],
         'noneRight': [0, 0, 0]}

health = 100

boss = {'hp': 104,
        'damage': 8,
        'armor': 1}

me = {'hp': 100,
      'damage': 0,
      'armor': 0,
      'cost': 0}
loadouts = []
losses = []

for w in weapons:
    for a in armor:
        for left in rings:
            cache = rings[left]
            del rings[left]
            for right in rings:
                stats = me.copy()
                stats['cost'] += weapons[w][0] + armor[a][0] + cache[0] + rings[right][0]
                stats['damage'] += weapons[w][1] + armor[a][1] + cache[1] + rings[right][1]
                stats['armor'] += weapons[w][2] + armor[a][2] + cache[2] + rings[right][2]
                loadouts.append(stats.copy())

            rings[left] = cache

for my_self in loadouts:
    my_boss = boss.copy()
    while my_self['hp'] > 0 and my_boss['hp'] > 0:
        my_boss['hp'] -= max(1, my_self['damage'] - my_boss['armor'])
        if my_boss['hp'] <= 0:
            break
        my_self['hp'] -= max(1, my_boss['damage'] - my_self['armor'])
        if my_self['hp'] <= 0:
            losses.append(my_self['cost'])
            break

print max(losses)