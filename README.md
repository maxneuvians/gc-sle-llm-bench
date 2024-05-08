# LLM Benchmark against Government of Canada Written Expression Exams

This repository contains the code to benchmark the performance of a language model against the Government of Canada second language written expression exams. Exams are taken from public practice exams available on the Government of Canada website.

Currently, the following models are benchmarked:

- Cohere (Command R+)
- Google Gemini Pro
- OpenAI GPT-3.5-turbo
- OpenAI GPT-4-turbo

A `random` model is also included as a baseline. The expected accuracy of the random model is 25% as it has a 1 in 4 chance of selecting the correct answer.

## Results

### May 2024

|Model|Language|Avg. accuracy|Total runs|
|---|---|---|---|
|cohere|en|64.31|5|
|cohere|fr|67.38|5|
|gemini-pro|en|72.31|5|
|gemini-pro|fr|67.69|5|
|openai3-5|en|61.85|5|
|openai3-5|fr|71.69|5|
|openai4|en|85.54|5|
|openai4|fr|88.31|5|
|random|en|25.23|5|
|random|fr|25.54|5|

## Question sources

- [FR Grammar set 1](https://publications.gc.ca/site/fra/9.801016/publication.html)
- [EN Grammar set 1](https://publications.gc.ca/site/eng/9.801031/publication.html)