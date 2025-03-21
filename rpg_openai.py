import openai
import os

openai.api_key = "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" #TODO: Paste your OPENAI Key here


def generate_rpg_story():
    client = openai.OpenAI(api_key=openai.api_key)

    prompt = "Create an RPG story about a plane breaking down in the pacific ocean with main charachter ending up on a desert island with two decisions at each step. There must be at least 8 decisions, at least one shared decision and at least 5 levels of decisions before the game ends. Format the decisions as: event_number|description|left_event|right_event" # TODO: Prompt engineer to get the exact story format you want here.

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an AI that generates structured RPG stories."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def save_story_to_file(filename, story_text):
    #TODO: Store the generated text into story.txt
    with open(filename, "w") as file:
        file.write(story_text)



if __name__ == "__main__":
    story_text = generate_rpg_story()
    save_story_to_file("story.txt", story_text)