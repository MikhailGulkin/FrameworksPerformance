from flask import Flask

from Servers.db_query.sync_query.sql_query import cursor
from Servers.db_query.query import *

app = Flask(__name__)


@app.route('/1_record')
def one_record():
    cursor.execute(
        QUERY_1
    )
    return {'len': len(cursor.fetchall())}


@app.route('/1_s_sleep')
def one_sec_sleep():
    cursor.execute(
        QUERY_SLEEP_1
    )
    return {'hello': "world"}


@app.route('/1_k_records')
def one_k_records():
    cursor.execute(
        QUERY_1K
    )
    return {'len': len(cursor.fetchall())}


@app.route('/10_k_records')
def ten_k_records():
    cursor.execute(
        QUERY_10K
    )
    return {'len': len(cursor.fetchall())}


@app.route('/100_k_records')
def thousand_k_records():
    cursor.execute(
        QUERY_100K
    )
    return {'len': len(cursor.fetchall())}


@app.route('/1_kk_records')
def one_million_records():
    cursor.execute(
        QUERY_1KK
    )
    return {'len': len(cursor.fetchall())}
