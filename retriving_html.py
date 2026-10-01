import requests

url = "https://www.flipkart.com/audio-video/headset/earphones/wireless-earphones/true-wireless/~cs-6ef68bc8d283b86730515a8f2c87ff23/pr?sid=0pm,fcn,821,a7x,2si&marketplace=FLIPKART&restrictLocale=true&BU=Mixed"

# Using a fixed, highly-compatible browser header configuration
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand)";v="24", "Google Chrome";v="122"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
}

with requests.Session() as session:
    # Passing the comprehensive headers into the session fetch
    response = session.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    with open("file.html", "w", encoding="utf-8") as file:
        file.write(response.text)

print("HTML saved successfully using requests!")
