#!/usr/bin/env python3
# Export Greek LaTeX text from Jupyter Notebooks
# Author: Marios Papachristou
# Usage: jupyter nbconvert foo.ipynb --to latex --stdout | jupyter-greek-latex.py >result.tex

import sys
   
with open('delimiter.aux') as f:
	delimiter = f.read()

with open('prelude.aux') as f:
	prelude = f.read()

notebook = sys.stdin.read().replace(delimiter, prelude)
sys.stdout.write(notebook)

