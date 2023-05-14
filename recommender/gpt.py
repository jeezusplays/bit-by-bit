import openai
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.environ.get("gptapi")

# Set up your OpenAI API credentials
openai.api_key = api_key


def prompt_chat_gpt(job):

    promptv1 = f"List top 50 skills as tags for a {job} return data only in json"

    promptv2 = f'''
    List relevant skills as tags for a {job}, return data only in json, categorize them accordingly, do not include other prompts, I expect only stringified json
    
    Category:
    Technical Skills
    Soft Skills
    Hard Skills
    Job-Specific Skills
    Transferable Skills
    Adaptive Skills
    Analytical Skills
    Creative Skills
    '''

    promptv3 = f'''
    List relevant skills as short tags for a {job}, return data only in json, categorize them accordingly, do not include other prompts, I expect only stringified json
    
    Category:
    Technical Skills
    Soft Skills
    Hard Skills
    Job-Specific Skills
    Transferable Skills
    Adaptive Skills
    Analytical Skills
    Creative Skills
    '''

    try:
        # Generate the response from ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that only returns data in json format from the prompt"},
                {"role": "user", "content": promptv2}
            ],
            temperature=0.2
        )

    # Extract the generated response from the API response
        print(response['choices'][0]['message']['content'])
        return {
            'job': job,
            'skills': json.loads(response['choices'][0]['message']['content'])
        }
    except:
        return {}
    # print(response['usage'])
    # Return the response as a JSON object
    # return json.dumps({'response': generated_text})
    # return None

if __name__ == "__main__":
    prompt_chat_gpt("Cardiac Sonographer")