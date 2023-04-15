from flask import Blueprint

from Servers.db.sync_query.sql_query import cursor
from Servers.db.sql_query import *

router = Blueprint(
    'db_sleep',
    __name__
)


@router.route('/0_25_s_sleep')
def zero_25_second_sleep():
    cursor.execute(
        QUERY_SLEEP_0_25
    )
    return {'hello': "world"}


@router.route('/0_5_s_sleep')
def zero_5_second_sleep():
    cursor.execute(
        QUERY_SLEEP_0_5
    )
    return {'hello': "world"}


@router.route('/0_75_s_sleep')
def zero_75_second_sleep():
    cursor.execute(
        QUERY_SLEEP_0_75
    )
    return {'hello': "world"}


@router.route('/1_s_sleep')
def one_second_sleep():
    cursor.execute(
        QUERY_SLEEP_1
    )
    return {'hello': "world"}


@router.route('/2_s_sleep')
def two_second_sleep():
    cursor.execute(
        QUERY_SLEEP_2
    )
    return {'hello': "world"}
