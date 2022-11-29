#create the emty list
goals = []

#append the goals
n = int(input("How many goals do you want? "))
for i in range(5) :
    new = input("Add a new goal to the list")
    goals.append(new)

prints(goals)
#edit an item
i = input('Which goal do you want to changge?')
# convert i from string to the interger
i = int(i)
goal[i-1] = input(' Enter a new goal: ')

print(goals)

#delete an item
i = int(input( 'Which goal do you want to delete? '))
del goals[i-1]
print(goals)