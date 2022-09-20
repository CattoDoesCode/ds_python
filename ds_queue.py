# Python program to
# demonstrate queue implementation
# using list

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty


# Initial queue
# ['a', 'b', 'c']
#
# Elements dequeued from queue
# a
# b
# c
#
# Queue after removing elements
# []

# cheat sheet functions
# "from queue import Queue" necessary import

# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with
# maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is
# available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot
# is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.

