from flask import Blueprint

from Servers.Python.utils.db.sync_query.db_con import cursor
from Servers.Python.utils.db.sql_query import *
from Servers.Python.utils.path import DbSleep

bp = Blueprint(
    'db_sleep',
    __name__
)


@bp.route(DbSleep.zero_25_second_sleep)
def zero_25_second_sleep():
    cursor.execute(
        QUERY_SLEEP_0_25
    )
    return {'hello': "world"}


@bp.route(DbSleep.zero_5_second_sleep)
def zero_5_second_sleep():
    cursor.execute(
        QUERY_SLEEP_0_5
    )
    return {'hello': "world"}


@bp.route(DbSleep.zero_75_second_sleep)
def zero_75_second_sleep():
    cursor.execute(
        QUERY_SLEEP_0_75
    )
    return {'hello': "world"}


@bp.route(DbSleep.one_second_sleep)
def one_second_sleep():
    cursor.execute(
        QUERY_SLEEP_1
    )
    return {'hello': "world"}


@bp.route(DbSleep.two_second_sleep)
def two_second_sleep():
    cursor.execute(
        QUERY_SLEEP_2
    )
    return {'hello': "world"}
