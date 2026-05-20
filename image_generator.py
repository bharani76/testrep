import urllib.parse

def generate_image_prompt(trend_topic, keywords):
    """
    Generates a detailed prompt for an AI image generator.
    """
    base_prompt = f"A {trend_topic} masterpiece, high quality, {', '.join(keywords)}, professional lighting, detailed textures, 8k resolution, award winning photography."
    return base_prompt

def get_image_url(prompt):
    """
    Uses Pollinations.ai (free, no-key required) to provide a direct image link.
    """
    encoded_prompt = urllib.parse.quote(prompt)
    return f"https://pollinations.ai/p/{encoded_prompt}?width=1080&height=1350&seed=42&model=flux"

if __name__ == "__main__":
    test_trend = "Hyper-realistic Surrealism"
    test_keywords = ["surreal", "dreamy", "4k", "cinematic"]
    prompt = generate_image_prompt(test_trend, test_keywords)
    image_url = get_image_url(prompt)
    print(f"Generated Image Prompt: {prompt}")
    print(f"Generated Image URL: {image_url}")
