from flask import Flask, request, jsonify, render_template, redirect, url_for
import logging
from database import get_db_connection, init_db


def create_app():
    app = Flask(__name__)

    # ---------------- LOGGING SETUP ----------------
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Initialize DB
    init_db()

    # ---------------- API ROUTES ----------------

    @app.route("/api/tasks", methods=["POST"])
    def create_task():
        try:
            data = request.get_json()

            title = data.get("title")
            description = data.get("description", "")
            due_date = data.get("due_date", "")
            status = data.get("status", "pending")

            if not title:
                return jsonify({"error": "Title is required"}), 400

            conn = get_db_connection()
            conn.execute(
                "INSERT INTO tasks (title, description, due_date, status) VALUES (?, ?, ?, ?)",
                (title, description, due_date, status)
            )
            conn.commit()
            conn.close()

            return jsonify({"message": "Task created successfully"}), 201

        except Exception as e:
            logging.error(str(e))
            return jsonify({"error": "Internal Server Error"}), 500


    @app.route("/api/tasks", methods=["GET"])
    def get_tasks():
        conn = get_db_connection()
        tasks = conn.execute("SELECT * FROM tasks").fetchall()
        conn.close()
        return jsonify([dict(task) for task in tasks]), 200


    @app.route("/api/tasks/<int:task_id>", methods=["GET"])
    def get_task(task_id):
        conn = get_db_connection()
        task = conn.execute(
            "SELECT * FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
        conn.close()

        if task is None:
            return jsonify({"error": "Task not found"}), 404

        return jsonify(dict(task)), 200


    @app.route("/api/tasks/<int:task_id>", methods=["PUT"])
    def update_task(task_id):
        data = request.get_json()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tasks
            SET title = ?, description = ?, due_date = ?, status = ?
            WHERE id = ?
        """, (
            data.get("title"),
            data.get("description"),
            data.get("due_date"),
            data.get("status"),
            task_id
        ))
        conn.commit()

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({"error": "Task not found"}), 404

        conn.close()
        return jsonify({"message": "Task updated successfully"}), 200


    @app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
    def delete_task(task_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({"error": "Task not found"}), 404

        conn.close()
        return jsonify({"message": "Task deleted successfully"}), 200


    # ---------------- WEB ROUTES ----------------

    @app.route("/")
    def home():
        conn = get_db_connection()
        tasks = conn.execute("SELECT * FROM tasks").fetchall()
        conn.close()
        return render_template("index.html", tasks=tasks)


    @app.route("/add", methods=["GET", "POST"])
    def add_task():
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            due_date = request.form["due_date"]

            conn = get_db_connection()
            conn.execute(
                "INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)",
                (title, description, due_date)
            )
            conn.commit()
            conn.close()

            return redirect(url_for("home"))

        return render_template("add_task.html")


    # ---------------- EDIT TASK (UI) ----------------
    @app.route("/edit/<int:task_id>", methods=["GET", "POST"])
    def edit_task_ui(task_id):
        conn = get_db_connection()
        task = conn.execute(
            "SELECT * FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()

        if task is None:
            conn.close()
            return "Task not found", 404

        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            due_date = request.form["due_date"]
            status = request.form["status"]

            conn.execute("""
                UPDATE tasks
                SET title = ?, description = ?, due_date = ?, status = ?
                WHERE id = ?
            """, (title, description, due_date, status, task_id))

            conn.commit()
            conn.close()
            return redirect(url_for("home"))

        conn.close()
        return render_template("edit_task.html", task=task)


    # ---------------- DELETE TASK (UI) ----------------
    @app.route("/delete-ui/<int:task_id>", methods=["POST"])
    def delete_task_ui(task_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        return redirect(url_for("home"))

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
