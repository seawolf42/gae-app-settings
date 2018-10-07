# -------------------------------------
# MAKEFILE
# -------------------------------------


#
# environment
#

ifndef VIRTUAL_ENV
$(error VIRTUAL_ENV is not set)
endif

GCLOUD_PATH := $(shell which gcloud)
ifndef GCLOUD_PATH
$(error google-cloud-sdk must be installed and on your path)
endif

APPENGINE_PYTHON_PATH := $(realpath ${GCLOUD_PATH}/../../platform/google_appengine)
PYTHONPATH := ${PYTHONPATH}:${APPENGINE_PYTHON_PATH}/:${APPENGINE_PYTHON_PATH}/lib/yaml/lib/

ifeq (test,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "test"
  TEST_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(TEST_ARGS):;@:)
endif
#
# commands for artifact cleanup
#

PHONY: clean.build
clean.build:
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	rm -rf *.egg-info

PHONY: clean.pyc
clean.pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete

PHONY: clean
clean: clean.build clean.pyc


#
# commands for testing
#

PHONY: test.flake8
test.flake8:
	flake8 .

PHONY: test.unittests
test.unittests:
	PYTHONPATH=${PYTHONPATH} python setup.py test

PHONY: test
test: test.unittests test.flake8


#
# commands for packaging and deploying to pypi
#

PHONY: sdist
sdist:
	python setup.py sdist
	python setup.py bdist_wheel

PHONY: release
release: clean sdist
	twine upload dist/*
