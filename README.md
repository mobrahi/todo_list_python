# 📝 Python To-Do List Manager

A feature-rich command-line to-do list application built with Python. Manage your tasks efficiently with this simple yet powerful tool that saves your tasks between sessions!

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## ✨ Features

- **➕ Add Tasks** - Create new tasks with automatic timestamps
- **📋 List Tasks** - View all tasks with their status
- **✅ Complete Tasks** - Mark tasks as done
- **🗑️ Delete Tasks** - Remove tasks you don't need
- **📊 Statistics** - Track your progress
- **💾 Persistent Storage** - Tasks saved in JSON file
- **🔄 Auto-ID** - Automatic task numbering

## 🚀 Quick Start

### Prerequisites
- Python 3.x installed

### Installation & Usage

```bash
# Clone the repository
git clone https://github.com/yourusername/todo-list-python.git

# Navigate to project
cd todo-list-python

# Run the application
python todo_list.py
```
## 🎮 How to Use

When you run the program, you'll see this menu:
```
==================================================
📝 TO-DO LIST MANAGER
==================================================
1. 📋 List all tasks
2. ➕ Add a task
3. ✅ Mark task as complete
4. 🗑️ Delete a task
5. 📊 Show statistics
6. 🚪 Exit
==================================================
Enter your choice (1-6): 
```

### Example Usage

Enter your choice (1-6): 2
Enter your task: Buy groceries
✅ Task added: Buy groceries

Enter your choice (1-6): 1
```
==================================================
📋 YOUR TO-DO LIST
==================================================
⭕ [1] Buy groceries
   📅 Created: 2024-01-15 14:30
--------------------------------------------------
```

## 📁 Data Storage

Tasks are automatically saved in tasks.json:
```
[
  {
    "id": 1,
    "task": "Buy groceries",
    "completed": false,
    "created": "2024-01-15 14:30",
    "completed_date": null
  }
]
```

## 🛠️ Built With

- Python 3.x - Core language
- JSON module - Data persistence
- datetime module - Timestamps
- os module - File operations

## 🎯 Learning Outcomes

This project teaches:

- File I/O operations
- JSON data handling
- CRUD operations (Create, Read, Update, Delete)
- Object-Oriented Programming basics
- Date/time manipulation
- Menu-driven interfaces
- Data persistence

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show your support

Give a ⭐ if this project helped you!

## Features That Can be Added Later

1. GUI Version using Tkinter
2. Web Version using Flask
3. Database using SQLite
4. Due Date Reminders
5. Task Categories
6. Search/Filter Options
