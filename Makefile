PYTHON=3.8.13
BASENAME=$(shell basename $(CURDIR))

env:
	conda create -n $(BASENAME)  python=$(PYTHON)

setup:
	conda install --file requirements.txt $(addprefix -c ,$(CONDA_CH))