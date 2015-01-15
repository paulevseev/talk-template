#!/usr/bin/env bash

latexmk -e '$pdflatex = xelatex' -f -pdf main-beamer.tex
latexmk -e '$pdflatex = xelatex' -f -pdf main-article.tex
latexmk -pdf handout.tex
