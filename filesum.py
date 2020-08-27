#%%
import re
from os import listdir
from os.path import isdir, isfile

def get_file_context():
    pattern = r'(.*)?.md'
    context_dict = {}
    root_path = listdir()
    for path in root_path:
        if isdir(path) and path != '.git':
            files = listdir(path)
            context_dict[path] = {re.search(pattern, file).group(0):f'{path}/{file}' for file in files if re.search(pattern, file)}
    
    return context_dict

def to_md(dict):
    with open('index.md', 'w', encoding='utf-8') as f:
        f.write('# 文章目录\n')
        for key, value in dict.items():
            f.write(f'\n## {key}\n')
            for key_2, value_2 in value.items():
                f.write(f'* [{key_2}]({value_2})\n')

dict = get_file_context()
to_md(dict)
