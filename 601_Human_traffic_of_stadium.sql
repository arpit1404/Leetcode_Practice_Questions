-- Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.

-- Return the result table ordered by visit_date in ascending order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Stadium table:
-- +------+------------+-----------+
-- | id   | visit_date | people    |
-- +------+------------+-----------+
-- | 1    | 2017-01-01 | 10        |
-- | 2    | 2017-01-02 | 109       |
-- | 3    | 2017-01-03 | 150       |
-- | 4    | 2017-01-04 | 99        |
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-09 | 188       |
-- +------+------------+-----------+
-- Output: 
-- +------+------------+-----------+
-- | id   | visit_date | people    |
-- +------+------------+-----------+
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-09 | 188       |
-- +------+------------+-----------+
-- Explanation: 
-- The four rows with ids 5, 6, 7, and 8 have consecutive ids and each of them has >= 100 people attended. Note that row 8 was included even though the visit_date was not the next day after row 7.
-- The rows with ids 2 and 3 are not included because we need at least three consecutive ids.


-- Step 1: Create a CTE (Common Table Expression) `S`
WITH S AS (
    SELECT
        *, 
        -- Step 2: Create a ranking key 'rk' to group consecutive `id`s 
        id - (ROW_NUMBER() OVER (ORDER BY id)) AS rk
    FROM Stadium
    WHERE people >= 100  -- Step 3: Filter only rows where `people >= 100`
),

-- Step 4: Create another CTE `T` to count how many rows belong to each group (rk)
T AS (
    SELECT 
        *, 
        COUNT(1) OVER (PARTITION BY rk) AS cnt  -- Step 5: Count number of rows in each `rk` group
    FROM S
)

-- Step 6: Select final output
SELECT id, visit_date, people
FROM T
WHERE cnt >= 3  -- Step 7: Only keep groups with 3 or more rows
ORDER BY id;   -- Step 8: Order results by `id`
