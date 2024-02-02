from copy import deepcopy

players = [{
    'first_name': 'John',
    'last_name' : 'Doe',
    'rank' : 3
},
{
    'first_name': 'Kevin',
    'last_name' : 'McCalisster',
    'rank' : 1
},
{
    'first_name': 'Brad',
    'last_name' : 'Kelvin',
    'rank' : 2
},
]

print(players)

print(sorted(players, key=lambda player: player['rank'], reverse=True))

def check_top_3_player(player):
    updated_player = deepcopy(player)
    updated_player['is_top_3'] = True if updated_player['rank'] <=3 else False

    return updated_player

top_players = map(check_top_3_player, players)
print(list(top_players))