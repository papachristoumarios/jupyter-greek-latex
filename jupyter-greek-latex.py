#!/usr/bin/env python3
# Export Greek LaTeX text from Jupyter Notebooks
# Author: Marios Papachristou
# Usage: jupyter nbconvert foo.ipynb --to latex --stdout | jupyter-greek-latex.py >result.tex

import sys
import os

this_dir, this_filename = os.path.split(__file__)
   
with open(os.path.join(this_dir, 'delimiter.aux')) as f:
	delimiter = f.read()

with open(os.path.join(this_dir, 'prelude.aux')) as f:
	prelude = f.read()

notebook = sys.stdin.read().replace(delimiter, prelude)
sys.stdout.write(notebook)

