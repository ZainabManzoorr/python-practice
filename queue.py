from collections import deque

queue = deque()
queue.append('task1')
queue.append('task2')
print(queue)
print("Initial queue:", list(queue))

print("Processing:", queue.popleft())
print(queue)