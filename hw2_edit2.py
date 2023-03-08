def create():
    #input matrix size 
    size = int(input("enter the size of square matrix: \n"))
    maze = []
    print("please enter the maze in a row wise pattern: \n")
    for i in range (size):
        elements = list(map(str, input().split()))
        maze.append(elements) 
    return maze

def successor(cr,cc,maze,flip):
    successors = []
    if flip == False:
        flip = True
        if (maze[cr][cc] == 'N'):
            for tr in range(1,len(maze)):
                north = cr - tr
                if north in range(0,len(maze)):
                    successors.append([north,cc,flip])
        if (maze[cr][cc] == 'S'):
            for tr in range(1,len(maze)):
                south = cr + tr
                if south in range(0,len(maze)):
                    successors.append([south,cc,flip])

        if (maze[cr][cc] == 'E'):
            for tc in range(1,len(maze)):
                east = cc + tc
                if east in range(0,len(maze)):
                    successors.append([cr,east,flip])

        if (maze[cr][cc] == 'W'):
            for tc in range(1,len(maze)):
                west = cc - tc
                if west in range(0,len(maze)):
                    successors.append([cr,west,flip])

        if (maze[cr][cc] == 'NE'):
            for temp in range(1,len(maze)):
                northeastR = cr - temp
                northeastC = cc + temp
                if northeastR in range(0,len(maze)) and northeastC in range(0,len(maze)):
                    successors.append([northeastR,northeastC,flip])        
     
        if (maze[cr][cc] == 'NW'):
            for temp in range(1,len(maze)):
                northwestR = cr - temp
                northwestC = cc - temp
                if northwestR in range(0,len(maze)) and northwestC in range(0,len(maze)):
                    successors.append([northwestR,northwestC,flip]) 

        if (maze[cr][cc] == 'SE'):
            for temp in range(1,len(maze)):
                southeastR = cr + temp
                southeastC = cc + temp
                if southeastR in range(0,len(maze)) and southeastC in range(0,len(maze)):
                    successors.append([southeastR,southeastC,flip]) 

        if (maze[cr][cc] == 'SW'):
            for temp in range(1,len(maze)):
                southwestR = cr + temp
                southwestC = cc - temp
                if southwestR in range(0,len(maze)) and southwestC in range(0,len(maze)):
                    successors.append([southwestR,southwestC,flip]) 
#---------------------
    if flip == True:
        flip = False 

        if (maze[cr][cc] == 'N'):
            for tr in range(1,len(maze)):
                south = cr + tr
                if south in range(0,len(maze)):
                    successors.append([south,cc,flip])

        if (maze[cr][cc] == 'S'):
            for tr in range(1,len(maze)):
                north = cr - tr
                if north in range(0,len(maze)):
                    successors.append([north,cc,flip])

        if (maze[cr][cc] == 'E'):
            for tc in range(1,len(maze)):
                west = cc - tc
                if west in range(0,len(maze)):
                    successors.append([cr,west,flip])

        if (maze[cr][cc] == 'W'):
            for tc in range(1,len(maze)):
                east = cc + tc
                if east in range(0,len(maze)):
                    successors.append([cr,east,flip])

        if (maze[cr][cc] == 'NE'):
            for temp in range(1,len(maze)):
                southwestR = cr + temp
                southwestC = cc - temp
                if southwestR in range (0,len(maze)) and southwestC in range (0,len(maze)):
                    successors.append([southwestR,southwestC,flip])

        if (maze[cr][cc] == 'NW'):
            for temp in range(1,len(maze)):
                southeastR = cr + temp
                southeastC = cc + temp
                if southeastR in range (0,len(maze)) and southeastC in range (0,len(maze)):
                    successors.append([southeastR,southeastC,flip])

        if (maze[cr][cc] == 'SE'):
            for temp in range(1,len(maze)):
                northwestR = cr - temp
                northwestC = cc - temp
                if northwestR in range (0,len(maze)) and northwestC in range (0,len(maze)):
                    successors.append([northwestR,northwestC,flip])


        if (maze[cr][cc] == 'SW'):
            for temp in range(1,len(maze)):
                northeastR = cr - temp
                northeastC = cc + temp
                if northeastR in range (0,len(maze)) and northeastC in range (0,len(maze)):
                    successors.append([northeastR,northeastC,flip])
    
    return successors 

#def ConstraintandOrganize(domain,maze):
    
#    scoreDomain = [
#    for var in domain:
#        row = var[0]
#        col = var[1]
#        if maze[row,col]


#def MazeSolver_constraintProp(start,maze):
#    v = None
#    domain_head = []
#    domain_tail = []
#    headScore = None
#    tailScore = None
#    flip = None 
#    goal = [None,None]
    
#    for row in range(len(maze)):
#        for col in range(len(maze)):
#            v = [row,vol]
#            domain_head = successors_head(v,maze)
#            domain_tail = successors_tail(v,maze)
#    return domain_head,domain_tail
def constraintProp(curr,maze,flip):
    score = 0
    scoreList = []
    x = successor(curr[0],curr[1],maze,flip)
    for explore in successor(curr[0],curr[1],maze,flip):
        if (len(successor(explore[0],explore[1],maze,flip)) == 0):
            continue
        if (len(successor(explore[0],explore[1],maze,flip)) > 0):
            score = 1
            #scoreList.append((explore[0],explore[1],flip,score))
            for temp in successor(explore[0],explore[1],maze,explore[2]):
                if (maze[temp[0]][temp[1]] == 'F'):
                    score = 2
                    scoreList.append([explore[0],explore[1],explore[2],score])
            if (score == 1):
                scoreList.append([explore[0],explore[1],explore[2],score])
    #print(scoreList)
    
    from operator import itemgetter
    scoreList = sorted(scoreList, key=itemgetter(3),reverse=True)
    print(scoreList)
    return scoreList        



def LocalSearch(cr,cc,maze):
    flip = False
    score = 0
    start = ([cr,cc,flip,score])
    visited = []
    stack = [(start,[start])]
    while stack:
        curr, path = stack.pop()
        constraintProp(curr,maze,flip)
        if curr in visited:
            continue
        visited.append(curr)
        if (maze[curr[0]][curr[1]] == 'F'):
            return path,(len(path)-1)
        if (len(path) == 1):
            for next_pos in successor(curr[0],curr[1],maze,flip):
                stack.append((next_pos, path+[next_pos]))
        elif(len(path) > 1):
            flip = curr[2]
            #add constraint function to filter and funnel the ordered list(oreder is critical) 
            for next_pos in successor(curr[0],curr[1],maze,flip):
                stack.append((next_pos, path+[next_pos]))
    return [], None
                

# ---------------------------------------------------------------------------------------------
def main():
    from operator import itemgetter 
    maze = create()
    path , cost = LocalSearch(0,0,maze)
    #print(MazeSolver_constraintProp(start,maze))
    print("this is the path : ",path)
if __name__ == "__main__":
    main()

