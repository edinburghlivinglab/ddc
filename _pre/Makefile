skeldir := ../course_docs
installdir := ../pages

#PRE := $(wildcard *.pre)
MD := $(patsubst %.pre, %.md, $(wildcard *.pre))

GPP := /opt/local/bin/gpp

all: $(MD)

install:
	cp $(MD) $(installdir)

%.md : %.pre
	$(GPP) -H -o $@ $<

clean:
	rm $(MD)






