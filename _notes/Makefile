installdir := ../slides
NEW := week10-2.md 
ALLHTML := $(wildcard *.html)
HTML := $(patsubst %.md, %.html, $(NEW))


OPTIONS := --variable revealjs-url="../assets/reveal.js"  --include-in-header="style.css" --standalone

all: $(HTML)


%.html : %.md
	pandoc --smart -t revealjs $(OPTIONS) $< -o $@
	cp $@ $(installdir)


clean:
	-rm $(ALLHTML)

