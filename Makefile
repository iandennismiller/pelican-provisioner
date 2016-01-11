# pelican-provisioner (c) 2016 Ian Dennis Miller

SHELL=/bin/bash

install:
	python setup.py install

build-wheels:
	pip wheel --find-links=share/wheelhouse --wheel-dir share/wheelhouse -r skel/requirements.txt

add-plugins:
	git submodule add https://github.com/getpelican/pelican-plugins share/pelican-plugins

clean:
	rm -rf build dist *.egg-info

.PHONY: install build-wheels install-wheels clean
