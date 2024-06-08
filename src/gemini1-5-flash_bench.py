import os
import re

import google.generativeai as genai

from data import answer_questions
from prompts import (
    generate_system_prompt,
    generate_incorrect_prompt,
    generate_missing_prompt,
)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash-latest")

config = genai.GenerationConfig(
    temperature=0.0,
)


def ask_incorrect_question(question, lang):
    resp = model.generate_content(
        contents=[
            {
                "role": "user",
                "parts": [
                    generate_system_prompt(lang),
                    generate_incorrect_prompt(
                        lang, question["question"], question["answers"]
                    ),
                ],
            },
        ],
        generation_config=config,
        stream=False,
    )
    return re.findall("\d+", resp.text)[0]


def ask_missing_question(question, lang):
    resp = model.generate_content(
        contents=[
            {
                "role": "user",
                "parts": [
                    generate_system_prompt(lang),
                    generate_missing_prompt(
                        lang, question["question"], question["answers"]
                    ),
                ],
            }
        ],
        generation_config=config,
        stream=False,
    )
    return re.findall("\d+", resp.text)[0]


def main(set=1):
    total, correct_count, incorrect_count = answer_questions(
        ask_incorrect_question, ask_missing_question, "gemini-1.5-flash-latest", "fr", set, 10
    )
    print(f"Total: {total} | Correct: {correct_count} | Incorrect: {incorrect_count}")
    print(f"Accuracy: {correct_count / (correct_count + incorrect_count) * 100:.2f}%")


if __name__ == "__main__":
    main()
