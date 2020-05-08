## Setup
# Python VER
VER=3.8

# Paths
PROJ_DIR:=$(realpath $(dir $(firstword ${MAKEFILE_LIST})))
PROJ?=$(notdir ${PROJ_DIR})
VENV?=venv${VER}
BIN=$(abspath ${VENV}/bin)
PYTHON=${BIN}/python${VER}

# Debug Variables
.PHONY: debug
debug:
	$(info $${PROJ_DIR}=${PROJ_DIR})
	$(info $${PROJ}=${PROJ})
	$(info $${BIN}=${BIN})
	$(info $${PYTHON}=${PYTHON})

# Create virtual environment.
.PHONY: venv
venv: ${VENV}
${VENV}:
	@python3.8 -mvenv ${@}
	@${BIN}/pip install --upgrade pip setuptools wheel
	@${MAKE} requirements

# Install requirements
.PHONY: requirements
requirements: requirements.txt
	@${BIN}/pip install --upgrade --requirement requirements.txt

## Action Targets
# Notebook in a screen.
.PHONY:nba
nba:
	screen -S ${PROJ} -d -m ${BIN}/jupyter-notebook --ip=

# Notebook locally in a screen.
.PHONY: nb
nb:
	screen -S ${PROJ} -d -m ${BIN}/jupyter-notebook

# Launch a worker.
.PHONY:worker
worker:
	${PYTHON} worker.py

## Make Documentation
# Generate the README from the Jupyter Notebook.
README.md: README.ipynb
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to markdown --output=${@} ${<}

.PHONY: clean.docs
clean.docs:
	rm -rf docs
# Convert Notebooks to other formats.
IPYNB:=$(wildcard *.ipynb)
MD:=$(patsubst %.ipynb,docs/markdown/%.md,${IPYNB})
PDF:=$(patsubst %.ipynb,docs/pdf/%.pdf,${IPYNB})
HTML:=$(patsubst %.ipynb,docs/html/%.html,${IPYNB})
.PHONY: docs
docs: ${MD} ${PDF} ${HTML}

#
docs/pdf/:
	mkdir -p ${@}
docs/html/:
	mkdir -p ${@}
docs/markdown/:
	mkdir -p ${@}

#
docs/markdown/%.md: %.ipynb docs/markdown/
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to markdown --output=${@} ${<}

docs/pdf/%.pdf: %.ipynb docs/pdf/
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to pdf --output=${@} ${<}

docs/html/%.html: %.ipynb docs/html/
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to html --output=${@} ${<}
