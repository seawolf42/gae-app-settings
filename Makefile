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
# commands for testing
#

PHONY: test
test:
	PYTHONPATH=${PYTHONPATH} python setup.py test


#
# commands for virtualenv maintenance
#

PHONY: sitepackages.clean
sitepackages.clean:
	pip freeze | xargs pip uninstall -y

PHONY: sitepackages.install
sitepackages.install:
	pip install .


#
# commands for packaging and deploying to pypi
#

PHONY: readme
readme:
	pip install pandoc

PHONY: package
package: readme
	pandoc -o README.rst README.md

PHONY: submit
submit: package
	python setup.py sdist upload -r pypi
