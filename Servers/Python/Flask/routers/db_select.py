from flask import Blueprint

from Servers.Python.utils.db.sync_query.db_con import cursor
from Servers.Python.utils.db.sql_query import *
from Servers.Python.utils.path import DbSelect

bp = Blueprint(
    'db_select_blueprint',
    __name__
)


@bp.route(DbSelect.one_record)
def one_record():
    cursor.execute(
        QUERY_1
    )
    return {'len': len(cursor.fetchall())}


@bp.route(DbSelect.one_k_records)
def one_k_records():
    cursor.execute(
        QUERY_1K
    )
    return {'len': len(cursor.fetchall())}


@bp.route(DbSelect.ten_k_records)
def ten_k_records():
    cursor.execute(
        QUERY_10K
    )
    return {'len': len(cursor.fetchall())}


@bp.route(DbSelect.hundred_k_records)
def hundred_k_records():
    cursor.execute(
        QUERY_100K
    )
    return {'len': len(cursor.fetchall())}
