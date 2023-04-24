## ----------------------------- Water Jug Problem ---------------------------------
##                                                               Date: 20-April-2022
##                                                                                
## Define 6 Functions for 6 operators                                             
##     - Fill Jug 1                                                               
##     - Fill Jug 2                                                               
##     - Transfer from Jug 1 to Jug 2                                             
##     - Transfer from Jug 2 to Jug 1                                             
##     - Empty Jug 1                                                              
##     - Empty Jug 2                                                              
##                                                                                
## Capacity of Jug 1 = 4                                                          
## Capacity of Jug 2 = 3                                                          
## Goal state = 2 Galloons of water in Jug 1                                      
## Find the total number of steps required to reach the goal state                
##                                                                                
## ---------------------------------------------------------------------------------

Initial = [0, 0]


def Full3(jugs):
    tempjugs = [0, 0]
    if jugs[1] == 3:
        return jugs
    else:
        tempjugs[0] = jugs[0]
        tempjugs[1] = 3
    return tempjugs


def Full4(jugs):
    tempjugs = [0, 0]
    if jugs[0] == 4:
        return jugs
    else:
        tempjugs[1] = jugs[1]
        tempjugs[0] = 4
    return tempjugs


def From3to4(jugs):
    tempjugs = [0, 0]
    tempjugs[0] = jugs[0]
    tempjugs[1] = jugs[1]

    if jugs[0] == 4:
        return jugs
    while tempjugs[0] != 4 and tempjugs[1] != 0:
        tempjugs[0] = tempjugs[0] + 1
        tempjugs[1] = tempjugs[1] - 1
    return tempjugs


def From4to3(jugs):
    tempjugs = [0, 0]
    tempjugs[0] = jugs[0]
    tempjugs[1] = jugs[1]

    if jugs[1] == 3:
        return jugs
    while tempjugs[0] != 0 and tempjugs[1] != 3:
        tempjugs[0] = tempjugs[0] - 1
        tempjugs[1] = tempjugs[1] + 1
    return tempjugs


def Empty4(jugs):
    tempjugs = [0, 0]
    tempjugs[0] = jugs[0]
    tempjugs[1] = jugs[1]

    if tempjugs[0] != 0:
        tempjugs[0] = 0
    return tempjugs


def Empty3(jugs):
    tempjugs = [0, 0]
    tempjugs[0] = jugs[0]
    tempjugs[1] = jugs[1]

    if tempjugs[1] != 0:
        tempjugs[1] = 0
    return tempjugs


queue = []

queue.append(Initial)

tempJugs = []
count = 0

while len(queue) != 0:
    Initial = queue.pop(0)
    print(Initial)

    if Full3(Initial)[0] != 2:
        queue.append(Full3(Initial))
        count += 1
    else:
        break

    if Full4(Initial)[0] != 2:
        queue.append(Full4(Initial))
        count += 1
    else:
        break

    if From3to4(Initial)[0] != 2:
        queue.append(From3to4(Initial))
        count += 1
    else:
        break

    if From4to3(Initial)[0] != 2:
        queue.append(From4to3(Initial))
        count += 1
    else:
        break

    if Empty3(Initial)[0] != 2:
        queue.append(Empty3(Initial))
        count += 1
    else:
        break

    if Empty4(Initial)[0] != 2:
        queue.append(Empty4(Initial))
        count += 1
    else:
        break

    if Initial[0] == 2:
        print(f"Final State Reached : {Initial}\nNo. of nodes explored : {count}")
        break

print(f"Number of nodes explored : {count}")