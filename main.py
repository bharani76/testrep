import trend_analyzer
import content_generator
import image_generator

def create_viral_post():
    print("--- 🔍 Analyzing Trends ---")
    trend = trend_analyzer.get_trending_topics()
    topic = trend["topic"]
    keywords = trend["keywords"]
    print(f"Targeting: {topic}\n")

    print("--- ✍️ Generating Viral Caption ---")
    caption = content_generator.generate_caption(topic, keywords)
    print(f"Caption:\n{caption}\n")

    print("--- 🎨 Generating Visual Concepts ---")
    image_prompt = image_generator.generate_image_prompt(topic, keywords)
    image_url = image_generator.get_image_url(image_prompt)
    print(f"Image Prompt: {image_prompt}")
    print(f"Image URL: {image_url}\n")

    print("--- ✅ Final Post Package ---")
    print(f"POST CONTENT:\n{caption}\n")
    print(f"POST IMAGE URL: {image_url}")
    print("\n--- DONE ---")

if __name__ == "__main__":
    create_viral_post()
