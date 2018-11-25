# :pen: Jupyter Greek LaTeX 

Convert Jupyter Notebooks to LaTeX with Greek Support (using XeLaTeX)

## Setup

Install Greek LaTeX support from [here](https://github.com/papachristoumarios/greek-latex)

Install from `setup.py`
```
python3 setup.py install
```

Or from PyPi with `pip3`
```
pip3 install jupyter-greek-latex
```

## Usage

Example Usage

```
jupyter nbconvert foo.ipynb --to latex && jupyter-greek-latex.py <foo.tex >result.tex
```

With compilation using `xelatex`
```
jupyter nbconvert foo.ipynb --to latex && jupyter-greek-latex.py <foo.tex | xelatex
```



