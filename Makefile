.DEFAULT_GOAL := all

.PHONY: all
all:
	python make_ballots.py 1000000 10
	python run_election.py
