graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue   open tromg ds thực hiện

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]: #nei là biến liền kề với s
      if neighbour not in visited: # nếu nei không trong visit
        visited.append(neighbour) #thêm
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')
# đầu tiên thêm đỉnh A vào ds visit, nếu que rỗng thì nó tb tkiem thất bại
còn k thì