filename=assignments-1

compdftex=pdflatex


all:
	${compdftex} ${filename}
	open ${filename}.pdf
	@echo Done ....!

bib:
	${compdftex} ${filename}
	-bibtex ${filename}
	-bibtex ${filename}
	${compdftex} ${filename}
	${compdftex} ${filename}
	open ${filename}.pdf
	@echo Done ....!


quick:
	${compdftex} ${filename}
	open ${filename}.pdf
	@echo Done ....!

pdf:
	${compdftex} ${filename}

abstract:
	${compdftex} ${abstract}

log:
	emacs -nw ${filename}.log

cleanbuild:

clean:
	rm -f *.aux *.log *.dvi *.blg *.bbl \
          *.fls *.fdb_latexmk *.out     \
          *.brf *.snm *.toc *.nav       \
		  *.pdfsync *.pdf 
	@echo Cleaned ....! 

%.pdf: %.tex
	${compdftex} $*
	${compdftex} $* 

