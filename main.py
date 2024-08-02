import requests
import zipfile
import io
import os
import json
from fingerprint import arrange_summary,cache_summary
from prepare_astroplate import *
# URL of the ZIP file
astroplateurl = "https://github.com/zeon-studio/astroplate/archive/refs/heads/main.zip"

# Directory where you want to extract the contents
extract_to_directory = "astroplate"

# Ensure the directory exists or create it if it doesn't
os.makedirs(extract_to_directory, exist_ok=True)
def get_theme(url):
    # Download the ZIP file
    response = requests.get(url)
    if response.status_code == 200:
        # Open the ZIP file
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            # Extract all the contents to the specified directory
            zip_ref.extractall(extract_to_directory)
        print(f"Successfully extracted files to '{extract_to_directory}'.")
    else:
        print(f"Failed to download ZIP file. Status code: {response.status_code}")
def set_blog(directory,theme_name):
    set_astroplate_blogs(directory+'/blogs',theme_name)

def set_fingerprint(directory,theme_name,output_directory):
    arrange_summary()
    md_path="content/changelog.md"
    json_path="content/astroplate/changelog.json"
    if os.path.exists(json_path):
        print('finger print meta json is here')
    else:
        print('finger print meta json is not here')
        return
    if os.path.exists(md_path):
        print('finger print md_path is here')
    else:
        print('finger print md_path is not here')
        return

    full_md_content = construct_full_md(md_path, json_path)
    
    # Write combined content to a new file
    combined_md_path = os.path.join(output_directory, f"changelog.mdx")
    with open(combined_md_path, 'w', encoding='utf-8') as combined_file:
        combined_file.write(full_md_content)
    
    print(f"Combined file created: {combined_md_path}")
# Manually manage the event loop in Jupyter Notebook or other environments
if __name__ == "__main__":
    theme='astroplate'
    prefix=None
    get_theme(astroplateurl)

    theme_name='astroplate'
    directory_path = 'content'  # Replace with your parent directory path
    set_astroplate_blogs(directory_path,theme_name,'astroplate/astroplate-main/src/content/blog/english')
    set_homepage(directory_path,theme_name,'astroplate/astroplate-main/src/content/homepage/english')
    set_fingerprint(directory_path,theme_name,'astroplate/astroplate-main/src/content/pages/english')