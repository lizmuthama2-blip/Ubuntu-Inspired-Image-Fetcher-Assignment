import requests
import os
from urllib.parse import urlparse
def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    url = input("Please enter the image URL: ").strip()
    try:
        os.makedirs("Fetched_Images", exist_ok=True)
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or "." not in filename:
            filename = "downloaded_image.jpg"
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, 'wb') as file:
            file.write(response.content)
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}"
if __name__ == "__main__":
    main()
