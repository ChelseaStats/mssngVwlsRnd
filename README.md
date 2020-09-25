# Chelsea Puzzles Word Games Bot for Twitter

- ![mssng vwls rnd](https://github.com/TheChelsOrg/bot_chelsea_puzzles/workflows/mssng%20vwls%20rnd/badge.svg) 
- ![Anagram](https://github.com/TheChelsOrg/bot_chelsea_puzzles/workflows/Anagram/badge.svg) 
- ![Guess the player](https://github.com/TheChelsOrg/bot_chelsea_puzzles/workflows/Guess%20the%20player/badge.svg)
- ![Linter](https://github.com/TheChelsOrg/bot_chelsea_puzzles/workflows/Linter/badge.svg)

> This repo contains a number of game types that post on twitter.

## MssngVwlsRnd

Missing Vowels Round Style Game for Twitter. Based on the game seen in the TV show, Only Connect, will tweet a player's name from the CSV file after removing all the vowels and spaces from the string. The answer (player's name) is tweeted 10 minutes later.

## Anagrams

Anagrams are a simple shuffle of the characters of the player's names and tweeted, the answer (player's name) is tweeted 10 minutes later.

## Guess the player

A question is post by giving the debut date, appearances and goals information of a plyer. the answer (player's name) is tweet 10 minutes later.

## Architecture and Code

The repository is made up of a CSV file that needs to be kept up to date with player names. The rest are python scripts in the `python` folder - these are used by scheduled GitHub actions. These actions run on the latest ubuntu, install python and some some packages. It runs the code then completes, deleting the inftastructure hosted by GitHub.

Twitter requires a developer account and application being set up. The credentials (keys, secrets and tokens) are stored in the secrets vault in GitHub and their values are visible once during setting and and are accessible only by name.
