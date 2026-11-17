
# 1. Add Patient (enqueue)
# 2. Display the next patient to be treated. (display_next) 
# 3. Remove a patient from the queue after treatment. (dequeue)
# 4. Display all waiting patients in priority order(display_all)

class node:
    def __init__(self, pid, name, pr):
        self.patient_id = pid
        self.patient_name = name
        self.priority = pr
        self.next = None


class priorityQueue:
    def __init__(self):
        self.front = None

    # 1. Add Patient (Enqueue)
    def enqueue(self, new_node):

        if self.front == None:
            self.front = new_node
            return

        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        temp = self.front

        while temp.next != None and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # 2. Display Next Patient
    def display_next(self):

        if self.front == None:
            print("No patients waiting!")
            return

        print("Next Patient to be Treated:")
        print("Patient ID:", self.front.patient_id)
        print("Patient Name:", self.front.patient_name)
        print("Priority:", self.front.priority)

    # 3. Remove Patient (Dequeue)
    def dequeue(self):

        if self.front == None:
            print("No patients waiting!")
            return

        temp = self.front
        self.front = self.front.next

        print("Patient Treated:")
        print("Patient ID:", temp.patient_id)
        print("Patient Name:", temp.patient_name)

    # 4. Display All Patients
    def display_all(self):

        if self.front == None:
            print("No patients waiting!")
            return

        temp = self.front

        print("All Waiting Patients:")

        while temp:
            print("Patient ID:", temp.patient_id)
            print("Patient Name:", temp.patient_name)
            print("Priority:", temp.priority)
           
            temp = temp.next


# Create Priority Queue
pq = priorityQueue()

# Add Patients
pq.enqueue(node(101, "Rahul", 3))
pq.enqueue(node(102, "Amit", 1))
pq.enqueue(node(103, "Priya", 2))
pq.enqueue(node(104, "Rohit", 1))
pq.enqueue(node(105, "Sneha", 3))

# Display All Patients
pq.display_all()

# Display Next Patient
print("\nNext Patient:")
pq.display_next()

# Remove Patient After Treatment
print("\nAfter Treatment:")
pq.dequeue()

# Display Remaining Patients
print("\nRemaining Patients:")
pq.display_all()
