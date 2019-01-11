include Makefile.defs

PORT := 4020

PAGESDIR := pages
DOCSDIR := course_docs
BUILDIR := _build
#export MD :=  prep.md sprint.md digging_deeper.md develpoment.md reporting.md project_success.md
INDEX := pages-root-folder/index.md
PAGES := $(INDEX) $(MD) 

headed := $(addprefix $(PAGESDIR)/, $(PAGES))
headless := $(addprefix $(BUILDIR)/, $(PAGES))	

STRIPPER := _scripts/preprocess.py
PANDOC := /usr/local/bin/pandoc

# build local Jekyll pages

local:
	bundle exec jekyll serve --port $(PORT) --config _config.yml,_config_dev.yml

####### build pdf version of course handbook

cat: headless
	$(MAKE) cat -C $(BUILDIR)

ci: pdf
	$(MAKE) pdf -C $(BUILDIR)

# strip YAML headers
headless: $(headed)
	python $(STRIPPER) -outdir $(BUILDIR) $^

# compile PDF in the build directory
pdf: headless
	$(MAKE) -C $(BUILDIR)

clean:
	rm -f $(BUILDIR)/*.md


