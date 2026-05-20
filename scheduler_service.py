import schedule
import time
import random
import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv

import trend_analyzer
import content_generator
import image_generator
import publisher

load_dotenv()

POSTS_PER_DAY = int(os.getenv("POSTS_PER_DAY", "4"))
DB_FILE = "posts_history.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (timestamp TEXT, topic TEXT, caption TEXT, image_url TEXT, status TEXT)''')
    conn.commit()
    conn.close()

def log_post(topic, caption, image_url, status):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO posts VALUES (?, ?, ?, ?, ?)",
              (datetime.now().isoformat(), topic, caption, image_url, status))
    conn.commit()
    conn.close()

def job():
    print(f"\n--- 🚀 Starting Scheduled Post Generation: {datetime.now()} ---")
    try:
        # 1. Analyze Trends
        trend = trend_analyzer.get_trending_topics()
        topic = trend["topic"]
        keywords = trend["keywords"]

        # 2. Generate Content
        caption = content_generator.generate_caption(topic, keywords)

        # 3. Generate Image
        image_prompt = image_generator.generate_image_prompt(topic, keywords)
        image_url = image_generator.get_image_url(image_prompt)

        # 4. Publish
        result = publisher.publish_to_instagram(image_url, caption)

        status = "Success" if result else "Failed"
        log_post(topic, caption, image_url, status)

        print(f"--- ✅ Job Completed: {status} ---\n")
    except Exception as e:
        print(f"Error in scheduled job: {e}")
        log_post("ERROR", str(e), "", "Error")

def run_scheduler():
    init_db()
    print(f"Scheduler started. Planning {POSTS_PER_DAY} posts per day.")

    # Simple strategy: Divide 24 hours by POSTS_PER_DAY
    interval = 24 // POSTS_PER_DAY
    for i in range(POSTS_PER_DAY):
        hour = (i * interval) % 24
        # Add some random minutes to look more human
        minute = random.randint(0, 59)
        time_str = f"{hour:02d}:{minute:02d}"
        schedule.every().day.at(time_str).do(job)
        print(f"Scheduled post at {time_str}")

    # Immediate trigger for testing if needed
    # job()

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    run_scheduler()
