test:
	python test.py


dist:
	cd oopyconnector && python setup.py sdist upload
