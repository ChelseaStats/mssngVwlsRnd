
import csv
import pytest
import player


def test_given_player_apps_matches_total_returns_true():
    with open('player_history.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            po = player.player(
                row['Player Name'],
                row['Goals'],
                row['Games'],
                row['Starter'],
                row['Sub'],
                row['Active'],
                row['Debut']
                )
            assert po.check_apps_matches_total() is True


testdata = [
    (0, "no goals"),
    (1, "1 goal"),
    (2, "2 goals"),
    (3, "3 goals"),
    (211, "211 goals")
]
@pytest.mark.parametrize("a, b", testdata)
def test_given_goal_output_string_returns_correctly(a, b):
    po = player.player("name", a, 0, 0, 0, 1, "2020-09-01")
    assert po.get_goals_string() == b


def test_given_active_player_0_games_returns_error():
    po = player.player("name", 0, 0, 0, 0, 1, "2020-09-01")
    assert po.get_guess_player_string() == 'error'


def test_given_active_player_1_games_return_string_correctly():
    po = player.player("name", 0, 1, 0, 0, 1, "2020-09-01")
    b = "#GuessThePlayer This player made his debut for #Chelsea on 1 September 2020 making 1 appearances so far, scoring no goals. #CFC"
    assert po.get_guess_player_string() == b


def test_given_nonactive_player_1_games_return_string_correctly():
    po = player.player("name", 0, 1, 0, 0, 0, "2020-09-01")
    b = "#GuessThePlayer This formerblue made his debut for #Chelsea on 1 September 2020 making a total of 1 appearances, scoring no goals. #CFC"
    assert po.get_guess_player_string() == b


def test_given_active_player_10_games_return_string_correctly():
    po = player.player("name", 10, 10, 5, 5, 1, "2020-09-01")
    b = "#GuessThePlayer This player made his debut for #Chelsea on 1 September 2020 making 10 appearances so far, scoring 10 goals. #CFC"
    assert po.get_guess_player_string() == b


def test_given_nonactive_player_10_games_return_string_correctly():
    po = player.player("name", 10, 10, 5, 5, 0, "2020-09-01")
    b = "#GuessThePlayer This formerblue made his debut for #Chelsea on 1 September 2020 making a total of 10 appearances, scoring 10 goals. #CFC"
    assert po.get_guess_player_string() == b
