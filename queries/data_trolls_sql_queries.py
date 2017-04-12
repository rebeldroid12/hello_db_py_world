CREATE_USER_SCRATCH_SCHEMA = """
CREATE SCHEMA IF NOT EXISTS user_scratch"""

CREATE_DATA_TROLLS_TABLE = """
CREATE TABLE IF NOT EXISTS user_scratch.data_trolls (
data_troll_id SERIAL PRIMARY KEY
,name TEXT NOT NULL
,favorite_color TEXT NOT NULL
,title TEXT NOT NULL
,enjoyed BOOLEAN NOT NULL
,data_troll_start_at DATE NOT NULL
)
"""


INSERT_INTO_DATA_TROLLS_TABLE = """
INSERT INTO user_scratch.data_trolls
(name,
favorite_color,
title,
enjoyed,
data_troll_start_at)
VALUES (
%(name)s,
%(favorite_color)s,
%(title)s,
%(enjoyed)s,
%(data_troll_start_at)s
)
"""
