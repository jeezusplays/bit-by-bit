import json
from gpt import prompt_chat_gpt
from time import sleep

# Read JSON data from file
with open("jobs.json") as json_file:
    data_list = json.load(json_file)

with open("skills3.json") as json_file:
    try:
        skills_list = json.load(json_file)
        skills_set = set([i['job'] for i in skills_list if i['skills'] != None])
        print("loaded skill: ", skills_set)
    except json.decoder.JSONDecodeError:
        skills_list=[]
        skills_set=set([])
        print("Invalid JSON syntax or empty file")
    except FileNotFoundError:
        skills_list=[]
        skills_set=set([])
        print("File not found")


all_skills = [i for i in skills_list if i['skills'] != None]
for data in data_list:
    industry = data['industry']
    jobs = data['jobs']

    for i in range(len(jobs)):
        retry = 5
        job = jobs[i]
        if job in skills_set:
            continue
        print(f'Getting skills for {job}')

        skills = prompt_chat_gpt(job).get('skills')
        while retry > 0 and skills == None:
            skills = prompt_chat_gpt(job).get('skills')
            sleep(5)
            retry -= 1

        j = {
            "job": job,
            'skills': skills
        }
        all_skills.append(j)
        jobs[i] = j

        json_data = json.dumps(all_skills)
        with open("skills3.json", "w") as json_file:
            json_file.write(json_data)

    print(jobs)