import queue
import time


def create_maze():
    maze = [
    ["#","#","#","O","#","#","#"],
    ["#"," "," "," ","#"," ","#"],
    ["#","#","#"," ","#"," ","#"],
    ["#"," ","#"," "," "," ","#"],
    ["#"," ","#"," ","#"," ","#"],
    ["#"," "," "," ","#","#","#"],
    ["#","X","#","#","#","#","#"]]

    return maze




def printMaze(maze, path=""):
    for col_index, pos in enumerate(maze[0]):
        if pos == "O":
            start = col_index

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for row,row_vector in enumerate(maze):
        for col,value in enumerate(row_vector):
            if (row,col) in pos:
                 print("+", end=" ")
               
         
            else:
                print(value,end=" ")
                
        print(end="\n")
        
 


def valid(maze, moves):
    for col_index, pos in enumerate(maze[0]):
        if pos == "O":
            start = col_index

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    for col_index, pos in enumerate(maze[0]):
        if pos == "O":
            start = col_index

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        
        printMaze(maze, moves)
        
        return True

    return False


#ALGORITHM
q = queue.Queue()
q.put("")
path = ""
maze  = create_maze()

while not findEnd(maze, path): 
    path = q.get()
    #print(path)
    for j in ["L", "R", "U", "D"]:
        put = path + j
        if valid(maze, put):
            q.put(put)
