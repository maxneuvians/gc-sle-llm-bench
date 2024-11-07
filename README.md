# LLM Benchmark against Government of Canada Written Expression Exams

This repository contains the code to benchmark the performance of a language model against the Government of Canada second language written expression exams. Exams are taken from public practice exams available on the Government of Canada website.

Currently, the following models are benchmarked:

- Anthropic Claude-3-opus
- Cohere (Command R+)
- Google Gemini Pro
- OpenAI GPT-3.5-turbo
- OpenAI GPT-4-turbo
- OpenAI GTP-4o

A `random` model is also included as a baseline. The expected accuracy of the random model is 25% as it has a 1 in 4 chance of selecting the correct answer.

## Results

### November 2024
|Model|Language|Accuracy|Count|
|---|---|---|---|
|claude-3-opus|en|86.15|5|
|claude-3-opus|fr|90.77|5|
|cohere|en|64.31|5|
|cohere|fr|67.38|5|
|gemini-pro|en|72.31|5|
|gemini-pro|fr|67.69|5|
|openai3-5|en|61.85|5|
|openai3-5|fr|71.69|5|
|openai4|en|85.54|5|
|openai4|fr|88.31|5|
|openai4o-mini|en|81.23|5|
|openai4o-mini|fr|84.00|5|
|openai4o|en|92.31|5|
|openai4o|fr|92.00|5|
|random|en|25.23|5|
|random|fr|25.54|5|

### May/June 2024

|Model|Language|Accuracy|Count|
|---|---|---|---|
|claude-3-opus|en|86.15|5|
|claude-3-opus|fr|90.77|5|
|cohere|en|64.31|5|
|cohere|fr|67.38|5|
|gemini-pro|en|72.31|5|
|gemini-pro|fr|67.69|5|
|openai3-5|en|61.85|5|
|openai3-5|fr|71.69|5|
|openai4|en|85.54|5|
|openai4|fr|88.31|5|
|openai4o|en|92.31|5|
|openai4o|fr|92.00|5|
|random|en|25.23|5|
|random|fr|25.54|5|

## Question sources

- [FR Grammar set 1](https://publications.gc.ca/site/fra/9.801016/publication.html)
- [EN Grammar set 1](https://publications.gc.ca/site/eng/9.801031/publication.html)