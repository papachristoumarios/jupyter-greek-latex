# Jupyter Greek LaTeX 

Convert Jupyter Notebooks to LaTeX with Greek Support (using XeLaTeX)

## Setup

Install from `setup.py`
```
python3 setup.py install
```

## Usage

Example Usage

```
jupyter nbconvert foo.ipynb --to latex --stdout | jupyter-greek-latex.py >result.tex
```

With compilation using `xelatex`
```
jupyter nbconvert foo.ipynb --to latex --stdout | jupyter-greek-latex.py | xelatex
```

