import yaml
import json
import os

HELLO_WORLD_DIR     = "../languages/"       # Where the hello world files are stored
CHECKLIST_OUT_DIR   = "../"                 # Where to output the constructed markdown document
LANGUAGE_REF_FILE   = "./languages.yml"     # YAML file to cross-reference file extensions
CHECKLIST_FILE_NAME = "CHECKLIST.md"        # The name of the checklist markdown file

# find a file based on the file extension (this needs to be updated to be more accurate)
def find_file(extension, directory):
    result = [_ for _ in os.listdir(directory) if _.endswith(extension)]    # An array of the results (files with the desired extension)

    if len(result) > 0:                                                     # If there are files in the list return 'checked'
        return "x"
    else:                                                                   # Otherwise return 'unchecked'
        return " "

# Generate the markdown file
def make_checklist(ref, text):
    total = len([*ref])                               # The total number of languages
    tally = 0                                       # The tally of languages completed
    for i in [*ref]:                                  # For each element in the list of languages
        exists = " "
        try:                                        # Sometimes a file will not have an extension (need to account for this case)
            extensions = ref[i]['extensions']
        except:
            continue
        for j in extensions:                        # For each of the extensions (some languages have multiple file extensions)
            exists = find_file(j, HELLO_WORLD_DIR)  # Search for the file
            if exists == "x":
                tally += 1
                break
        text += f" - [{exists}] {i}\n"              # Append the language's checkbox to the markdown string
    return text, tally, total                       # Return the markdown string, tally and total number

# The main function
if __name__ == "__main__":
    print("Opening reference files...")

    language_ref    = open(LANGUAGE_REF_FILE, "r")
    print("done.")

    print("Parsing reference files...")
    language_ref    = yaml.load(language_ref, Loader=yaml.SafeLoader)
    print("done.")

    print(f"Generating {CHECKLIST_FILE_NAME} file...")
    checklist_text  = ""
    
    checklist_out   = make_checklist(language_ref, checklist_text)
    checklist_text += "# Language Checklist\n\n"
    checklist_text += f"***{checklist_out[1]}** out of **{checklist_out[2]}***\n"
    checklist_text += checklist_out[0]
    print("done.")

    print(f"Saving {CHECKLIST_FILE_NAME}...")
    checklist_file  = open(f"{CHECKLIST_OUT_DIR}{CHECKLIST_FILE_NAME}", "w")
    checklist_file.write(checklist_text)
    checklist_file.close()
    print("done.")
