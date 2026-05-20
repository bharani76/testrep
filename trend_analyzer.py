import random
try:
    from pytrends.request import TrendReq
    PYTRENDS_AVAILABLE = True
except ImportError:
    PYTRENDS_AVAILABLE = False

def get_trending_topics():
    """
    Fetches trending topics for Instagram.
    Tries to use Google Trends via pytrends if available, else falls back to curated trends.
    """
    if PYTRENDS_AVAILABLE:
        try:
            pytrends = TrendReq(hl='en-US', tz=360)
            # Fetch real-time trending searches for US
            trending_searches_df = pytrends.trending_searches(pn='united_states')
            if not trending_searches_df.empty:
                top_trend = trending_searches_df.iloc[0, 0]
                return {
                    "topic": top_trend,
                    "niche": "News/Viral",
                    "keywords": [top_trend.lower(), "trending", "viral", "2025"]
                }
        except Exception as e:
            print(f"Error fetching real-time trends: {e}")

    # Curated fallbacks based on 2025 research
    trends = [
        {"topic": "Hyper-realistic Surrealism", "niche": "Art", "keywords": ["surreal", "dreamy", "4k", "cinematic"]},
        {"topic": "Cozy Minimalist Lifestyle", "niche": "Lifestyle", "keywords": ["cozy", "minimalist", "aesthetic", "peaceful"]},
        {"topic": "Futuristic Cyberpunk Fashion", "niche": "Fashion", "keywords": ["cyberpunk", "neon", "techwear", "future"]},
        {"topic": "Mindfulness and Mental Health", "niche": "Wellness", "keywords": ["mindfulness", "growth", "mental health", "positivity"]},
        {"topic": "Sustainable Future Cities", "niche": "Environment", "keywords": ["green city", "sustainability", "eco-friendly", "architecture"]}
    ]
    return random.choice(trends)

if __name__ == "__main__":
    trend = get_trending_topics()
    print(f"Current Trending Topic: {trend['topic']}")
    print(f"Keywords: {', '.join(trend['keywords'])}")
