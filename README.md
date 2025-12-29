# 🚀 To-Do Manager

[![Flask](https://img.shields.io/badge/Flask-2.3.3-blue.svg)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3.0-lightgrey.svg)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.2-purple.svg)](https://getbootstrap.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A modern, full-stack To-Do Manager application built with Flask, featuring a sleek web interface and powerful RESTful API. Streamline your productivity with intuitive task management, real-time status tracking, and seamless CRUD operations.

## ✨ Features

### 🎯 Core Functionality
- **Complete Task Management**: Create, read, update, and delete tasks with ease
- **Smart Status Tracking**: Toggle between pending and completed states
- **Due Date Management**: Set and track deadlines for better time management
- **Responsive Design**: Beautiful, mobile-friendly interface powered by Bootstrap

### 🔧 Technical Excellence
- **RESTful API**: Comprehensive API for seamless integrations
- **Lightweight Database**: SQLite for fast, file-based storage
- **Robust Logging**: Built-in logging system for monitoring and debugging
- **Comprehensive Testing**: Full test suite with pytest for reliability
- **Modular Architecture**: Clean, maintainable code structure

### 🎨 User Experience
- **Intuitive Web Interface**: User-friendly forms and navigation
- **Real-time Updates**: Instant feedback on all operations
- **Error Handling**: Graceful error messages and validation
- **Accessibility**: WCAG-compliant design principles

## 📁 Project Structure

```
tudo_app/
├── 📄 app.py                 # 🏠 Main Flask application with routes and logic
├── ⚙️ config.py              # 🔧 Configuration settings (database path, etc.)
├── 🗄️ database.py            # 💾 Database connection and initialization utilities
├── 🚀 init_db.py             # 🛠️ Script to initialize the database
├── 📦 requirements.txt       # 📋 Python dependencies
├── 💽 tudo.db                # 🗃️ SQLite database file (auto-generated)
├── 🚫 .gitignore             # 📝 Git ignore rules
├── 📖 README.md              # 📚 Project documentation (this file)
├── 🎨 templates/             # 🌐 HTML templates for web interface
│   ├── 🏠 index.html         # 📋 Home page displaying all tasks
│   ├── ➕ add_task.html      # 📝 Form to add a new task
│   └── ✏️ edit_task.html     # 🔄 Form to edit an existing task
└── 🧪 tests/                 # ✅ Test suite
    ├── 🔧 conftest.py        # ⚙️ Pytest configuration and fixtures
    └── 🔍 test_api.py        # 🧪 API endpoint tests
```

## 🛠️ Installation & Setup

### Prerequisites
- **Python 3.8+**: Ensure you have Python installed
- **Git**: For cloning the repository
- **Virtual Environment**: Recommended for dependency management

### Quick Start

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/harshit843/tudo_app>
   cd tudo_app
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**
   ```bash
   python init_db.py
   ```

5. **Launch the Application**
   ```bash
   python app.py
   ```

🎉 **Your To-Do Manager is now running at** `http://localhost:5000`!

## 📖 Usage Guide

### 🌐 Web Interface

Navigate to `http://localhost:5000` to access the web interface:

- **🏠 Dashboard (`/`)**: View all your tasks in an organized table
- **➕ Add Task (`/add`)**: Create new tasks with title, description, and due date
- **✏️ Edit Task (`/edit/<task_id>`)**: Modify existing tasks
- **🗑️ Delete Task**: Remove tasks with confirmation prompts

### 🔌 API Reference

The application provides a comprehensive RESTful API:

#### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | Retrieve all tasks |
| GET | `/api/tasks/<id>` | Get specific task |
| POST | `/api/tasks` | Create new task |
| PUT | `/api/tasks/<id>` | Update existing task |
| DELETE | `/api/tasks/<id>` | Delete task |

#### 📝 Create a Task
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project proposal",
    "description": "Draft and review the Q4 project proposal",
    "due_date": "2024-01-15",
    "status": "pending"
  }'
```

#### 📋 Retrieve Tasks
```bash
# Get all tasks
curl http://localhost:5000/api/tasks

# Get specific task
curl http://localhost:5000/api/tasks/1
```

#### 🔄 Update a Task
```bash
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated project proposal",
    "status": "completed"
  }'
```

#### 🗑️ Delete a Task
```bash
curl -X DELETE http://localhost:5000/api/tasks/1
```

## 🧪 Testing

Run the comprehensive test suite to ensure everything works perfectly:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_api.py
```

## ⚙️ Configuration

### Database Configuration
- **Location**: Configured in `config.py`
- **Default Path**: `todo.db` in project root
- **Type**: SQLite (lightweight, file-based)

### Logging Configuration
- **Level**: INFO (configurable in `app.py`)
- **Output**: Console logging
- **Format**: Timestamp, level, and message

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the Repository**
2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make Your Changes**
4. **Add Tests** for new functionality
5. **Run Tests**
   ```bash
   pytest
   ```
6. **Commit Changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
7. **Push to Branch**
   ```bash
   git push origin feature/amazing-feature
   ```
8. **Open Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Write comprehensive tests for new features
- Update documentation for API changes
- Ensure all tests pass before submitting

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🏗️ Architecture & Technologies

### Backend Stack
- **Flask**: Lightweight WSGI web application framework
- **SQLite**: Embedded relational database
- **SQLAlchemy**: (Potential future enhancement for ORM)

### Frontend Stack
- **Bootstrap 5**: Responsive CSS framework
- **Jinja2**: Server-side templating engine
- **HTML5**: Semantic markup
- **CSS3**: Modern styling

### Development Tools
- **pytest**: Testing framework
- **Git**: Version control
- **Virtualenv**: Python environment management

## 🚀 Future Enhancements

- [ ] User authentication and authorization
- [ ] Task categories and tags
- [ ] Email notifications for due dates
- [ ] API rate limiting
- [ ] Task prioritization system
- [ ] Export tasks to CSV/PDF
- [ ] Dark mode theme
- [ ] Multi-language support

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/harshit843/tudo_app/issues) page
2. Create a new issue with detailed information
3. Include error messages, steps to reproduce, and your environment details

## 🙏 Acknowledgments

- **Flask Community**: For the amazing web framework
- **Bootstrap Team**: For the beautiful UI components
- **SQLite**: For reliable data storage
- **Open Source Community**: For the tools that make development possible

---

<div align="center">

**Built with ❤️ using Flask and modern web technologies**

⭐ Star this repo if you find it helpful!

[Report Bug](https://github.com/harshit843/tudo_app/issues) • [Request Feature](https://github.com/harshit843/tudo_app)

</div>
