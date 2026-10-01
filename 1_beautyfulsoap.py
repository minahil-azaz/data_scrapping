from bs4 import BeautifulSoup

# Open and safely read your local HTML file
with open("file1.html", "r", encoding="utf-8") as file:
    html_content = file.read()
    
    # Parse the text string using the HTML parser
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Print the formatted, clean HTML structure to your console
    print(soup.prettify())
