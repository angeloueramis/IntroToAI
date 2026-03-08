import heapq

# | Terrain     | Symbol | Energy Cost |
# | ----------- | ------ | ----------- |
# | Start       | S      | 1           |
# | Goal        | G      | 1           |
# | Flat ground | .      | 1           |
# | Uphill      | ^      | 4           |
# | Downhill    | v      | 2           |
# | Rock        | #      | blocked     |

example1 = [
['S','.','^','.','.'],
['.','^','^','.','.'],
['.','.','v','.','.'],
['#','.','.','^','.'],
['.','.','.','.','G']
]

example2 = [
['S','.','.','^','.'],
['.','#','.','^','.'],
['.','#','.','.','.'],
['.','.','v','.','.'],
['.','.','.','.','G']
]

terrain_cost={
'.':1,
'^':4,
'v':2,
'S':1,
'G':1
}

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def find(grid, symbol):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == symbol:
                return (r,c)

def aStar(grid):

    rows=len(grid)
    cols=len(grid[0])

    start=find(grid,'S')
    goal=find(grid,'G')

    open_list=[]
    heapq.heappush(open_list,(0,start))

    g_score={start:0}
    came_from={}

    while open_list:
        _,current = heapq.heappop(open_list)

        if current==goal:
            path=[]
            while current in came_from:
                path.append(current)
                current=came_from[current]
            path.append(start)
            path.reverse()
            return path

        r,c=current
        neighbors=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

        for nr,nc in neighbors:
            if 0<=nr<rows and 0<=nc<cols:
                if grid[nr][nc]=='#':
                    continue

                cost = terrain_cost[grid[nr][nc]]
                tentative = g_score[current] + cost

                if (nr,nc) not in g_score or tentative < g_score[(nr,nc)]:

                    g_score[(nr,nc)] = tentative
                    f = tentative + heuristic((nr,nc),goal)

                    heapq.heappush(open_list,(f,(nr,nc)))
                    came_from[(nr,nc)] = current
    return None

path1=aStar(example1)
path2=aStar(example2)

print("Best hiking path (example no. 1):")
print(path1)
print("\nBest hiking path (example no. 2):")
print(path2)