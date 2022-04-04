import sqlite3


class RedditDB:

    table_create = '''CREATE TABLE {table_name}(
            submission_id VARCHAR(16),
            subreddit VARCHAR(128),
            title VARCHAR(256),
            link_flair_text VARCHAR(256),
            author VARCHAR(32),
            url VARCHAR(512),
            duration INTEGER,
            over_18 BOOLEAN,
            score INTEGER,
            upvote_ratio DECIMAL(1,2),
            hls_url VARCHAR(512),
            datetime DATETIME,
            CONSTRAINT submission_pk PRIMARY KEY (submission_id))'''
    table_exist = """SELECT count(*) FROM sqlite_master
        WHERE type='table' AND name='{table_name}';"""

    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
        self.cur = self.conn.cursor()
        table_exist = self.cur.execute(
            self.table_exist.format(table_name="reddit")).fetchone()[0]
        if table_exist == 0:
            self.cur.execute(self.table_create.format(table_name="reddit"))

    def create(self, record):
        self.cur.execute(
            "insert or ignore into reddit values (?,?,?,?,?,?,?,?,?,?,?,?)",
            record)
        self.conn.commit()

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
