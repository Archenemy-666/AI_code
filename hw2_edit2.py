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
        return successors
 
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


#create constraints by adding scores and then score 0 nodes are removed, highest score is 2
def constraintProp(curr,maze,flip):
    score = 0
    scoreList = []
    x = successor(curr[0],curr[1],maze,flip)
    for explore in successor(curr[0],curr[1],maze,flip):
        if  (len(successor(explore[0],explore[1],maze,explore[2])) == 0) and (maze[explore[0]][explore[1]] != 'F'):    
            if (len(successor(explore[0],explore[1],maze,explore[2])) == 0 ):
                score = 0
                continue
        if (maze[explore[0]][explore[1]] == 'F'):
            score = 2
        if  (len(successor(explore[0],explore[1],maze,explore[2])) > 0 ) and (maze[explore[0]][explore[1]] != 'F'):
            score = 1
        
        for sense in successor(explore[0],explore[1],maze,explore[2]):
            if (maze[sense[0]][sense[1]] == 'F'):
                score = 2

        flip = explore[2]
        scoreList.append([explore[0],explore[1],flip,score])
    
    from operator import itemgetter
    scoreList = sorted(scoreList,key=itemgetter(3), reverse = False)     
    #print("actualList : ",x)
    #print("score list : ",scoreList)    
    return scoreList 

# Using local search to traverse through the tree.
def LocalSearch(cr,cc,maze):
    flip = False
    score = 0
    start = ([cr,cc,flip,score])
    visited = []
    stack = [(start,[start])]
    steps = 0
    while stack:
        curr, path = stack.pop()
        if curr in visited:
            continue
        visited.append(curr)
        if (maze[curr[0]][curr[1]] == 'F'):
           return path,steps
        if (len(path) == 1):
            for next_pos in constraintProp(curr,maze,flip):
                stack.append((next_pos, path+[next_pos]))
                steps += 1
        elif(len(path) > 1):
            flip = curr[2]
            
            #add constraint function to filter and funnel the ordered list(oreder is critical) 
            for next_pos in constraintProp(curr,maze,flip):
                stack.append((next_pos, path+[next_pos]))
                steps += 1
    return [], steps
                

# ---------------------------------------------------------------------------------------------
def main():
    from operator import itemgetter 
    maze = create()
    path , cost = LocalSearch(0,0,maze)
    #print(MazeSolver_constraintProp(start,maze))
    if len(path) != 0:
        directionList = []
        for i in path:
            directionList.append(maze[i[0]][i[1]])
        print("path : ",path)
        print("path in direction values : ",directionList)
        print("cost : ",cost)
        print("length of path : ",len(path))
    else: 
        print("no dfs solution")



if __name__ == "__main__":
    main()

