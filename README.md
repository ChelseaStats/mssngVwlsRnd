### MssngVwlsRnd
 
 > Missing Vowels Round Style Game for Twitter

Based on the game seen in the TV show Only Connect this script, run as a scheduled task / cron job will tweet a player's name from the database after removing all the vowels and adding random spaces to the string.

The answer is tweeted 20 minutes later.

#### About

Uses Abraham's twitter oauth library and a pdo db class with a couple of extra methods for tweeting and formatting names you'll need to set up an app on `dev.twitter.com` and then get the set of `keys` (4) and you'll need to add some `DB` connection info.

#### Query and Table

The query selects a random row from the table where count is 0.

The table is `id`,`field`,`count` .
+ `id` is autoincrementing, primary key, integer.
+ `field` is the name or whatever to be 'mssngVwled' and tweeted.
+ `count` is defaulted to zero and then updated to 1 after being tweeted so it's not used again.

The query returns `id` (to be used for updating later) and the `field` (to be jumbled up and tweeted) the field is also stored in a variable so it can be used as the answer in a later tweet.

#### Cron

set up a cron to execute `index.php` at a given time (once a day probably). 
20 minutes later the answer will be tweeted.
