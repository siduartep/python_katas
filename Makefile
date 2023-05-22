all: check coverage mutants

.PHONY: \
		all \
		check \
		clean \
		coverage \
		format \
		green \
		init \
		install \
		linter \
		mutants \
		red \
		refactor \
		setup \
		tests

module = python_katas
codecov_token = 9efa7d6e-d2ae-4ba9-aae2-7f519bddcb01

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests
	mypy ${module}
	mypy tests

clean:
	rm --force --recursive .*_cache
	rm --force --recursive ${module}.egg-info
	rm --force --recursive ${module}/__pycache__
	rm --force --recursive tests/__pycache__
	rm --force .mutmut-cache
	rm --force coverage.xml

coverage: setup
	pytest --cov=${module} --cov-report=xml --verbose && \
	coverage report --show-missing

format:
	black --line-length 100 ${module}
	black --line-length 100 tests

install:
	pip install --editable .

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants: setup
	mutmut run --paths-to-mutate ${module}

setup: clean install

tests:
	pytest --verbose

init: setup tests
	git config --global --add safe.directory /workdir
	git config --global user.name "Simon Duarte"
	git config --global user.email "simon.duarte@islas.org.mx"

setup: clean install

red: format
	git restore python_katas/
	pytest --verbose \
	&& git restore tests/ \
	|| (git add tests/*.py && git commit -m "🛑🧪 Fail tests. This is the way.")
	chmod g+w -R .

green: format
	pytest --verbose \
	&& (git add python_katas/*.py tests/*.py && git commit -m "✅ Pass tests. This is the way.") \
	|| git restore python_katas/ tests/
	chmod g+w -R .

refactor: format
	pytest --verbose \
	&& (git add python_katas/*.py tests/*.py && git commit -m "♻️  Refactor. This is the way.") \
	|| git restore python_katas/ tests/
	chmod g+w -R .