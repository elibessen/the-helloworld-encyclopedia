import yaml
import json
import os

HELLO_WORLD_DIR     = "../languages/"       # Where the hello world files are stored
CHECKLIST_OUT_DIR   = "../"                 # Where to output the constructed markdown document
LANGUAGE_REF_FILE   = "./languages.yml"     # YAML file to cross-reference file extensions
LANGUAGES_TO_COMP   = "../languages.json"   # JSON file which stores the languages to be completed
CHECKLIST_FILE_NAME = "CHECKLIST.md"        # The name of the checklist markdown file

def find_file(extension, directory):
    result = [_ for _ in os.listdir(directory) if _.endswith(extension)]

    if len(result) > 0:
        return "x"
    else:
        return " "

def make_checklist(list, ref, text):
    total = len(list)
    tally = 0
    for i in list:
        exists = " "
        try:
            extensions = ref[i]['extensions']
        except:
            continue
        for j in extensions:
            exists = find_file(j, HELLO_WORLD_DIR)
            if exists == "x":
                tally += 1
                break
        text += f" - [{exists}] {i}\n" 
    return text, tally, total

if __name__ == "__main__":
    language_ref    = open(LANGUAGE_REF_FILE, "r")
    language_list   = open(LANGUAGES_TO_COMP, "r")

    language_ref    = yaml.load(language_ref, Loader=yaml.SafeLoader)
    language_list   = list(json.load(language_list).keys())

    checklist_text  = ""
    
    checklist_out   = make_checklist(language_list, language_ref, checklist_text)
    checklist_text += "# Language Checklist\n\n"
    checklist_text += f"***{checklist_out[1]}** out of **{checklist_out[2]}***\n"
    checklist_text += checklist_out[0]
    
    checklist_file  = open(f"{CHECKLIST_OUT_DIR}{CHECKLIST_FILE_NAME}", "w")
    checklist_file.write(checklist_text)
    checklist_file.close()
