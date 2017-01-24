CREATE_DATA_TROLLS_TABLE = """
CREATE TABLE IF NOT EXISTS user_scratch.data_trolls (
data_troll_id SERIAL PRIMARY KEY
,name TEXT NOT NULL
,favourite_color TEXT NOT NULL
,employee_start_at DATE NOT NULL
,title TEXT NOT NULL
,enjoyed_lunch_n_learn BOOLEAN NOT NULL
,data_troll_start_at DATE NOT NULL
)
"""


INSERT_INTO_DATA_TROLLS_TABLE = """
INSERT INTO user_scratch.data_trolls
(name,
favourite_color,
employee_start_at,
title,
enjoyed_lunch_n_learn,
data_troll_start_at)
VALUES (
%(name)s,
%(favourite_color)s,
%(employee_start_at)s,
%(title)s,
%(enjoyed_lunch_n_learn)s,
%(data_troll_start_at)s
)
"""
