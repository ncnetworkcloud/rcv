#!/usr/bin/env python

import json
import sys
import random
import string


def make_ballots(ballots, candidates):

    # Initialize the candidate string, one uppercase letter for each
    data = {
        "candidates": string.ascii_uppercase[:candidates],
        "ballots": []
    }

    # Build random ballots with lists of length 1 to "candidates"
    # and with random candidate values in each list
    for ballot in range(ballots):
        votes = random.sample(data["candidates"], random.randint(1, candidates))
        data["ballots"].append(votes)

    # Write ballots to file
    with open("input.json", "w") as handle:
        json.dump(data, handle, indent=2)


if __name__ == "__main__":
    # If the user has specified the proper number of CLI arguments,
    # read in the number of ballots and candidates desired
    if len(sys.argv) == 3:
        make_ballots(ballots=int(sys.argv[1]), candidates=int(sys.argv[2]))

    # CLI args not provided or incorrect number; use defaults
    else:
        make_ballots(ballots=100, candidates=4)
