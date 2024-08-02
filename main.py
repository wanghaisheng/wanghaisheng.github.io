import requests
import zipfile
import io
import os
import json
from fingerprint import arrange_summary,cache_summary
from prepare_astroplate import *
import shutil

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
    print('start to gen finfer print md')
    arrange_summary()
    print('start to combine finfer print md')

    md_path=f"{directory}/changelog.md"
    json_path=f"{directory}/{theme_name}/changelog.json"
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

    full_md_content = combine_yaml_md(md_path, json_path)
    print('start to save final finfer print md')

    # Write combined content to a new file
    combined_md_path = os.path.join(output_directory, f"changelog.mdx")
    with open(combined_md_path, 'w', encoding='utf-8') as combined_file:
        combined_file.write(full_md_content)
    
    print(f"Combined file created: {combined_md_path}")
# Manually manage the event loop in Jupyter Notebook or other environments
def copy_images(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    # List all files in the source folder
    files = os.listdir(source_folder)
    
    for file in files:
        # Check if the file is an image (you can adjust the condition as needed)
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
            # Construct paths
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            
            # Copy the file
            shutil.copyfile(source_path, destination_path)
            print(f"Copied {file} to {destination_folder}")
def move_image(source_file, destination_folder):
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    # Construct destination path
    destination_path = os.path.join(destination_folder, os.path.basename(source_file))
    
    # Move the file, overwriting if it already exists
    shutil.move(source_file, destination_path)
    print(f"Moved {source_file} to {destination_folder}")
if __name__ == "__main__":
    theme='astroplate'
    prefix=None
    get_theme(astroplateurl)

    theme_name='astroplate'
    directory_path = 'content'  # Replace with your parent directory path
    set_astroplate_blogs(directory_path,theme_name,'astroplate/astroplate-main/src/content/blog/english')
    homejson_path = os.path.join(directory_path, theme_name, 'homepage.json')
    homemd_path=os.path.join('astroplate/astroplate-main/src/content/homepage/english', '-index.md')
    
    set_json_to_md_page(homejson_path,homemd_path)
    ctajson_path = os.path.join(directory_path, theme_name, 'cta.json')
    ctamd_path=os.path.join('astroplate/astroplate-main/src/content/sections/english', 'call-to-action.md')
    
    set_json_to_md_page(ctajson_path,ctamd_path)
    
    testimonialjson_path = os.path.join(directory_path, theme_name, 'testimonial.json')
    testimonial_md_path=os.path.join('astroplate/astroplate-main/src/content/sections/english', 'testimonial.md')
    
    set_json_to_md_page(testimonialjson_path,testimonial_md_path)
    print('process fingerprint')

    set_fingerprint(directory_path,theme_name,'astroplate/astroplate-main/src/content/pages/english')
    print('process logo')
    logopath=os.path.join(directory_path,'images', 'logo.png')
    
    logo_output_path=os.path.join('astroplate/astroplate-main/public/images', 'logo.png')
    
    move_image(logopath,logo_output_path)