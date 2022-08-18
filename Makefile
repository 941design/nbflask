NAME=test
NOTEBOOK=src/$(NAME).ipynb
MARKDOWN=src/$(NAME).md


install:
	pipenv install --dev


install-kernel:
	export JUPYTER_DATA_DIR=$$(pipenv --venv)/share/jupyter; pipenv run install_kernel


to-pdf:
	export PIPENV_DOTENV_LOCATION=./local.env; \
	export NOTEBOOK_FILENAME=$(NOTEBOOK); \
	pipenv run cli


start:
	export PIPENV_DOTENV_LOCATION=./local.env; \
	export NOTEBOOK_FILENAME=$(NOTEBOOK); \
	pipenv run app


to-md:
	pipenv run jupytext --to md --output $(MARKDOWN) $(NOTEBOOK)


from-md:
	pipenv run jupytext --to ipynb --output $(NOTEBOOK) $(MARKDOWN)


notebook:
	export PIPENV_DOTENV_LOCATION=./local.env; \
	pipenv run notebook
