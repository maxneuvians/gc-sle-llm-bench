phony: debug cohere install openai3-5 openai4 random result

debug:
	@python3 src/prompts.py

cohere:
	@python3 src/cohere_bench.py

install:
	@pip3 install --user -r requirements.txt

openai3-5:
	@python3 src/openai3-5_bench.py

openai4:
	@python3 src/openai4_bench.py

random:
	@python3 src/random_bench.py

result:
	@python3 src/result_printer.py