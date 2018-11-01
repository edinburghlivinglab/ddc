installdir := ../slides
pptxdir := ../pptx

NEW := week10-2.md 
ALLHTML := $(wildcard *.html)
HTML := $(patsubst %.md, %.html, $(NEW))

ALLMD := $(wildcard *.md)
PPTX := $(patsubst %.md, %.pptx, $(ALLMD))

OPTIONS := --variable revealjs-url="../assets/reveal.js"  --include-in-header="style.css" --standalone

all: $(HTML)

pptx: $(PPTX)


%.html : %.md
	pandoc --smart -t revealjs $(OPTIONS) $< -o $@
	cp $@ $(installdir)


%.pptx : %.md
	pandoc $< -o $@
	mv $@ $(pptxdir)


clean:
	-rm $(ALLHTML)

