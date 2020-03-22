IPYNB:=$(wildcard *.ipynb)
MD:=$(patsubst %.ipynb,markdown/%.md,${IPYNB})
PDF:=$(patsubst %.ipynb,pdf/%.pdf,${IPYNB})
HTML:=$(patsubst %.ipynb,html/%.html,${IPYNB})

.PHONY: docs
docs: ${MD} ${PDF} ${HTML}

markdown/%.md: %.ipynb
	mkdir -p `dirname ${@}`
	jupyter-nbconvert --ExecutePreprocessor.allow_errors=True --ExecutePreprocessor.timeout=600 --execute --to markdown --output=${@} ${<}

pdf/%.pdf: %.ipynb
	mkdir -p `dirname ${@}`
	-jupyter-nbconvert --ExecutePreprocessor.allow_errors=True --ExecutePreprocessor.timeout=600 --execute --to pdf --output=${@} ${<}

html/%.html: %.ipynb
	mkdir -p `dirname ${@}`
	jupyter-nbconvert --ExecutePreprocessor.allow_errors=True --ExecutePreprocessor.timeout=600 --execute --to html --output=${@} ${<}

README.md: README.ipynb
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to markdown --output=${@} ${<}


.PHONY: clean
clean:
	rm -rf html pdf markdown
