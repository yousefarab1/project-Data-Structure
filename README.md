# 📞 Basic Call Center Queue System  
(Basic Queue using Singly Linked List)

## 📌 Project Description
This project simulates a **basic call center system** where incoming customer calls are handled in the order they arrive, following the **First-In, First-Out (FIFO)** principle.

The system is implemented using a **Basic Queue**, with a **Singly Linked List** as the underlying data structure to demonstrate a dynamic queue implementation.

---

## 🧱 Data Structures Used

### 1️⃣ Basic Queue
- Used to store incoming customer calls.
- New calls are added to the back of the queue (**Enqueue**).
- Available agents answer calls from the front of the queue (**Dequeue**).
- Enforces the **FIFO** rule.

### 2️⃣ Singly Linked List
- Used to implement the queue dynamically.
- Insertion is performed at the **tail** of the list.
- Deletion is performed from the **head** of the list.
- Demonstrates how queues can be implemented without fixed-size arrays.

---

## ⚙️ Key Features

### 📥 New Call (Arrival)
- Creates a new call object.
- Adds the call to the queue using an **enqueue** operation (insert at tail).

### 📤 Agent Answers (Service)
- Removes and serves the oldest call in the queue.
- Uses a **dequeue** operation (delete from head).

### ⏱️ Check Wait Time
- Calculates how long the call at the front of the queue has been waiting.
- Based on the call’s arrival time.

---

## 🎯 Project Objectives
- Understand the practical use of the **Queue** data structure.
- Apply **Singly Linked List** concepts in a real-world scenario.
- Demonstrate enqueue and dequeue operations clearly.
- Connect data structures with real system simulations.

---

## 🛠 Possible Extensions
- Implement a Priority Queue.
- Support multiple agents.
- Display all waiting calls.
- Calculate average waiting time.

---

## 👨‍💻 Author
**Yousef Arabi**  
Data Structures Project
