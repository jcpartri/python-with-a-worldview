# collections is part of the Python standard library.
# it has been around for a very long time.
from collections import deque


# Create a Queue class that inherits from deque
class Queue(deque):
    def __init__(self):
        super().__init__()

    # we do need to create our own put() method.
    # if we do not, then we have to use append().
    def put(self, e):
        self.append(e)

    # we also need to create our own get() method.
    # if we do not, then we have to use the built-in
    # popleft() method.
    def get(self):
        return self.popleft()

queue = Queue()
queue.put("e")
queue.put("f")
queue.put("g")
print(queue)
# Output: Queue(['e', 'f', 'g'])
e = queue.get()
print(f"Element removed from queue is: {e}")
print(f"Elements remaining in queue are: {queue}")
