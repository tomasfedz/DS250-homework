
# # %%
# import pandas as pd
# import numpy as np
# import sqlite3
# import os

# sqlite_file = r'c:/Users/tomas/Downloads/lahmansbaseballdb.sqlite'

# con = sqlite3.connect(sqlite_file)

# # %%
# # careful to list your path to the file. Or save this code in the same folder as the sqlite file.

# sqlite_file = 'lahmansbaseballdb.sqlite'
# con = sqlite3.connect(sqlite_file)



# # %%
# # allstar table

# q = """
#     SELECT *
#     FROM AllstarFull
#     WHERE yearID > 1999 
#         AND GP <> 1
#     LIMIT 5
# ;
# """

# df = pd.read_sql_query(q,con)
# df

import pandas as pd
import sqlite3
import os

# File path
sqlite_file = r'C:\\Users\\tomas\\Downloads\\lahmansbaseballdb (1).sqlite'
con = sqlite3.connect(sqlite_file)



q1 = """
WITH CareerLength AS (
    SELECT playerID, 
           MIN(yearID) AS start_year, 
           MAX(yearID) AS end_year,
           (MAX(yearID) - MIN(yearID)) AS career_length
    FROM Appearances
    GROUP BY playerID
    HAVING SUM(G_all) >= 10  -- Using SUM(G_all) instead of COUNT(gameID)
)
SELECT p.nameFirst AS first_name, 
       p.nameLast AS last_name, 
       c.career_length
FROM CareerLength c
JOIN People p ON c.playerID = p.playerID
ORDER BY c.career_length DESC
LIMIT 10;

"""

df = pd.read_sql_query(q1, con)
print(df)