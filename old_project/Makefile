.SILENT: env clean release run uwsgi gunicorn qa test nose-cover test-cover benchmark profile gropf
.PHONY: env clean release run uwsgi gunicorn qa test nose-cover test-cover benchmark profile gropf

VERSION=2.7
PYPI=http://pypi.python.org/simple
ENV=env

PYTHON=$(ENV)/bin/python$(VERSION)
EASY_INSTALL=$(ENV)/bin/easy_install-$(VERSION)
PYTEST=$(ENV)/bin/py.test-$(VERSION)
NOSE=$(ENV)/bin/nosetests-$(VERSION)


all: clean nose-cover release

env:
	PYTHON_EXE=/usr/local/bin/python$(VERSION); \
	if [ ! -x $$PYTHON_EXE ]; then \
		    PYTHON_EXE=/usr/bin/python$(VERSION); \
	fi;\
	virtualenv --python=$$PYTHON_EXE env
	$(EASY_INSTALL) -i $(PYPI) -O2 coverage nose pytest \
	        pytest-pep8 pytest-cov flake8
	# The following packages available for python == 2.4
	if [ "$$(echo $(VERSION) | sed 's/\.//')" -eq 24 ]; then \
		$(EASY_INSTALL) -i $(PYPI) -O2 wsgiref; \
	fi
	$(PYTHON) setup.py develop -O2 -U -i $(PYPI)

clean:
	find src/ -type d -name __pycache__ | xargs rm -rf
	find src/ -name '*.py[co]' -delete
	find src/ -name '*.mo' -delete
	find src/ -name '*.cache' -delete
	rm -rf .cache .coverage src/*.egg-info/

release:
	rm -rf src/*.egg-info/
	$(PYTHON) setup.py -q egg_info sdist

run:
	$(PYTHON) src/app.py

uwsgi:
	$(ENV)/bin/uwsgi --ini development.ini

gunicorn:
	export PYTHONPATH=$$PYTHONPATH:./src ; \
		$(ENV)/bin/gunicorn -b 0.0.0.0:8080 -w 1 app:main

qa:
	$(ENV)/bin/flake8 --max-complexity 6 src setup.py && \
		$(ENV)/bin/pep8 src setup.py ; \

test:
	$(PYTEST) -q -x --pep8 --doctest-modules src/

nose-cover:
	$(NOSE) --stop --with-doctest --detailed-errors --with-coverage \
		--cover-package=public

test-cover:
	$(PYTEST) -q -x --cov-report term-missing src/ \
		--cov public

benchmark:
	$(NOSE) -qs -m benchmark src/

profile:
	$(NOSE) -qs -m benchmark --with-profile \
		--profile-stats-file=profile.pstats src/public

gropf:
	gprof2dot.py -f pstats profile.pstats | dot -Tpng -o profile.png
