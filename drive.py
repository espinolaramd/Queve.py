from list import LinkedListTail


class Queue:
    def __init__(self):
        self.myqueue = LinkedListTail()

    def push(self, data):
        self.myqueue.push_head(data)

    def push_end(self,data):
        self.myqueue.push_end(data)

    def pop(self):
        self.myqueue.pop_head()


myqueve = Queue()
myqueve.push(5)
myqueve.push(10)
myqueve.push_end(10)
print(myqueve.pop())
