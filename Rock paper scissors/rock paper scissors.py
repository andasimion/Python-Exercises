# Make a two-player Rock-Paper-Scissors game.
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

def the_winner(option1, option2):
    lower_player1 = option1.lower()
    lower_player2 = option2.lower()

    if lower_player1 == lower_player2:
        return (lower_player1, lower_player2)

    rules = {('rock', 'scissors'): 'rock', ('scissors', 'rock'): 'rock', ('scissors', 'paper'): 'scissors',
     ('paper', 'scissors'): 'scissors', ('paper', 'rock'): 'paper', ('rock', 'paper'): 'paper'}
    players = (lower_player1, lower_player2)

    return rules[players]

print 'Let\'s play Rock Paper Scissors!'
try:

    player1 = raw_input('Choose what you prefer:')
    player2 = raw_input('Now it\'s your turn:')
    winner = the_winner(player1, player2)
    if type(winner) is tuple:
        print 'It\'s a tie!'
    else:
        print 'The winner is %s' % winner

except KeyError:
    print 'Please enter the words rock, scissors or paper!'
