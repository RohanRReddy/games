import random
pos1 =0
pos2 =0

ladders ={14:32,19:31,26:48,11:49,56:79,62:88,80:99}
snakes ={17:7,54:34,61:42,64:32,87:24,93:73,95:75,98:18}

def move(pos):
    dice = random.randint(1,6)
    print('you have rolled',dice)
    pos += dice
    if pos in ladders:
        print("we found a ladder,lets move up")
        pos = ladders[pos]
    elif pos in snakes:
        print("we got bitten by snake,lets go down")
        pos = snakes[pos]
    print('new postion: ',pos)
    return pos

def start():
    global pos1,pos2
    while True:
        player1 = input('player1 turn: \n enter "y" to contine: ')
        if player1=='y':
            pos1 = move(pos1)
            if pos1 ==100:
                print ('player 1 wins')
                break
        
        player2 =input('player2 turn: \nenter "y" to contine:')
        if player2 == 'y':
            pos2 = move(pos2)
            if pos2 == 100:
                print ('player 2 wins')
                break

if __name__ == '__main__':
    start()