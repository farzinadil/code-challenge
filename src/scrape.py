import os
import json
from bs4 import BeautifulSoup
import configparser

from image_extractor import extract_content


# Read the HTML file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
config = configparser.ConfigParser()
config.read(os.path.join(parent_dir, 'files', 'config.ini'))
file_name = config['DEFAULT']['file']
html_file = os.path.join(parent_dir, 'files', file_name)

with open(html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all carousel items
carousel_items = soup.find_all(class_='klitem-tr')

# List to store all carousel item information
all_carousel_items = []

for carousel_item in carousel_items:
    if carousel_item.name == 'div':
        '''
            It is probably better to use regex; treat the entire klitem-tr 
            as a string, and look for aria-label, title, href, etc.
        '''
        carousel_item = carousel_item.find('a', attrs={'aria-label': True})
    # Extract the name of the carousel item
    label = carousel_item.get('aria-label', None)
    name = label if label else None

    
    # Extract the date (extensions)
    title = carousel_item.get('title', None)
    if title != name:
        title_and_extension = title.replace('(', '').replace(')', '')
        title_name, extension = title_and_extension.rsplit(' ', 1)
        extensions = extension
    else:
        extensions = None


    #date_element = carousel_item.find(class_='klmeta')
    #extensions = date_element.text.strip() if date_element else ""
    
    # Extract the Google link  
    link = 'https://www.google.com' + carousel_item.get('href', '') if carousel_item.has_attr('href') else None
    
    # Extract the thumbnail image URL
    img_element = carousel_item.find('img')
    image = None
    if img_element and img_element.has_attr('id'):
        img_id = img_element['id']
        image = extract_content(html_file, img_id)

    # Create a dictionary for the carousel item and add it to the list
    carousel_item_info = {
        "name": name,
    }
    
    # Only include extensions if they exist and are not empty
    if extensions:
        carousel_item_info["extensions"] = [extensions]
    
    # Add the remaining items
    carousel_item_info.update({
        "link": link,
        "image": image
    })
    
    all_carousel_items.append(carousel_item_info)

# Save Output
output_file = os.path.join(parent_dir, 'files', 'generated_array.json')
with open(output_file, 'w', encoding='utf-8') as json_file:
    json_file.write('"artworks": ')
    json.dump(all_carousel_items, json_file, indent=2, ensure_ascii=False)

print(f"Successfully extracted {len(all_carousel_items)} carousel items. Data saved to generated_array.json")