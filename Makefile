NAME=test
NOTEBOOK=src/$(NAME).ipynb
MARKDOWN=$(NAME).md


to-pdf:
	export PIPENV_DOTENV_LOCATION=./local.env; \
	export NOTEBOOK_FILENAME=$(NOTEBOOK); \
	pipenv run cli


start:
	export PIPENV_DOTENV_LOCATION=./local.env; \
	export NOTEBOOK_FILENAME=$(NOTEBOOK); \
	pipenv run app


to-md:
	jupytext --to md --output $(MARKDOWN) $(NOTEBOOK)


from-md:
	jupytext --to ipynb --output $(NOTEBOOK) $(MARKDOWN)
