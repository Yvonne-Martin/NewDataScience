# implementing queues using collection.deque
# adding elements ina a queue

from collections import deque
myQueue = deque()
myQueue.append("yvonne")
myQueue.append('Leila')
myQueue.append('Martin')
print(myQueue)#output:deque(['yvonne', 'Leila', 'Martin'])

# removing elements
print(myQueue.popleft())
print(myQueue.popleft())
# Queue after removing elements
print(myQueue)#output: deque([])

print(type(myQueue))#<class 'collections.deque'>

#implementataion using queue.Queue

from queue import Queue
a=Queue(maxsize=3)
print(a.qsize())
a.put("yvonne")
a.put("martin")
a.put("yvonne")
print(a.full())#check if the queue is full
print(a.get())
print(a.get())
print(a.get())
print(a.empty())#checks if the queue is empty
print(a.full())#check if the stack is still full after removing elements