# 21092_dfs-bfs_001

python에서 list는 기본적으로 stack 형태

queue를 사용하려면

deque라는 키워드를 알고 있어야 함

from collections import deque 

로 하면 된다.


% list를 2차 배열로 표현할 때 참고

a = [[] for _ in range(3)]

이면

[[], [], []] 

으로 출력된다.


dfs(depth first search)는 stack을 기초로 재귀 함수를 사용하고, bfs(breath first search)는 queue를 활용하여 구현한다.



## dfs

dfs 절차

1. 스택에 탐색 시작 노드를 넣고 방문 처리를 한다
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다
  방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
3. 2번 과정을 수행할 수 없을 때까지 반복한다


######################### dfs #########################
### 그래프 예

graph =[
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]


def dfs(graph, v, visited): # 그래프, 시작 노드, 방문 처리 리스트

  % 현재 노드 방문 처리
  
  visited[v] = 1
  
  print(v)
  
  % 현재 노드에 연결된 다른 노드를 재귀적으로 처리
  
  for i in graph[v]:
  
    if not visited[i]:
    
      dfs(graph, i, visited)


visited = [0] * 9

dfs(graph, 1, visited)

print(visited)

![image](https://user-images.githubusercontent.com/88085974/135052936-a79ff271-2340-4468-9010-4ade5ad60bd7.png)

## bfs

bfs 절차

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다
3. 2번 과정을 수행할 수 없을때까지 반복한다

######################### bfs #########################

from collections import deque as dq


def bfs(graph, start, visited):

  q = dq([start])

  % 시작 노드 방문 처리
  
  visited[start] = 1

  while q:

    v = q.popleft()
    
    print(v, end = '')

    for i in graph[v]:
    
      if not visited[i]:
      
        q.append(i)
        
        visited[i] = 1


graph =[
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]


visited = [0] * 9

bfs(graph, 1, visited)


![image](https://user-images.githubusercontent.com/88085974/135186346-5383f709-c2d5-44fa-946d-3fc43ccd2d80.png)


## problem_001 / 30 min ---- 다시 풀기

![image](https://user-images.githubusercontent.com/88085974/135186646-05da10cc-f7bf-458c-a530-6be7b9ebf0f9.png)

## problem_002 / 30 min

![image](https://user-images.githubusercontent.com/88085974/135202558-2344291e-9bfa-4c7f-a724-6c360c3ead7d.png)



