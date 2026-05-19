import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def generate_caption(trend_topic, keywords):
    """
    Generates a viral Instagram caption using Hugging Face Inference API.
    If no API key is provided, it falls back to a template-based generation.
    """
    prompt = f"Create a viral Instagram caption for the topic '{trend_topic}' using these keywords: {', '.join(keywords)}. The caption should be engaging, include a call to action, and some relevant emojis. Keep it under 200 characters."

    if HUGGINGFACE_API_KEY:
        # Use a more capable model for viral content
        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

        try:
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt, "parameters": {"max_new_tokens": 100}})
            response.raise_for_status()
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                generated_text = result[0].get("generated_text", "")
                # Clean up response: remove prompt and handle formatting
                if generated_text.startswith(prompt):
                    generated_text = generated_text[len(prompt):].strip()

                # If the AI returned an empty or too short string, use fallback
                if len(generated_text) > 20:
                    return generated_text
        except Exception as e:
            print(f"Error calling Hugging Face API: {e}")

    # Advanced Fallback template with psychological triggers
    hooks = [
        f"POV: You just discovered {trend_topic}. ✨",
        f"Is it just me, or is {trend_topic} taking over? 🚀",
        f"The future is here: {trend_topic}. 🌎",
        f"POV: {keywords[0].capitalize()} is the vibe we all needed. 🧘"
    ]
    hook = random.choice(hooks) if 'random' in globals() else hooks[0]

    import random # ensure random is available
    hook = random.choice(hooks)

    return f"{hook}\n\nObsessed with the {keywords[1]} energy lately. {keywords[2].capitalize()} goals! 🔥\n\nTag someone who needs to see this! 👇\n\n#{' #'.join(keywords)} #viral #2025 #trending"

if __name__ == "__main__":
    test_trend = "Hyper-realistic Surrealism"
    test_keywords = ["surreal", "dreamy", "4k", "cinematic"]
    caption = generate_caption(test_trend, test_keywords)
    print(f"Generated Caption:\n{caption}")
