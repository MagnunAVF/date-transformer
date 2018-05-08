help:
	@echo 'Makefile for data-changer                                             '
	@echo '                                                                      '
	@echo 'Usage:                                                                '
	@echo '   setup                                      Install all dependencies'
	@echo '   test                                              Run project tests'

setup:
	@pip install -r requirements_dev.txt

test:
	@py.test tests --cov-report term-missing --cov-report xml --cov=src --pep8 --flakes

.PHONY: help, setup, test
