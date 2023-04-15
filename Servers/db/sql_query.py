TABLE_NAME = 'Speed'

QUERY_SLEEP_0_25 = 'SELECT pg_sleep(0.25)'
QUERY_SLEEP_0_5 = 'SELECT pg_sleep(0.5)'
QUERY_SLEEP_0_75 = 'SELECT pg_sleep(0.75)'
QUERY_SLEEP_1 = 'SELECT pg_sleep(1)'
QUERY_SLEEP_2 = 'SELECT pg_sleep(2)'

QUERY_1 = f"""
    SELECT *
    FROM {TABLE_NAME}
    LIMIT 1
"""
QUERY_1K = f"""
    SELECT *
    FROM {TABLE_NAME}
    LIMIT 1000
"""
QUERY_10K = f"""
    SELECT *
    FROM {TABLE_NAME}
    LIMIT 10000
"""

QUERY_100K = f"""
    SELECT *
    FROM {TABLE_NAME}
    LIMIT 100000
"""
QUERY_1KK = f"""
    SELECT *
    FROM {TABLE_NAME}
    LIMIT 1000000
"""

__all__ = [
    'QUERY_1',
    'QUERY_1K',
    'QUERY_10K',
    'QUERY_100K',
    'QUERY_1KK',

    'QUERY_SLEEP_0_25',
    'QUERY_SLEEP_0_5',
    'QUERY_SLEEP_0_75',
    'QUERY_SLEEP_1',
    'QUERY_SLEEP_2',
]
