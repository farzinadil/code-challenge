import json
import re
from bs4 import BeautifulSoup

# Open the HTML file
with open('files/van-gogh-paintings.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML file
soup = BeautifulSoup(html_content, 'html.parser')

# Find the first painting
first_painting = soup.find(class_='klitem')

if first_painting:
    # Get the name of the painting
    name_element = first_painting.find(class_='kltat')
    name = name_element.text.strip() if name_element else "Name not found"
    
    # Get the date (extensions)
    date_element = first_painting.find(class_='klmeta')
    extensions = [date_element.text.strip()] if date_element else []
    
    # Get the Google link  
    link = 'https://www.google.com' + first_painting.get('href', '') if first_painting.has_attr('href') else None
    
    # Get the thumbnail image URL
    img_element = first_painting.find('img')
    image = None
    if img_element:
        img_id = img_element.get('id')
        if img_id:
            # Find the script that sets the src for this image
            script = soup.find('script', text=re.compile(img_id))
            if script:
                # Get the image data from the script
                match = re.search(r"var s='(data:image/jpeg;base64,[^']+)'", script.string)
                if match:
                    # Remove double backslashes from the image data
                    image = match.group(1).replace('\\', '')

    # Create a dictionary for the painting
    painting_info = {
        "name": name,
        "extensions": extensions,
        "link": link,
        "image": image
    }

    # Print the result as JSON
    print(json.dumps([painting_info], indent=2))

else:
    print("Could not find any paintings.")