# Reads json file that was made using cloud conversion from a flat csv (that was made from the working google sheet doc)
# Takes each of 676 dictionaries in array and gives it a new embedded structure that is desired in the database
# Makes a new json object and creates a file for it
# after running this program, need to open newly created file and right-click and format it

import json
import copy
 
with open('./old_new_json/tableaus_first_embed.json') as file:

    # takes JSON object from file, which in MY case is in the 
    # specialized JSON ARRAY format, and returns a LIST of dictionaries
    dictionaries_orig = json.load(file)

dictionaries_new = []

# new schema:
dict_new = {
    "letter_pair": "",
    "starter_sentence": "",
    "images": {
        "person": "",
        "verb": "",
        "object": "",
        "supplemental": "",
    },
    "elaboration": {
        "pronunciation": "",
        "synopsis": "",
        "hybrid_definition": "",
        "backstory": {
            "story": "",
            "length": 0
        }
    },
    "group": [],
    "comments": [],
    "word_resources": {
        "more_words": "",
        "legacy_sentence": ""
    },
    "memory_tags": {
        "location": "",
        "tableau": ""
    }
}

for dict in dictionaries_orig:

    dict_new["letter_pair"] = dict["letter_pair"]
    dict_new["starter_sentence"] = dict["starter_sentence"]
    dict_new["images"]["person"] = dict["pic_1_person"]
    dict_new["images"]["verb"] = dict["pic_2_verb"]
    dict_new["images"]["object"] = dict["pic_3_object"]
    dict_new["images"]["supplemental"] = dict["pic_4_supplemental"]
    dict_new["elaboration"]["pronunciation"] = dict["pronunciation"]
    dict_new["elaboration"]["synopsis"] = dict["synopsis"]
    dict_new["elaboration"]["hybrid_definition"] = dict["hybrid_definition"]
    dict_new["elaboration"]["backstory"]["story"] = dict["backstory"]
    dict_new["elaboration"]["backstory"]["length"] = int(dict["length_backstory"])
    dict_new["group"] = dict["group"].strip().split(",") if dict["group"] != "" else []
    # dict_new["comments"] = [],
    dict_new["word_resources"]["more_words"] = dict["more_words"]
    dict_new["word_resources"]["legacy_sentence"] = dict["legacy_sentence"]
    dict_new["memory_tags"]["location"] = dict["location"]
    dict_new["memory_tags"]["tableau"] = dict["tableau"]

    dict_local = copy.deepcopy(dict_new)
    dictionaries_new.append(dict_local)


with open('./old_new_json/tableaus_duly_embedded.json', 'w') as output_file:
    json.dump(dictionaries_new, output_file)
