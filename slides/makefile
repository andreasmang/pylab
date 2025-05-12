filename=lec01
filename=lec02
filename=lec03
filename=lec04
filename=lec05
filename=lec06
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
		  *.pdfsync *.bcf *.pdf *.vrb 
	@echo Cleaned ....!
