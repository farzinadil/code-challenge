from bs4 import BeautifulSoup

# Read HTML file
with open('files/van-gogh-paintings.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML file
soup = BeautifulSoup(html_content, 'html.parser')

# Find the first painting
first_painting = soup.find(class_='klitem')

# Print the name of the painting
if first_painting:
    name_element = first_painting.find(class_='kltat')
    if name_element:
        print("Name of the first painting:", name_element.text.strip())
    else:
        print("Could not find the name element for the first painting.")
else:
    print("Could not find any paintings.")