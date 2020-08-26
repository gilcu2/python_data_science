import numpy as np
def numberAmazonTreasureTrucks(rows, column, grid):
    # WRITE YOUR CODE HERE
    gridMarks=[]
    for i in range(rows):
        gridMarks.append([0]*column)
    nGroups=0
    for x in range(0,rows):
        for y in range(0,column):
            if grid[x][y]==1:
                if gridMarks[x][y]==0:
                    if x>0 and gridMarks[x-1][y]!=0:
                      gridMarks[x][y]=gridMarks[x-1][y]
                    elif y>0 and gridMarks[x][y-1]!=0:
                        gridMarks[x][y] = gridMarks[x][y - 1]
                    else:
                        nGroups+=1
                        gridMarks[x][y]=nGroups

    return nGroups

if __name__ == '__main__':
    print(numberAmazonTreasureTrucks(5,4,
                               [
                                   [1,1,0,0],
                                   [0,0,1,0],
                                   [0,0,0,0],
                                   [1,0,1,1],
                                   [1,1,1,1]


                                ]))