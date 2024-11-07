phony: anthropic-opus black debug cohere gemini install openai3-5 openai4 random result

anthropic-opus:
	@python3 src/anthropic_opus_bench.py

black:
	@black src/*.py

debug:
	@python3 src/prompts.py

cohere:
	@python3 src/cohere_bench.py

gemini:
	@python3 src/gemini_bench.py

gemini1-5-flash:
	@python3 src/gemini1-5-flash_bench.py

install:
	@pip3 install --user -r requirements.txt

openai3-5:
	@python3 src/openai3-5_bench.py

openai4:
	@python3 src/openai4_bench.py

openai4o:
	@python3 src/openai4o_bench.py

openai4o-mini:
	@python3 src/openai4o-mini_bench.py

openaio1-mini:
	@python3 src/openaio1-mini_bench.py

random:
	@python3 src/random_bench.py

result:
	@python3 src/result_printer.py