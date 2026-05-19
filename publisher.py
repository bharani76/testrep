import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

IG_USER_ID = os.getenv("IG_USER_ID")
IG_ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN")
DRY_RUN = os.getenv("DRY_RUN", "True").lower() == "true"

def publish_to_instagram(image_url, caption):
    """
    Publishes a post to Instagram using the Graph API.
    Follows the 2-step process:
    1. Create Media Container
    2. Publish Media Container
    """
    if DRY_RUN:
        print(f"[DRY RUN] Publishing to Instagram...")
        print(f"[DRY RUN] Image: {image_url}")
        print(f"[DRY RUN] Caption: {caption}")
        return {"id": "DRY_RUN_SUCCESS_ID"}

    if not IG_USER_ID or not IG_ACCESS_TOKEN:
        print("Error: Instagram credentials missing in environment.")
        return None

    try:
        # Step 1: Create Media Container
        container_url = f"https://graph.facebook.com/v25.0/{IG_USER_ID}/media"
        params = {
            "image_url": image_url,
            "caption": caption,
            "access_token": IG_ACCESS_TOKEN
        }

        response = requests.post(container_url, params=params)
        response.raise_for_status()
        container_id = response.json().get("id")

        if not container_id:
            print("Error: Failed to get container ID.")
            return None

        # Wait a bit for the container to be ready
        print(f"Container created (ID: {container_id}). Waiting for processing...")
        time.sleep(5)

        # Step 2: Publish Media Container
        publish_url = f"https://graph.facebook.com/v25.0/{IG_USER_ID}/media_publish"
        publish_params = {
            "creation_id": container_id,
            "access_token": IG_ACCESS_TOKEN
        }

        publish_response = requests.post(publish_url, params=publish_params)
        publish_response.raise_for_status()

        print("Post published successfully!")
        return publish_response.json()

    except Exception as e:
        print(f"Error publishing to Instagram: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"Response: {e.response.text}")
        return None

if __name__ == "__main__":
    # Test call
    result = publish_to_instagram("https://example.com/image.jpg", "Hello Instagram! #test")
    print(result)
