The Problem
The problem is sourced from LeetCode, specifically Game Play Analysis IV.

We are given a table 'Activity' with the following schema:

Column Name	Type
player_id	int
device_id	int
event_date	date
games_played	int
(player_id, event_date) is the primary key of this table.

The table records the activity of players for different games. Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on some day using some device.

Our task is to write an SQL query to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, we need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

Example:

Input:

player_id	device_id	event_date	games_played
1	2	2016-03-01	5
1	2	2016-03-02	6
2	3	2017-06-25	1
3	1	2016-03-02	0
3	4	2018-07-03	5
Output:

fraction
0.33
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33


Using CTE, JOIN, and Aggregate Functions

WITH first_login AS (
    SELECT player_id, MIN(event_date) [first_day]
    FROM Activity
    GROUP BY player_id
),
second_login AS (
    SELECT a.player_id
    FROM Activity a
    INNER JOIN first_login f ON a.player_id = f.player_id AND a.event_date = DATEADD(day, 1, f.first_day)
)
SELECT 
    ROUND(COUNT(DISTINCT s.player_id) * 1.0 / COUNT(DISTINCT f.player_id), 2) [fraction]
FROM 
    first_login f
LEFT JOIN 
    second_login s ON f.player_id = s.player_id


    Solution 2: Using Window Functions and DATEDIFF

    WITH result AS (
    SELECT
        event_date,
        MIN(event_date) OVER(PARTITION BY player_id) [first_event_date],
        ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) [rn]
    FROM Activity
), counters AS (
    SELECT COUNT(DISTINCT player_id) [counter]
    FROM Activity
)
SELECT ISNULL(
    (
        SELECT DISTINCT ROUND(COUNT(rn) OVER() * 1.0 / counter, 2) [f]
        FROM result, counters
        WHERE DATEDIFF(day, first_event_date, event_date) = 1
    )
, 0) [fraction]