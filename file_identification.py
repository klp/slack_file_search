'''
A script that identifies files in a directory/sub-directories that match
string pattern(s)
'''

# import modules that comes with Python's 'batteries included' nature
import os           # gain access to os shell commands 
import fnmatch      # unix filename pattern matching
import re           # regular expressions operation (proceed with caution!)

# create a function to search files
def identify_paths_to_files(directory, file_name_pattern, search_patterns):
    for path, directory, files in os.walk(directory):
        for file_name_pattern in file_name_pattern:
            for file_name in fnmatch.filter(files, file_name_pattern):
                file_path = os.path.join(path, file_name)
                with open(file_path, 'r') as file:
                    file_contents = file.read()
                    file_matches = 0
                    for search_pattern in search_patterns:
                        if re.search(search_pattern, file_contents):
                            file_matches += 1
                        if file_matches == len(search_pattern):
                            yield(file_path)

top_level_directory = '/file_dir'
file_patterns = ['*.json', '*.txt.'] 
search_pattern = ['cowabunga', 'ay caramba']

for file_path in identify_paths_to_files(
    top_level_directory, file_patterns, search_pattern):
        print(file_path)