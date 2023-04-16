from flask import Blueprint

from Servers.db.sync_query.db_con import cursor
from Servers.db.sql_query import *

bp = Blueprint(
    'db_select_blueprint',
    __name__
)


@bp.route('/1_record')
def one_record():
    cursor.execute(
        QUERY_1
    )
    return {'len': len(cursor.fetchall())}


@bp.route('/1_k_records')
def one_k_records():
    cursor.execute(
        QUERY_1K
    )
    return {'len': len(cursor.fetchall())}


@bp.route('/10_k_records')
def ten_k_records():
    cursor.execute(
        QUERY_10K
    )
    return {'len': len(cursor.fetchall())}


@bp.route('/100_k_records')
def thousand_k_records():
    cursor.execute(
        QUERY_100K
    )
    return {'len': len(cursor.fetchall())}
