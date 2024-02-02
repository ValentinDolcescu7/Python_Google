import requests

def save_html_to_file(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"HTML content has been successfully scraped and saved to '{filename}'.")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    target_url = "https://lpf.ro/"
    save_html_to_file(target_url, "scraped_articles.txt")
