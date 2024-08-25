from bs4 import BeautifulSoup

# Read HTML file
with open('files/van-gogh-paintings.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML file
soup = BeautifulSoup(html_content, 'html.parser')

# Find the first painting
first_painting = soup.find(class_='klitem')

if first_painting:
    # Get the name of the painting
    name_element = first_painting.find(class_='kltat')
    if name_element:
        name = name_element.text.strip()
        print("Name of the first painting:", name)
    else:
        print("Missing painting name")
    
    # Get the date 
    date_element = first_painting.find(class_='klmeta')
    if date_element:
        date = date_element.text.strip()
        extensions = [date]  # Put the date in an array
        print("Extensions (date):", extensions)
    else:
        print("Missing painting date")
    
    # Extract the Google link
    link_element = first_painting.find('a')
    if link_element:
        link = link_element.get('href')
        if link.startswith('/'):
            link = 'https://www.google.com' + link
        print("Google link:", link)
    else:
        print("Missing painting link")
else:
    print("Could not find painting")