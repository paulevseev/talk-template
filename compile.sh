#!/usr/bin/env bash

latexmk -bibtex -xelatex main-beamer.tex
latexmk -bibtex -xelatex main-article.tex
