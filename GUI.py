import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# ===================== Data Classes =====================

class Node:
    def __init__(self, call):
        self.call = call
        self.next = None


class Call:
    def __init__(self, caller_name):
        self.caller_name = caller_name
        self.arrival_time = datetime.now()

    def __str__(self):
        return f"{self.caller_name}  -  {self.arrival_time.strftime('%H:%M:%S')}"


class CallQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, call):
        new_node = Node(call)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        removed_call = self.head.call
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_call

    def peek(self):
        return self.head.call if self.head else None

    def get_all_calls(self):
        data = []
        ptr = self.head
        while ptr:
            data.append(str(ptr.call))
            ptr = ptr.next
        return data


# ===================== GUI APPLICATION =====================

class CallCenterGUI:
    def __init__(self, root):
        self.queue = CallQueue()
        self.root = root
        self.root.title("Call Center Queue")
        self.root.geometry("550x450")
        self.root.config(bg="#f2f4f7")

        # --------- Title ---------
        tk.Label(
            root,
            text="📞 Call Center Queue System",
            font=("Arial", 18, "bold"),
            bg="#f2f4f7",
            fg="#333"
        ).pack(pady=10)

        # --------- Input Frame ---------
        frame = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge")
        frame.pack(pady=10)

        tk.Label(frame, text="Caller Name:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, padx=10, pady=10)
        self.caller_entry = tk.Entry(frame, width=25, font=("Arial", 12))
        self.caller_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            frame,
            text="Add Call",
            command=self.add_call,
            bg="#4CAF50", fg="white",
            font=("Arial", 12), width=12
        ).grid(row=1, column=0, columnspan=2, pady=10)

        # --------- Queue Display ---------
        tk.Label(root, text="Current Queue:", font=("Arial", 14, "bold"), bg="#f2f4f7").pack()
        self.listbox = tk.Listbox(root, width=45, height=10, font=("Arial", 12))
        self.listbox.pack(pady=5)

        # --------- Buttons ---------
        btn_frame = tk.Frame(root, bg="#f2f4f7")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame, text="Answer Call", command=self.answer_call,
            bg="#2196F3", fg="white", width=15, font=("Arial", 12)
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame, text="Check Wait Time", command=self.check_wait,
            bg="#FF9800", fg="white", width=15, font=("Arial", 12)
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            btn_frame, text="Show First Call", command=self.show_first,
            bg="#9C27B0", fg="white", width=15, font=("Arial", 12)
        ).grid(row=0, column=2, padx=10)

    # -------------------------------------------------------

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for call in self.queue.get_all_calls():
            self.listbox.insert(tk.END, call)

    def add_call(self):
        name = self.caller_entry.get().strip()
        if not name:
            messagebox.showwarning("Warning", "Caller name cannot be empty!")
            return

        self.queue.enqueue(Call(name))
        self.refresh_list()
        self.caller_entry.delete(0, tk.END)

    def answer_call(self):
        call = self.queue.dequeue()
        if call:
            messagebox.showinfo("Answered", f"Agent answered: {call.caller_name}")
        else:
            messagebox.showinfo("Info", "No calls in queue!")
        self.refresh_list()

    def check_wait(self):
        first = self.queue.peek()
        if not first:
            messagebox.showinfo("Info", "No calls waiting.")
            return

        wait_sec = (datetime.now() - first.arrival_time).total_seconds()
        messagebox.showinfo("Wait Time", f"Current waiting time for {first.caller_name}: {wait_sec:.2f} seconds")

    def show_first(self):
        first = self.queue.peek()
        if first:
            messagebox.showinfo("First Call", str(first))
        else:
            messagebox.showinfo("Info", "No calls in queue.")


# ===================== Run App =====================

root = tk.Tk()
app = CallCenterGUI(root)
root.mainloop()
