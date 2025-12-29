# To-Do Manager

A simple and efficient To-Do Manager application built with Flask, featuring both a RESTful API and a user-friendly web interface. Manage your tasks seamlessly with CRUD operations, status tracking, and due dates.

## Features

- **Task Management**: Create, read, update, and delete tasks.
- **Status Tracking**: Mark tasks as pending or completed.
- **Due Dates**: Assign and track due dates for tasks.
- **RESTful API**: Full API support for integration with other applications.
- **Web Interface**: Intuitive web UI built with Bootstrap for easy task management.
- **Database**: SQLite for lightweight, file-based storage.
- **Logging**: Built-in logging for monitoring and debugging.
- **Testing**: Comprehensive test suite using pytest.

## Project Structure

```
tudo_app/
├── app.py                 # Main Flask application with routes and logic
├── config.py              # Configuration settings (e.g., database path)
├── database.py            # Database connection and initialization utilities
├── init_db.py             # Script to initialize the database
├── requirements.txt       # Python dependencies
├── tudo.db                # SQLite database file (auto-generated)
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation (this file)
├── templates/             # HTML templates for web interface
│   ├── index.html         # Home page displaying all tasks
│   ├── add_task.html      # Form to add a new task
│   └── edit_task.html     # Form to edit an existing task
└── tests/                 # Test suite
    ├── conftest.py        # Pytest configuration and fixtures
    └── test_api.py        # API endpoint tests
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd tudo_app
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

## Usage

### Running the Application

Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`.

### Web Interface

- **Home Page** (`/`): View all tasks in a table format.
- **Add Task** (`/add`): Form to create a new task.
- **Edit Task** (`/edit/<task_id>`): Form to update an existing task.
- **Delete Task**: Delete a task directly from the home page.

### API Endpoints

The application provides a RESTful API for programmatic access:

- **GET /api/tasks**: Retrieve all tasks.
- **GET /api/tasks/<task_id>**: Retrieve a specific task by ID.
- **POST /api/tasks**: Create a new task.
  - Body: `{"title": "Task Title", "description": "Description", "due_date": "YYYY-MM-DD", "status": "pending"}`
- **PUT /api/tasks/<task_id>**: Update an existing task.
  - Body: `{"title": "Updated Title", "description": "Updated Description", "due_date": "YYYY-MM-DD", "status": "completed"}`
- **DELETE /api/tasks/<task_id>**: Delete a task by ID.

#### Example API Usage

Create a task:
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, bread, eggs", "due_date": "2023-12-31"}'
```

Get all tasks:
```bash
curl http://localhost:5000/api/tasks
```

## Testing

Run the test suite using pytest:
```bash
pytest
```

The tests cover API endpoints and ensure the application functions correctly.

## Configuration

- **Database Path**: Configured in `config.py`. Defaults to `todo.db` in the project root.
- **Logging**: Configured in `app.py` with INFO level logging to the console.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Make your changes and add tests.
4. Run tests: `pytest`.
5. Commit your changes: `git commit -am 'Add new feature'`.
6. Push to the branch: `git push origin feature-name`.
7. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Technologies Used

- **Flask**: Web framework for Python.
- **SQLite**: Lightweight database.
- **Bootstrap**: CSS framework for responsive web design.
- **pytest**: Testing framework.
- **Jinja2**: Templating engine (included with Flask).
