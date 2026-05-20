from flask import Flask, render_template_string
import sqlite3
import os

app = Flask(__name__)
DB_FILE = "posts_history.db"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Instagram Agent Dashboard</title>
    <style>
        body { font-family: sans-serif; margin: 40px; background: #f4f4f4; }
        .container { max-width: 1000px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #eee; }
        .status-success { color: green; font-weight: bold; }
        .status-failed { color: red; font-weight: bold; }
        .image-preview { width: 100px; border-radius: 4px; }
        .caption { font-size: 0.9em; color: #666; max-width: 300px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📱 Instagram Agentic Dashboard</h1>
        <p>Monitoring automated post generation and publishing history.</p>

        <table>
            <thead>
                <tr>
                    <th>Timestamp</th>
                    <th>Topic</th>
                    <th>Caption</th>
                    <th>Image</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {% for post in posts %}
                <tr>
                    <td>{{ post[0] }}</td>
                    <td>{{ post[1] }}</td>
                    <td><div class="caption">{{ post[2] }}</div></td>
                    <td>
                        {% if post[3] %}
                        <a href="{{ post[3] }}" target="_blank">
                            <img src="{{ post[3] }}" class="image-preview">
                        </a>
                        {% endif %}
                    </td>
                    <td>
                        <span class="status-{{ post[4]|lower }}">{{ post[4] }}</span>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

def get_posts():
    if not os.path.exists(DB_FILE):
        return []
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM posts ORDER BY timestamp DESC")
    posts = c.fetchall()
    conn.close()
    return posts

@app.route("/")
def index():
    posts = get_posts()
    return render_template_string(HTML_TEMPLATE, posts=posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
