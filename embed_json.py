# Python program to read json file
 
import json
 
with open('./old_new_json/tableaus_first_embed.json') as file:

    # returns JSON object as a dictionary
    data = json.load(file)
 
    for i in data:

        print(i['letter_pair'])
 