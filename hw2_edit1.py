#Constraint Satisfaction Problem:
# 1. Variables 
# 2. Domains 
# 3. Constraints

#create maze
def create():
    #input matrix size 
    size = int(input("enter the size of square matrix: \n"))
    maze = []
    print("please enter the maze in a row wise pattern: \n")
    for i in range (size):
        elements = list(map(str, input().split()))
        maze.append(elements) 
    return maze
def successor_head(v,maze):
    successors = []
    row = v[0]
    col = v[1]
    if (maze[v[0]][v[1]] == 'N'):
        for tr in range(1,len(maze)):
            north = row - tr
            if north in range(0,len(maze)):
                successors.append([north,col])
    if (maze[v[0]][v[1]] == 'S'):
        for tr in range(1,len(maze)):
            south = row + tr
            if south in range(0,len(maze)):
                successors.append([south,col])

    if (maze[v[0]][v[1]] == 'E'):
        for tc in range(1,len(maze)):
            east = col + tc
            if east in range(0,len(maze)):
                successors.append([row,east])

    if (maze[v[0]][v[1]] == 'W'):
        for tc in range(1,len(maze)):
            west = col - tc
            if west in range(0,len(maze)):
                successors.append([row,west])

    if (maze[v[0]][v[1]] == 'NE'):
        for temp in range(1,len(maze)):
            northeastR = row - temp
            northeastC = col + temp
            if northeastR in range(0,len(maze)) and northeastC in range(0,len(maze)):
                successors.append([northeastR,northeastC])        
     
    if (maze[v[0]][v[1]] == 'NW'):
        for temp in range(1,len(maze)):
            northwestR = row - temp
            northwestC = col - temp
            if northwestR in range(0,len(maze)) and northwestC in range(0,len(maze)):
                successors.append([northwestR,northwestC]) 

    if (maze[v[0]][v[1]] == 'SE'):
        for temp in range(1,len(maze)):
            southeastR = row + temp
            southeastC = col + temp
            if southeastR in range(0,len(maze)) and southeastC in range(0,len(maze)):
                successors.append([southeastR,southeastC]) 

    if (maze[v[0]][v[1]] == 'SW'):
        for temp in range(1,len(maze)):
            southwestR = row + temp
            southwestC = col - temp
            if southwestR in range(0,len(maze)) and southwestC in range(0,len(maze)):
                successors.append([southwestR,southwestC]) 

    return successors
    
def successor_tail(v,maze):
    row = v[0]
    col = v[1]
    successors = []
    if (maze[v[0]][v[1]] == 'N'):
        for tc in range(1,len(maze)):
            south = col + tc
            if south in range(0,len(maze)):
                successors.append([south,col])

    if (maze[v[0]][v[1]] == 'S'):
        for tc in range(1,len(maze)):
            north = col - tc
            if north in range(0,len(maze)):
                successors.append([north,col])

    if (maze[v[0]][v[1]] == 'E'):
        for tc in range(1,len(maze)):
            west = col - tc
            if west in range(0,len(maze)):
                successors.append([row,west])

    if (maze[v[0]][v[1]] == 'W'):
        for tc in range(1,len(maze)):
            east = col + tc
            if east in range(0,len(maze)):
                successors.append([row,east])

    if (maze[v[0]][v[1]] == 'NE'):
        for temp in range(1,len(maze)):
            southwestR = row + temp
            southwestC = col - temp
            if southwestR in range (0,len(maze)) and southwestC in range (0,len(maze)):
                successors.append([southwestR,southwestC])

    if (maze[v[0]][v[1]] == 'NW'):
        for temp in range(1,len(maze)):
            southeastR = row + temp
            southeastC = col + temp
            if southeastR in range (0,len(maze)) and southeastC in range (0,len(maze)):
                successors.append([southeastR,southeastC])

    if (maze[v[0]][v[1]] == 'SE'):
        for temp in range(1,len(maze)):
            northwestR = row - temp
            northwestC = col - temp
            if northwestR in range (0,len(maze)) and northwestC in range (0,len(maze)):
                successors.append([northwestR,northwestC])


    if (maze[v[0]][v[1]] == 'SW'):
        for temp in range(1,len(maze)):
            northeastR = row - temp
            northeastC = col + temp
            if northeastR in range (0,len(maze)) and northeastC in range (0,len(maze)):
                successors.append([northeastR,northeastC])

    return successors 

def MazeSolver_constraintProp(start,maze):
    v = None
    domain_head = []
    domain_tail = []
    headScore = None
    tailScore = None
    flip = None
    goal = [None,None]
    variables = [(v,domain_head,domain_tail)]
    scores_head = [(v,headScore)]
    scores_tail = [(v,tailScore)]
    for row in range(len(maze)):
        for col in range(len(maze)):
            v = [row,col]
            # domain needs to be taken from the successors
            domain_head = successor_head(v,maze)
            domain_tail = successor_tail(v,maze)
            variables.append((v,domain_head,domain_tail))
            if (maze[row][col] == 'F'):
                goal = [row,col]
    #parse through the varibles and iassign scores
    for pointer in variables:
        domain_head = pointer[1]
        domain_tail = pointer[2]
        v = pointer[0]
        if v != None:
            if maze[v[0]][v[1]] != 'F':
                if (len(domain_head) == 0):
                    headScore = 0
                if (len(domain_tail) == 0):
                    tailScore = 0
                if(len(domain_head) != 0 ):
                    headScore = 1
                    if [2,2] in domain_head:
                        headScore = 2
                if(len(domain_tail) != 0 ):
                    tailScore = 1
                    if goal in domain_tail:
                        tailScore = 2
                print(headScore,goal)
                scores_head.append((v,headScore))
                scores_tail.append((v,tailScore))
                
    print(variables,"\n")
    print(scores_head,"\n")
    print(scores_tail,"\n")
    return variables,scores_tail,scores_tail



#main function
def main():
    maze = create()
    start = [0,0]
    print(MazeSolver_constraintProp(start,maze))

if __name__ == "__main__":
    main()

