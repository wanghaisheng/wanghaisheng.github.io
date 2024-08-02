import os
import json
import re
import ruamel.yaml
import sys
from ruamel.yaml.comments import CommentedMap
from datetime import datetime
import shutil

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

def load_json_to_yaml(json_path):
    # Load JSON data from file
    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    # Convert JSON date string to datetime object
    if json_data.get('date'):
        json_data['date'] = datetime.strptime(json_data['date'], '%Y-%m-%dT%H:%M:%SZ')

    # Convert JSON to YAML format
    yaml_data = CommentedMap(json_data)  # Convert JSON to a CommentedMap

    return yaml_data
def combine_yaml_md( md_path,json_path, combined_path=None):
    # Load existing Markdown content
    with open(md_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert YAML data to YAML string
    yaml = ruamel.yaml.YAML()
    yaml.default_flow_style = False  # Ensure block style YAML
    yaml_data=load_json_to_yaml(json_path)
    # Create an in-memory stream (StringIO) to dump YAML content
    yaml_stream = ruamel.yaml.compat.StringIO()

    # Dump YAML data to the in-memory stream
    yaml.dump(yaml_data, yaml_stream)

    # Get YAML string from the in-memory stream
    yaml_str = yaml_stream.getvalue()
    # Remove the final '...' added by ruamel.yaml (if present)
    if yaml_str.endswith('...\n'):
        yaml_str = yaml_str[:-4]

    # Combine YAML string and existing Markdown content
    combined_content = f"---\n{yaml_str.strip()}\n---\n\n{md_content.strip()}\n"

    # Write combined content to a new file if combined_path is provided
    if combined_path:
        with open(combined_path, 'w', encoding='utf-8') as combined_file:
            combined_file.write(combined_content)
        print(f"Combined YAML and Markdown file created: {combined_path}")

    return combined_content


def construct_full_md(md_path, json_path):
    # Read original markdown content
    with open(md_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read().strip()

    # Construct front matter
    front_matter =json_to_yaml(json_path)
    if not front_matter:
        print(f'frontmatter error:{front_matter}')
    # Combine front matter with original content
    full_content = f"{front_matter}\n{md_content}"

    return full_content
def prepare_lang(path):
    # Then iterate over the items as shown above

    data=load_json(path)
    llist=[]
    for lang_option in data:
        d=lang_option['contentDir']
        print(f"Content Directory: {d}")
        llist.append(d)
    return llist
def set_astroplate_blogs(directory,theme_name,output_directory):
    # Ensure directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    blogdirectory=directory+'/blogs'
    langpath=os.path.join(directory, theme_name, 'config/language.json')

    langlist=prepare_lang(langpath)
    # Iterate through all .md files in the directory
    for md_file in os.listdir(blogdirectory):
        if md_file.endswith('.md'):
            print(f'find a md under /blog:{md_file}')
            md_path = os.path.join(blogdirectory, md_file)
            
            # Construct corresponding JSON file path in subdirectory 'x'
            json_file = re.sub(r'\.md$', '.json', md_file)
            json_path = os.path.join(directory, theme_name, json_file)
            
            # Load JSON data
            # json_data = load_json(json_path)
            print('load yml frontmatter')
            if os.path.exists(json_path):
                # Construct full markdown content
                full_md_content = combine_yaml_md(md_path, json_path)
                
                # Write combined content to a new file
                for lang in langlist:
                    lang_output_directory=os.path.join(output_directory,lang)
                    if not os.path.exists(lang_output_directory):

                        os.makedirs(lang_output_directory)
                    combined_md_path = os.path.join(output_directory,lang, f"{md_file}")
  
                    with open(combined_md_path, 'w', encoding='utf-8') as combined_file:
                        combined_file.write(full_md_content)
                    
                    print(f"Combined blog file created: {combined_md_path}")
def add_lang_folder(directory,theme_name,output_directory):
    langpath=os.path.join(directory, theme_name, 'config/language.json')

    langlist=prepare_lang(langpath)    
    for lang in langlist:

        for dir in os.listdir(output_directory):
            new_destination_folder=os.path.join(dir,lang) 
            destination_folder=os.path.join(dir,'english') 

            if not os.path.exists(new_destination_folder):
                # Rename the existing destination folder
                shutil.move(destination_folder, new_destination_folder)
                print(f"cp english  folder  to {new_destination_folder}")
                
def json_to_yaml(json_path):
    # Create a YAML object
    yaml = ruamel.yaml.YAML()
    json_data = load_json(json_path)


    # Dump JSON data to YAML format
    return yaml.dump(json_data,sys.stdout)

def set_json_to_md_page(json_path,combined_path):
    # Create a YAML object
    yaml = ruamel.yaml.YAML()
    json_file='homepage.json'

    yaml.default_flow_style = False  # Ensure block style YAML
    yaml_data=load_json_to_yaml(json_path)
    # Create an in-memory stream (StringIO) to dump YAML content
    yaml_stream = ruamel.yaml.compat.StringIO()

    # Dump YAML data to the in-memory stream
    yaml.dump(yaml_data, yaml_stream)

    # Get YAML string from the in-memory stream
    yaml_str = yaml_stream.getvalue()
    # Remove the final '...' added by ruamel.yaml (if present)
    if yaml_str.endswith('...\n'):
        yaml_str = yaml_str[:-4]

    # Combine YAML string and existing Markdown content
    combined_content = f"---\n{yaml_str.strip()}\n---"
    # combined_path = os.path.join(output_directory, '-index.md')

    # Write combined content to a new file if combined_path is provided
    if combined_path:
        with open(combined_path, 'w', encoding='utf-8') as combined_file:
            combined_file.write(combined_content)
        print(f"Combined YAML and Markdown file created: {combined_path}")


# Example usage:
# if __name__ == "__main__":
#     theme_name='astroplate'
#     directory_path = 'content'  # Replace with your parent directory path
#     set_astroplate_blogs(directory_path,theme_name,'astroplate/astroplate-main/src/content/blog/english')
#     set_homepage(directory_path,theme_name,'astroplate/astroplate-main/src/content/homepage/english')