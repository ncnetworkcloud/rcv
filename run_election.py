#!/usr/bin/env python


import json

DEBUG = False

def print_ballots(ballots):
    if DEBUG:
        print()
        for ballot in ballots:
            print(" ".join(ballot))
        print()


def main():

    # Vote totals per unique candidate; start at zero
    votes = {"a": 0, "b": 0, "c": 0, "d": 0}

    with open("input.json", "r") as handle:
        data = json.load(handle)

    votes = {cand: 0 for cand in data["candidates"]}

    # Round 1: Winner has more than 50% of first-choice votes

    for ballot in data["ballots"]:
        votes[ballot[0]] += 1

    total = len(data["ballots"])
    print(f"Round 1: {votes}")
    for k, v in votes.items():
        if v > total / 2:
            print(f"Winner: '{k}' with {v}/{total} votes")
            return

    print_ballots(data["ballots"])

    # No outright winner; eliminate the weakest candidate
    i = 1
    while len(votes) > 2:

        # Identify and remove the loser
        loser = min(votes, key=votes.get)
        votes.pop(loser)

        # Reset all remaining candidate votes to zero
        votes = dict.fromkeys(votes, 0)

        # Count votes for the next best choice, ensuring that
        # the ballot has at least one choice remaining
        for ballot in data["ballots"]:
            if loser in ballot:
                ballot.remove(loser)
            if ballot:
                votes[ballot[0]] += 1

        i += 1
        print(f"Round {i}: '{loser}' eliminated - {votes}")
        print_ballots(data["ballots"])

    # Eliminations complete; recount ballots
    for k, v in votes.items():
        total = sum(votes.values())
        if v > total / 2:
            print(f"Winner: '{k}' with {v}/{total} votes")

if __name__ == "__main__":
    main()
