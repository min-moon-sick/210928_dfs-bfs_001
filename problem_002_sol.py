


n = 5
m = 6

x = 1
y = 1


a = [
  [-1, 0],
  [1,0],
  [0,-1],
  [0,1]
]

graph = [
  [1,0,1,0,1,0],
  [1,1,1,1,1,1],
  [0,0,0,0,0,1],
  [1,1,1,1,1,1],
  [1,1,1,1,1,1]
]

from collections import deque as dq

def bfs(x, y):

  q = dq([[x-1,y-1]])

  # graph[x][y] = 0

  if x < 0 or x > n -1 or y < 0 or y > m -1:
    return 0

  while q:

    v = q.popleft()

    if v[0] == n-1 and v[1] == m-1:
      return graph[n-1][m-1]

    for i in range(len(a)):
      if 0 <= v[0] + a[i][0] <= n-1 and 0 <= v[1] + a[i][1] <= m-1:
        if graph[v[0] + a[i][0]][v[1] + a[i][1]] == 1:
          q.append([v[0] + a[i][0], v[1] + a[i][1]])
          graph[v[0] + a[i][0]][v[1] + a[i][1]] = graph[v[0]][v[1]] + 1


print(bfs(x,y))
# print(graph)



