# importing modules
import datefinder
import random


# Class
class player:
    def __init__(self, name, goals, apps, starts, subs, active, debut):
        self.name = name
        self.goals = goals
        self.apps = int(apps or 0)
        self.starts = int(starts or 0)
        self.subs = int(subs or 0)
        self.total = self.starts + self.subs
        self.active = active
        self.debut = debut

    def __repr__(self):
        return repr(self.name, self.goals, self.apps, self.starts, self.subs, self.total, self.active, self.debut)

    def check_apps_matches_total(self):
        if(self.apps != self.total):
            print(self.name)
            return False
        else:
            return True

    def get_date_from_string(self):
        try:
            published_matches = list(datefinder.find_dates(self.debut))
            if len(published_matches) > 0:
                date_string = published_matches[0].strftime("%-d %B %Y")
            else:
                date_string = ""
        except KeyError:
            print(f"error with debut for {self.name}")
            date_string = ""
        return date_string

    def get_goals_string(self):
        if(self.goals > 1):
            output_goals = f"{self.goals} goals"
        elif(self.goals == 0):
            output_goals = "no goals"
        else:
            output_goals = "1 goal"
        return output_goals

    def get_anagram_of_string(self):
        letters = list(self.name)
        random.shuffle(letters)
        return ''.join(letters)

    def get_guess_player_string(self):
        if(self.apps == 0):
            return "error"
        else:
            goals_string = self.get_goals_string()
            debut_string = self.get_date_from_string()
            if(self.active == 1):
                return f"#GuessThePlayer This player made his debut for #Chelsea on {debut_string} making {self.apps} appearances so far, scoring {goals_string}. #CFC"
            else:
                return f"#GuessThePlayer This formerblue made his debut for #Chelsea on {debut_string} making a total of {self.apps} appearances, scoring {goals_string}. #CFC"
