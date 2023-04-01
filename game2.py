def actions():
    actions = ['rock','paper','scissor']
    return actions

def result(action1,action2):
    if action1 == action2 :
        return 'draw'
    if action1 == 'rock' and action2 == 'scissor':
         winner = 'winner player 1'
    elif action1 == 'paper' and action2 == 'rock':
         winner = 'winner player 1'
    elif action1 == 'scissor' and action2 == 'paper':
         winner = 'winner player 1'
    else:
        winner = 'winner player 2'
    return winner
    
def validationAction(action):
    check = 'false'
    for i in actions():
        if(i == action):
            check = 'true'
    return check

def game(action1,action2):
    check1 = validationAction(action1)
    if(check1 == 'false'):
        return 'invalid action 1'
    check2 = validationAction(action2)
    if(check2 == 'false'):
        return 'invalid action 2'
    return result(action1,action2)

action1 = input('player 1')
action2 = input('player 2')
game(action1,action2)