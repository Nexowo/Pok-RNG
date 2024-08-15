import random as rd
import os

NATURES = ['Adamant',
           'Bashful',
           'Bold',
           'Brave',
           'Calm',
           'Careful',
           'Docile',
           'Gentle',
           'Hardy',
           'Hasty',
           'Impish'
           'Jolly',
           'Lax',
           'Lonely',
           'Mild',
           'Modest',
           'Naive',
           'Naughty',
           'Quiet',
           'Quirky',
           'Rash',
           'Relaxed',
           'Sassy',
           'Serious',
           'Timid']

TYPES = ['Bug',
         'Dark',
         'Dragon',
         'Electric',
         'Fairy',
         'Fighting',
         'Fire',
         'Flying',
         'Ghost',
         'Grass',
         'Ground',
         'Ice',
         'Normal',
         'Poison',
         'Psychic',
         'Rock',
         'Steel',
         'Stellar',
         'Water']

HP = 'HP'
ATK = 'Atk'
DEF = 'Def'
SPATK = 'SpA'
SPDEF = 'SpD'
SPE = 'Spe'

STATS = [HP, ATK, DEF, SPATK, SPDEF, SPE]

NB_POKE_PER_TEAM = 6
NB_PLAYER = 2

class Pokemon:

    iv_list : list[int]
    nature : str
    name : str
    tera_type : str

    def __init__(self, name : str):
        self.name = name
        self.iv_list = [252,252,4,0,0,0]
        rd.shuffle(self.iv_list)
        self.nature = rd.choice(NATURES)
        self.tera_type = rd.choice(TYPES)


    def to_string(self):
        poke_str = self.name + '\nTera Type: ' + self.tera_type + '\nEVs: '
        cnt = 0
        for i in range(6):
            if self.iv_list[i] != 0:
                poke_str += f'{self.iv_list[i]} ' + STATS[i]
                cnt+=1
                if cnt < 3:
                    poke_str+= ' / '
        poke_str += '\n' + self.nature + ' Nature\n'
        poke_str += '\n'

        return poke_str
    
def init_dict():
    d : dict[str,list[str]]= {}
    f = open('pokemons', 'r')
    for x in f:
        pokedex_line = x.split(',')
        if pokedex_line[0] in d.keys():
            d[pokedex_line[0]].append(pokedex_line[1])
        else:
            d[pokedex_line[0]] = [pokedex_line[1]]

    f.close()

    return d


if __name__ == '__main__':
    d = init_dict()

    for i in range(NB_PLAYER):
        if os.path.exists(f'stats_p{i+1}.txt'):
            os.remove(f'stats_p{i+1}.txt')
    
        file = open(f'stats_p{i+1}.txt', 'a')
        
        for _ in range(NB_POKE_PER_TEAM):
            names = rd.choice(list(d.values()))
            name = ''
            if len(names) > 1:
                name = rd.choice(names)
            else:
                name = names[0]

            poke = Pokemon(name)
            file.write(poke.to_string())
        
        file.close()