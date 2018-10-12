include ../Makefile.defs

installdir := ../course_docs

INDEX := index.md
#PAGES := $(INDEX) syllabus.md $(MD) 
PAGES := syllabus.md $(MD) 
OPTIONS := -s --latex-engine=xelatex --template=latex.template --number-sections


HANDBOOK := handbook.md
PDF := $(HANDBOOK:md=pdf)
#PDF := $(patsubst %.md, %.pdf, $(HANDBOOK))

PANDOC := /usr/local/bin/pandoc

ci: install
	git ci -m "updated handbook" $(installdir)/$(PDF)

install: pdf
	mv $(PDF) $(installdir)

pdf: $(PDF)

cat:
	cat $(PAGES) > $(HANDBOOK)

$(PDF): $(PAGES)
	$(PANDOC) $(OPTIONS) $^ -o $(PDF)




