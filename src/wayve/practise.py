from queue import Queue

def balance_data(data_str):
    def toNumber(str):
        try:
            return float(str)
        except ValueError:
            pass

    splitted = data_str.split(",")
    numbers0 = list(map(toNumber, splitted))
    numbers = list(filter(lambda x: isinstance(x, float), numbers0))
    byInterval = {0: [], 1: [], 2: [], 3: [], 4: []}
    for number in numbers:
        interval = int(number * 5)
        byInterval[interval].append(number)
    min_lenght = min(map(lambda x: len(x), list(byInterval.values())))
    sublists = list(map(lambda x: x[:min_lenght], list(byInterval.values())))
    balanced = [item for sublist in sublists for item in sublist]
    return ','.join(str(x) for x in balanced)

# Return array of articles sorted by number of comments of lenght less than limit
def topArticles(limit):
    import urllib.request
    import json

    fp = urllib.request.urlopen("https://jsonmock.hackerrank.com/api/articles?page=1")
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    decoded = json.loads(mystr)
    npages=decoded["total_pages"]
    total=[]
    fp.close()

    for i in range(npages):
        fp = urllib.request.urlopen("https://jsonmock.hackerrank.com/api/articles?page="+str(i))
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        decoded = json.loads(mystr)
        data = decoded["data"]
        filtered = list(filter(lambda x: x["num_comments"] != None, data))
        total+=filtered
        fp.close()

    result=sorted(total,key=lambda x:x["num_comments"],reverse=True)
    return result[:5]

def horseMinMoves(n, startRow, startCol, endRow, endCol):
    validMovesCol=[-2,-2,2,2,-1,-1,1,1]
    validMovesRow=[-1,1,-1,1,-2,2,-2,2]

    def isValid(col,row):
        return col>=1 and row>=1 and col<=n and row<=9

    class PosDistance:
        def __init__(self,col,row,dist):
            self.col=col
            self.row=row
            self.distance=dist

        def __str__(self):
            return "< "+str(self.col)+", "+str(self.row)+", "+str(self.distance)+">"

        def __repr__(self):
            return self.__str__()

    queue=Queue()
    visited=set()

    queue.put(PosDistance(startCol,startRow,0))
    while True:
        node=queue.get()
        if node.col==endCol and node.row==endRow:
            return node.distance

        if node not in visited:
            visited.add(node)

            for i in range(8):
                p=PosDistance(node.col+validMovesCol[i],node.row+validMovesRow[i], node.distance+1)
                if isValid(p.col,p.row):
                    queue.put(p)

def getDistanceMetrics(arr):
    result= [0] * len(arr)

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                result[i]+=j-i
                result[j]+=j-i
    return result

if __name__ == "__main__":
    # r = balance_data("0.1,0.15, 0.9,0.25,0.46,0.73,k")
    # r = topArticles(5)
    # for d in r:
    #     print(d)

    # r=horseMinMoves(8,1,1,2,2)
    # print(r)

    print(getDistanceMetrics([1,2,3,1,1,2]))