import json
import os

with open(os.path.join(os.curdir, 'server\\resources\\questions.json'), 'r') as f:
    qa_data = json.load(f)

def generate_list():
    result = []
    for obj in qa_data:
        for l in ['easy', 'medium', 'hard']:
            for q in obj[l]:
                result.append(q)

    with open(os.path.join(os.curdir, 'server\\resources\\ques_list.json'), 'w') as f:
        json.dump(result, f, indent=4)
        print('saved')

generate_list()