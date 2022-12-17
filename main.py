lines = open('input2')
myScore = 0
theirScore = 0
game = []

print("ENTERING READ LOOP")
for line in lines:
    plays = line.rsplit( )
    game.append(plays)


# A and X are rock || B and Y are paper || C and Z are scissors
print("ENTERING LOGIC LOOP")
for match in game:
    if match[0] == 'A':
        match match[1]:
            #ROCK V ROCK = DRAW
            case 'X':
                myScore = myScore + 3 + 1
                theirScore = theirScore + 3 + 1
                #print("HERE2X")
            case 'Y':
                #ROCK V PAPER = I WIN
                myScore = myScore + 6 + 2
                theirScore = theirScore + 1
            case 'Z':
                #ROCK v SCISSORS = I LOSE
                myScore = myScore + 3
                theirScore = theirScore + 6 + 1

    if match[0] == 'B':
        match match[1]:
            case 'X':
                #PAPER V ROCK = I LOSE
                myScore = myScore + 1
                theirScore = theirScore + 6 + 2
            case 'Y':
                # PAPER V PAPER = DRAW
                myScore = myScore + 3 + 2
                theirScore = theirScore + 3 + 2
            case 'Z':
                #PAPER V SCISSORS = I WIN
                myScore = myScore + 3 + 6
                theirScore = theirScore + 2

    if match[0] == 'C':
        match match[1]:
            case 'X':
                #SCISSORS V ROCK = I WIN
                myScore = myScore + 6 + 1
                theirScore = theirScore + 3
                #print("HERE2X")
            case 'Y':
                #SCISSORS V PAPER = I LOSE
                myScore = myScore + 2
                theirScore = theirScore + 6 + 3
            case 'Z':
                #SCISSORS V SCISSORS = DRAW
                myScore = myScore + 3 + 3
                theirScore = theirScore + 3 + 3


print("\nTOTAL LINES IN FILE " + len(game).__str__())
print("THEIR SCORE: " + theirScore.__str__())
print("MY SCORE: " + myScore.__str__())




