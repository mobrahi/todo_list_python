# todo_list.py
import os
import json
from datetime import datetime

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []
    
    def save_tasks(self):
        """Save tasks to file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)
    
    def add_task(self, task):
        """Add a new task"""
        self.tasks.append({
            'id': len(self.tasks) + 1,
            'task': task,
            'completed': False,
            'created': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'completed_date': None
        })
        self.save_tasks()
        print(f"✅ Task added: {task}")
    
    def list_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("📭 No tasks found!")
            return
        
        print("\n" + "="*50)
        print("📋 YOUR TO-DO LIST")
        print("="*50)
        
        for task in self.tasks:
            status = "✅" if task['completed'] else "⭕"
            print(f"{status} [{task['id']}] {task['task']}")
            print(f"   📅 Created: {task['created']}")
            if task['completed_date']:
                print(f"   🎉 Completed: {task['completed_date']}")
            print("-"*50)
    
    def complete_task(self, task_id):
        """Mark task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                if not task['completed']:
                    task['completed'] = True
                    task['completed_date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
                    self.save_tasks()
                    print(f"🎉 Task {task_id} marked as completed!")
                else:
                    print(f"⚠️ Task {task_id} is already completed!")
                return
        print(f"❌ Task {task_id} not found!")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted = self.tasks.pop(i)
                # Renumber remaining tasks
                for j, t in enumerate(self.tasks, 1):
                    t['id'] = j
                self.save_tasks()
                print(f"🗑️ Deleted: {deleted['task']}")
                return
        print(f"❌ Task {task_id} not found!")
    
    def show_stats(self):
        """Show task statistics"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task['completed'])
        pending = total - completed
        
        print("\n📊 STATISTICS")
        print("="*30)
        print(f"📋 Total tasks: {total}")
        print(f"✅ Completed: {completed}")
        print(f"⭕ Pending: {pending}")
        if total > 0:
            print(f"📈 Progress: {(completed/total)*100:.1f}%")

def main():
    todo = TodoList()
    
    while True:
        print("\n" + "="*50)
        print("📝 TO-DO LIST MANAGER")
        print("="*50)
        print("1. 📋 List all tasks")
        print("2. ➕ Add a task")
        print("3. ✅ Mark task as complete")
        print("4. 🗑️ Delete a task")
        print("5. 📊 Show statistics")
        print("6. 🚪 Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            todo.list_tasks()
        
        elif choice == '2':
            task = input("Enter your task: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("❌ Task cannot be empty!")
        
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to complete: "))
                todo.complete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == '5':
            todo.show_stats()
        
        elif choice == '6':
            print("👋 Goodbye! Have a productive day!")
            break
        
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()