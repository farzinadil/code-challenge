# image_extractor.py

import re

def extract_content(file_path, search_string):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find all occurrences of _setImagesSrc
    all_matches = list(re.finditer(r"_setImagesSrc", content))
    
    # Find the occurrence of the search string
    search_match = re.search(f"\['{search_string}'\]", content)
    
    if search_match and all_matches:
        # Find the _setImagesSrc that immediately precedes the search string
        preceding_match = next((m for m in reversed(all_matches) if m.start() < search_match.start()), None)
        
        if preceding_match:
            start_index = preceding_match.start()
            end_index = search_match.start()
            
            # Extract the content between the preceding _setImagesSrc and the search string
            matched_content = content[start_index:end_index]
            
            # Extract the image data
            image_data_match = re.search(r"s='(.*?)'", matched_content)
            if image_data_match:
                result = image_data_match.group(1)
                
                # Remove backslashes after the last slash
                last_slash_index = result.rfind('/')
                if last_slash_index != -1:
                    before_last_slash = result[:last_slash_index + 1]
                    after_last_slash = result[last_slash_index + 1:].replace('\\', '')
                    result = before_last_slash + after_last_slash
                
                return result
    
    return None