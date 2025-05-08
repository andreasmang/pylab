filename=lec01
#filename=applications

all:
	pdflatex ${filename}
	open -a Skim ${filename}.pdf
	@echo Done ....!


bib:
	pdflatex ${filename}
	bibtex ${filename}
	bibtex ${filename}
	pdflatex ${filename}
	pdflatex ${filename}
	open -a Skim ${filename}.pdf
	@echo Done ....!


clean:
	rm -f *.aux *.log *.dvi *.blg *.bbl \
          *.fls *.fdb_latexmk *.out     \
          *.brf *.snm *.toc *.nav       \
		  *.pdfsync *.bcf *.pdf 
	@echo Cleaned ....!
