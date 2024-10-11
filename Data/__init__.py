import json

with open('./Data/JSONS/button_text.json', 'r', encoding="utf-8") as json_btn_file:
    button_text = json.load(json_btn_file)

with open('./Data/JSONS/text.json', 'r', encoding="utf-8") as json_text_file:
    text = json.load(json_text_file)

