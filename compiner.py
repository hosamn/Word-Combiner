import os
from docxcompose.composer import Composer
from docx import Document as Document_compose

def combine_all(compined_file, files_list):
    number_of_sections = len(files_list)
    master = Document_compose(files_list[0])   # start with the first file in the list
    composer = Composer(master)
    for i in range(1, number_of_sections):
        doc_temp = Document_compose(files_list[i])
        composer.append(doc_temp)
    composer.save(compined_file)

#########################################

# Change the working directory to the py file dir:
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Get a list of current dir files:
for root, dirs, files in os.walk("."):
    # print(len(files), files)
    files_list = [f for f in files if (f.endswith('.docx') and not f.startswith('Combined'))]
    print(*files_list, sep="\n")
    break  # break after reporting current dir files and don't go deeper



combine_all("Combined.docx", files_list)
