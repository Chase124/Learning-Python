Number_list = [15,84,200, 50,9]

res = Number_list[0] + Number_list[1]

#print(res)
#print(max(Number_list))
#print(min(Number_list))

creature_list =['elf','dragon','unicorn','cyclops', 'fairy','troll'] #, 'elephant'
creatureNameSize = []
maxCreatureNameSize = 0

#find the size of the biggest creature name
for creature in creature_list:
    print(creature)
    creatureNameSize.append(len(creature))
    print(creature_list)
    print(creatureNameSize)
    maxCreatureNameSize = (max(creatureNameSize))

print(maxCreatureNameSize)

#check inside the list which creature has that size
for creature in creature_list:
    if (len(creature) == maxCreatureNameSize):
        print(creature)
