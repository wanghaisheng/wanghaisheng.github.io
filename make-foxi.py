import requests
import zipfile
import io
import os
import json
from fingerprint import arrange_summary,cache_summary
from prepare_astroplate import *
import shutil

# URL of the ZIP file
themedownloadurl = "https://github.com/oxygenna-themes/foxi-astro-theme/archive/refs/heads/main.zip"

# Directory where you want to extract the contents
extract_to_directory = "foxi-astro-theme"

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
    
    # 检查文件是否存在
    if os.path.exists(combined_md_path):
        print(f"The file {combined_md_path} already exists and will be overwritten.")
        # 如果需要，可以在这里添加询问用户是否覆盖的逻辑
    
    with open(combined_md_path, 'w', encoding='utf-8') as combined_file:
        combined_file.write(full_md_content)
    
    print(f"Combined file created: {combined_md_path}")

def copy_images(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    else:
        # If the destination folder exists, find a new name for it
        base_folder, folder_name = os.path.split(destination_folder)
        folder_number = 1
        new_folder_name = f"{folder_name}_copy{folder_number}"
        new_destination_folder = os.path.join(base_folder, new_folder_name)
        
        # Keep finding new names until an available one is found
        while os.path.exists(new_destination_folder):
            folder_number += 1
            new_folder_name = f"{folder_name}_copy{folder_number}"
            new_destination_folder = os.path.join(base_folder, new_folder_name)
        
        # Rename the existing destination folder
        shutil.move(destination_folder, new_destination_folder)
        print(f"Existing destination folder renamed to {new_destination_folder}")
        
        # Now create the new destination folder
        os.makedirs(destination_folder)
    
    # List all files in the source folder
    files = os.listdir(source_folder)
    
    for file in files:
        # Check if the file is an image (you can adjust the condition as needed)
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Construct paths
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            
            # Copy the file
            shutil.copyfile(source_path, destination_path)
            print(f"Copied {file} to {destination_folder}")

# Example usage:
# copy_images('/path/to/source', '/path/to/destination')



def copy_json_files_rename(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    else:
        # If the destination folder exists, find a new name for it
        base_folder, folder_name = os.path.split(destination_folder)
        folder_number = 1
        new_folder_name = f"{folder_name}_copy{folder_number}"
        new_destination_folder = os.path.join(base_folder, new_folder_name)
        
        # Keep finding new names until an available one is found
        while os.path.exists(new_destination_folder):
            folder_number += 1
            new_folder_name = f"{folder_name}_copy{folder_number}"
            new_destination_folder = os.path.join(base_folder, new_folder_name)
        
        # Rename the existing destination folder
        shutil.move(destination_folder, new_destination_folder)
        print(f"Existing destination folder renamed to {new_destination_folder}")
        
        # Now create the new destination folder
        os.makedirs(destination_folder)
    
    # List all files in the source folder
    files = os.listdir(source_folder)
    
    for file in files:
        # Check if the file is a JSON file
        if file.lower().endswith('.json'):
            # Construct paths
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            
            # Copy the file
            shutil.copyfile(source_path, destination_path)
            print(f"Copied {file} to {destination_folder}")

def copy_json_files(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    if os.path.exists(destination_folder):
        # If the destination folder exists, remove it
        shutil.rmtree(destination_folder)
        print(f"Existing destination folder {destination_folder} removed")

    # Create the new destination folder
    os.makedirs(destination_folder)
    
    # List all files in the source folder
    files = os.listdir(source_folder)
    
    for file in files:
        # Check if the file is a JSON file
        if file.lower().endswith('.json'):
            # Construct paths
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            
            # Copy the file
            shutil.copyfile(source_path, destination_path)
            print(f"Copied {file} to {destination_folder}")
# Example usage:
# copy_json_files('/path/to/source', '/path/to/destination')
def move_image(source_file, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):

        os.makedirs(destination_folder)
    
    # Construct destination path
    destination_path = os.path.join(destination_folder, os.path.basename(source_file))
    
    if os.path.exists(destination_path):
        # Handle the case where the destination file already exists
        try:
            os.remove(destination_path)  # Delete existing file
            print(f"Deleted existing file: {destination_path}")
        except OSError as e:
            print(f"Error deleting file: {destination_path}")
            print(e)
    
    try:
        # Attempt to move the file
        shutil.move(source_file, destination_path)
        print(f"Moved {source_file} to {destination_path}")
    except FileNotFoundError:
        print(f"Source file not found: {source_file}")
    except Exception as e:
        print(f"Error moving file: {e}")

if __name__ == "__main__":
    theme='foxi-astro-theme'
    prefix=None
    theme_folder_root = f'{theme}/{theme}-main'

    try:
        if os.path.exists(theme_folder_root):
            shutil.rmtree(theme_folder_root)
            print(f"The folder {theme_folder_root} has been removed.")
        else:
            print(f"The folder {theme_folder_root} does not exist.")
    except OSError as e:
        print(f"Error: {e.strerror}. The folder {theme_folder_root} could not be removed.")        
    get_theme(themedownloadurl)

    theme_name='foxi-astro-theme'
    
    directory_path = 'content'  # Replace with your parent directory path


    set_astroplate_blogs(directory_path,theme_name,f'{theme_folder_root}/src/content/blog')
    print('process homepage')

    homejson_path = os.path.join(directory_path, theme_name, 'homepage.json')
    homemd_path=os.path.join(f'{theme_folder_root}/src/content/homepage/english', '-index.md')
    
    set_json_to_md_page(homejson_path,homemd_path)
    ctajson_path = os.path.join(directory_path, theme_name, 'cta.json')
    ctamd_path=os.path.join(f'{theme_folder_root}/src/content/sections/english', 'call-to-action.md')
    
    set_json_to_md_page(ctajson_path,ctamd_path)
    
    testimonialjson_path = os.path.join(directory_path, theme_name, 'testimonial.json')
    testimonial_md_path=os.path.join(f'{theme_folder_root}/src/content/sections/english', 'testimonial.md')
    
    set_json_to_md_page(testimonialjson_path,testimonial_md_path)
    print('process fingerprint')
    try:
        set_fingerprint(directory_path,theme_name,f'{theme_folder_root}/src/content/pages/english')
    except:
        pass
    print('process logo')
    logopath=os.path.join(directory_path,'images', 'logo.png')
    
    logo_output_path=os.path.join(f'{theme_folder_root}/public/', 'images')
    
    move_image(logopath,logo_output_path)

    print('process astro config')
    source_folder=os.path.join(directory_path, theme_name, 'config')
    destination_folder=f'{theme_folder_root}/src/config'
    copy_json_files(source_folder,destination_folder)
    print('process i18n config')
    source_folder=os.path.join(directory_path, theme_name, 'i18n')
    destination_folder=f'{theme_folder_root}/src/i18n'
    copy_json_files(source_folder,destination_folder)
    print('process lang folder')

    add_lang_folder(directory_path,theme_name,f'{theme_folder_root}/src/content')
    print('process blog')
