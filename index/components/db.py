from pony.orm import Database, set_sql_debug
import os
from urllib.parse import urlparse
from components.log import log

db = Database()


def init_db():
    database_url = os.getenv("DATABASE_URL")
    print("database_url: ", database_url)
    url = urlparse(database_url)
    print("url: ", url)
    print("url.hostname: ", url.password)

    db.bind(
        provider=url.scheme,
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path[1:],
        # sslmode='require',
        # options='endpoint=ep-twilight-queen-56021949'
    )

    print("db.bind success")
    db.generate_mapping(create_tables=True)

    set_sql_debug(True)

    log.info("init db ok")
