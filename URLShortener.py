import string
import random

def generate_short_url(url_length=6):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(url_length))
    return short_url

def main():
    print("Welcome to the URL Shortener!")
    original_url = input("Enter the original URL: ")
    short_url = generate_short_url()
    print(f"Short URL: https://short.com/{short_url}")

if __name__ == "__main__":
    main()
