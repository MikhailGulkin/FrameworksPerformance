TABLE_NAME = 'Speed'
QUERY_SLEEP_1 = 'SELECT pg_sleep(10)'
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
    'QUERY_10K',
    'QUERY_1K',
    'QUERY_100K',
    'QUERY_SLEEP_1',
]
