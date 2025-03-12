import openai
import os

openai.api_key = "Paste your OPENAI key here" #TODO: Paste your OPENAI Key here


def generate_rpg_story():
    client = openai.OpenAI(api_key=openai.api_key)

    prompt = """ """ # TODO: Prompt engineer to get the exact story format you want here.

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI that generates structured RPG stories."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def save_story_to_file(filename, story_text):
    #TODO: Store the generated text into story.txt


if __name__ == "__main__":
    story_text = generate_rpg_story()
    save_story_to_file("story.txt", story_text)