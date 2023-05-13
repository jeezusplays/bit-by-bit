from bs4 import BeautifulSoup

def extract_text_from_html(html):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html, 'html.parser')

    # Remove unwanted HTML elements
    for element in soup(['script', 'style']):
        element.extract()

    # Get the text content from the remaining elements
    text = soup.get_text(separator=' ',strip=True)

    return text
    # Remove extra whitespace
    # text = ' '.join(text.split())

    

html = "".join(open(file="./test.html").readlines())

# Extract important details from HTML
text = extract_text_from_html(html)

# Print the extracted text
print(text)