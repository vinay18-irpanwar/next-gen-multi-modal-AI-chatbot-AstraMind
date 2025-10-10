import requests

def generate_image_pollinations(prompt: str) -> str:
    """
    Generate image using Pollinations.ai (free, no API key required).
    Returns the direct image URL.
    """
    try:
        # Pollinations API format
        base_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
        return base_url
    except Exception as e:
        return f"⚠️ Pollinations Error: {e}"
