class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 and self.rear == -1
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self,item):
        if self.is_full():
            print ("Queue is full. Unable to enqueue.")
            return
        
        if self.is_empty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity  # !
        self.queue[self.rear] = item  # !
    
    def dequeue(self):
        if self.is_empty():
            print ("Queue is empty. Unable to dequeue.")
            return None
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else: 
            self.front = (self.front + 1) % self.capacity
        item = self.queue[self.front]  # !

        return item
    
    def display(self):
        if self.is_empty():
            print ("Queue is empty.")
            return
        
        current = self.front  # !
        while current != self.rear:
            print (self.queue[current], end=" ")
            '''
            指定 "end" 的值，使多個輸出以(此處為空格)分隔，並呈現在同一行
            '''
            current = (current + 1) % self.capacity
        print (self.queue[self.rear])

queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.display()
print ("Dequeued item:", queue.dequeue())
print ("Dequeued item:", queue.dequeue())
queue.display()