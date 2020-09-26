import os
import csv
import pytest
import csv

def tests():
    with open('../player_history.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Player Name']
            apps = row['Games']
            starts = row['Starter'] or 0
            subs = row['Sub'] or 0
            response = checker(name, apps, starts, subs)
            assert response == True


def checker(name, apps, starts, subs):
    total = int(starts) + int(subs)
    if(int(apps) != total):
        print(name)
        return False
    else:
        return True