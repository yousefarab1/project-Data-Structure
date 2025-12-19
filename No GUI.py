import time
from datetime import datetime

class Node:
    def __init__(self, call):
        self.call = call
        self.next = None

class Call:
    def __init__(self, caller_name):
        self.caller_name = caller_name
        self.arrival_time = datetime.now()

    def __str__(self):
        return f"Caller: {self.caller_name}, Arrived: {self.arrival_time.strftime('%H:%M:%S')}"

class CallQueue:
    def __init__(self):
        self.head = None  # Front of queue
        self.tail = None  # Back of queue

    def enqueue(self, call):
        new_node = Node(call)
        if self.tail is None:   # Queue empty
            self.head = self.tail = new_node
        else:   
            self.tail.next = new_node
            self.tail = new_node
        print(f"[ENQUEUE] Call added: {call.caller_name}")

    def dequeue(self):
        if self.head is None:
            print("[DEQUEUE] No calls in queue.")
            return None
        removed_call = self.head.call
        self.head = self.head.next
        if self.head is None:  # Queue became empty
            self.tail = None
        print(f"[DEQUEUE] Agent answered: {removed_call.caller_name}")
        return removed_call
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.call
    
    def check_wait_time(self):
        if self.head is None:
            print("No calls waiting.")
            return
        now = datetime.now()
        wait_seconds = (now - self.head.call.arrival_time).total_seconds()
        print(f"Current waiting time for {self.head.call.caller_name}: {wait_seconds:.2f} seconds")

queue = CallQueue()
while True:
    print("\n===== Call Center Menu =====")
    print("1. New Call (Enqueue)")
    print("2. Agent Answers Call (Dequeue)")
    print("3. Check Wait Time")
    print("4. Show First Call")
    print("5. Exit")
    choice = input("Select an option: ")
    if choice == "1":
        name = input("Enter caller name: ")
        queue.enqueue(Call(name))
    elif choice == "2":
        queue.dequeue()
    elif choice == "3":
        queue.check_wait_time()
    elif choice == "4":
        first_call = queue.peek()
        if first_call:
            print("First call in queue:", first_call)
        else:
            print("No calls in queue.")
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
        