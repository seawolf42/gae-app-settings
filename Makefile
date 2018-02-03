# -------------------------------------
# MAKEFILE
# -------------------------------------


#
# environment
#

ifndef VIRTUAL_ENV
$(error VIRTUAL_ENV is not set)
endif

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
	python setup.py test


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
