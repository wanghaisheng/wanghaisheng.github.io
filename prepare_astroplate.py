import os
import json
import re
import ruamel.yaml

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"JSON file not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {file_path}")
        return None

def construct_full_md(md_path, json_data):
    # Read original markdown content
    with open(md_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read().strip()

    # Construct front matter
    front_matter = f"""---
title: "{json_data.get('title', '')}"
meta_title: "{json_data.get('meta_title', '')}"
description: "{json_data.get('description', '')}"
date: "{json_data.get('date', '')}"
image: "{json_data.get('image', '')}"
categories: {json_data.get('categories', [])}
author: "{json_data.get('author', '')}"
tags: {json_data.get('tags', [])}
draft: {json_data.get('draft', False)}
---
"""

    # Combine front matter with original content
    full_content = f"{front_matter}\n{md_content}"

    return full_content

def set_astroplate_blogs(directory,theme_name,output_directory):
    # Ensure directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    # Iterate through all .md files in the directory
    for md_file in os.listdir(directory):
        if md_file.endswith('.md'):
            md_path = os.path.join(directory, md_file)
            
            # Construct corresponding JSON file path in subdirectory 'x'
            json_file = re.sub(r'\.md$', '.json', md_file)
            json_path = os.path.join(directory, theme_name, json_file)
            
            # Load JSON data
            json_data = load_json(json_path)
            if json_data:
                # Construct full markdown content
                full_md_content = construct_full_md(md_path, json_data)
                
                # Write combined content to a new file
                combined_md_path = os.path.join(output_directory, f"{md_file}")
                with open(combined_md_path, 'w', encoding='utf-8') as combined_file:
                    combined_file.write(full_md_content)
                
                print(f"Combined file created: {combined_md_path}")


def set_homepage(directory,theme_name,output_directory):
    # Create a YAML object
    yaml = ruamel.yaml.YAML()
    json_file='homepage.json'
    json_path = os.path.join(directory, theme_name, json_file)
    json_data = load_json(json_path)

    # Construct the output YAML file path
    combined_md_path = os.path.join(output_directory, '-index.md')

    # Dump JSON data to YAML format
    with open(combined_md_path, 'w', encoding='utf-8') as combined_file:
        yaml.dump(json_data, combined_file)

    print(f"YAML file created: {combined_md_path}")
# Example usage:
if __name__ == "__main__":
    theme_name='astroplate'
    directory_path = 'content'  # Replace with your parent directory path
    set_astroplate_blogs(directory_path,theme_name,'astroplate/astroplate-main/src/content/blog/english')
    set_homepage(directory_path,theme_name,'astroplate/astroplate-main/src/content/homepage/english')