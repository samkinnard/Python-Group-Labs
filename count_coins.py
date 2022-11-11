# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         SAM KINNARD
# Section:      565
# Assignment:   11.12
# Date:         11/11/2022

# establishing variables that will be added on to later
count = 0
numcoins = 0
coinlist = []

# opening and reading the file line by line
with open('game.txt', 'r') as newfile:
    lines = newfile.readlines()
    
# while loop that analyzes each line and creates variables
# storing instruction info and numerical data
while count < len(lines):
    info = lines[count].split()
    instruct = info[0]
    num = int(info[1])
    if instruct == "coin":
        numcoins += num
        count += 1
        coinlist.append(num)
    elif instruct == "jump":
        count += num
    else:
        count += 1
        
# closing the game file
newfile.close()

# print statement outputting the total number of coins
print(f'Total coins collected: {numcoins}')

# creating the coin file 
coinfile = open('coins.txt', 'w')
for i in coinlist:
    coinfile.write(str(i))
    coinfile.write('\n')
coinfile.close()
