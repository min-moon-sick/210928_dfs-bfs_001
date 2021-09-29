n = 4
m = 5

graph =[
  [0,0,1,1,0],
  [0,0,0,1,1],
  [1,1,1,1,1],
  [0,0,0,0,0]
]


def dfp(x, y):
  
  if -1 >= x or x >= n or -1 >= y or y >= m:
    return 0

  if graph[x][y] == 0:
    graph[x][y] = 1

    dfp(x-1,y)
    dfp(x+1,y)
    dfp(x,y-1)
    dfp(x,y+1)

    return 1
  return 0

cnt = 0
for i in range(n):
  for ii in range(m):
    print("i : {}, ii : {}".format(i, ii))
    if dfp(i,ii) == 1:
      cnt += 1

print(cnt)
