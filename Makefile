.DEFAULT_GOAL := help

help:          ## Show available options with this Makefile
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY : test
test:          ## Run all the tests
test:
	python setup.py test


recreate_env:          ## Run all the tests
recreate_env:
	conda env create --force -f dev_environment.yml
