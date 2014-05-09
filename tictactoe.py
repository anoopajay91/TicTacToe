print "welcome to tic - tac - toe game"
#dictionary containing null values initially, corresponds to values on board
d = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

#to store winner info, 1 value stands for winner
winner ={'x':0,'o':0}


#to fill the board after each time user enters
def fill(d):
    for each in range(1,4):
        if each == 2:
            print ' '+d[1]+" ' "+d[2]+" ' "+d[3]
        else:
            print ' '*3+"'"+' '*3+"'"+' '*3
    print '-'*11
    for each in range(1,4):
        if each == 2:
            print ' '+d[4]+" ' "+d[5]+" ' "+d[6]
        else:
            print ' '*3+"'"+' '*3+"'"+' '*3
    print '-'*11
    for each in range(1,4):
        if each == 2:
            print ' '+d[7]+" ' "+d[8]+" ' "+d[9]
        else:
            print ' '*3+"'"+' '*3+"'"+' '*3


#to print gap
def gap():
    for each in range(1,4):
        print

# to check if anyone has won
def check(d):
    return((('x' in [d[1],d[2],d[3]] or 'o' in [d[1],d[2],d[3]]) and  d[1]==d[2]==d[3])
    or (('x' in [d[1],d[4],d[7]] or 'o' in [d[1],d[4],d[7]]) and d[1]==d[4]==d[7])
      or (('x' in [d[1],d[5],d[9]] or 'o' in [d[1],d[5],d[9]]) and d[1]==d[5]==d[9])
      or (('x' in [d[4],d[5],d[6]] or 'o' in [d[4],d[5],d[6]])  and d[4]==d[5]==d[6])
      or (('x' in [d[2],d[5],d[8]] or 'o' in [d[2],d[5],d[8]])  and d[2]==d[5]==d[8])
      or (('x' in [d[3],d[6],d[9]] or 'o' in [d[3],d[6],d[9]])  and d[3]==d[6]==d[9])
      or (('x' in [d[7],d[8],d[9]] or 'o' in [d[7],d[8],d[9]])  and d[7]==d[8]==d[9])
      or (('x' in [d[3],d[5],d[7]] or 'o' in [d[3],d[5],d[7]]) and d[3]==d[5]==d[7])
      or (sum(1 for each in d.values() if each=='x') + sum(1 for each in d.values() if each=='o') == 9))


# to find out the winner, should change this, feels redundant.
def findWinner():
    if d[1]==d[2]==d[3]:
        winner[d[1]]=1
    elif d[1]==d[4]==d[7]:
        winner[d[1]]=1
    elif d[1]==d[5]==d[9]:
        winner[d[1]]=1
    elif d[4]==d[5]==d[6]:
        winner[d[4]]=1
    elif d[2]==d[5]==d[8]:
        winner[d[2]]=1
    elif d[3]==d[6]==d[9]:
        winner[d[3]]=1
    elif d[7]==d[8]==d[9]:
        winner[d[7]]=1
    elif d[3]==d[5]==d[7]:
        winner[d[3]]=1


# to check if values entered on board are within range, if so return that number
def checkRange(user,name):
    if name=="user1":
        while(user<=0 or user>9):
          print 'not in range..plz try again'
          user=int(raw_input("enter where you want to place x: "))
    else:
        while(user<=0 or user>9):
          print 'not in range..plz try again'
          user=int(raw_input("enter where you want to place o: "))

    return user


#printing empty board
fill(d)
gap()

initial = 1
for each in d:
    d[each]= str(initial)
    initial = initial +1


#printing nos on board so that user knows
#which number to enter while program prompts
fill(d)
gap()

#resetting all values in d to ' '
for each in d:
    d[each]=' '


user1=int(raw_input("enter where you want to place x: "))
user1 = checkRange(user1,"user1")
d[user1]='x'
fill(d)

user2= int(raw_input("enter where you want to place o: "))
user2 = checkRange(user2,"user2")
while(d[user2]=='x'):
    print "x/o already present"
    user2= int(raw_input("enter where you want to place o: "))
    user2 = checkRange(user2,"user2")

d[user2]='o'
fill(d)

while(1 not in winner.itervalues()):
    
    user1=int(raw_input("enter where you want to place x: "))
    user1 = checkRange(user1,"user1")
    while(d[user1] in ['o','x']):
        print "x/o already present"
        user1= int(raw_input("enter where you want to place x: "))
        user1 = checkRange(user1,"user1")    
    d[user1]='x'
    fill(d)

    if check(d):
        break
    
    user2= int(raw_input("enter where you want to place o: "))
    user2 = checkRange(user2,"user2")    
    while(d[user2] in ['o','x']):
        print "x/o already present"
        user2= int(raw_input("enter where you want to place o: "))
        user2 = checkRange(user2,"user2")
    d[user2]='o'
    fill(d)

    if check(d):
        break
    
findWinner()


result = [value for value in winner if winner[value]==1]
if result==[]:
    print "it's a tie"
else:
    print str(result[0])+" is the winner"
