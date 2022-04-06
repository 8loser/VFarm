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
            export_count INTEGER,
            create_datetime DATETIME,
            CONSTRAINT submiussion_pk PRIMARY KEY (submission_id))'''
    table_exist = """SELECT count(*) FROM sqlite_master
        WHERE type='table' AND name='{table_name}';"""

    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
        self.cur = self.conn.cursor()
        table_exist = self.cur.execute(
            self.table_exist.format(table_name="reddit")).fetchone()[0]
        if table_exist == 0:
            self.cur.execute(self.table_create.format(table_name="reddit"))
        # 預設查詢條件
        self.query_string = '''
            select submission_id,duration,hls_url
            from reddit
            where export_count=0 and over_18=False'''

    def create(self, record):
        self.cur.execute(
            "insert or ignore into reddit values (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            record)
        self.conn.commit()

    def set_flair(self, flair):
        if flair:
            self.query_string += ' and link_flair_text in (' + ','.join(
                str("\"" + e + "\"") for e in flair) + ")"

    def set_duration(self, length):
        self.query_string += ' and duration<' + str(length)

    def query(self):
        rows = self.cur.execute(self.query_string).fetchall()
        return rows

    def update(self, id_list):
        id_string = ','.join("\"" + id + "\"" for id in id_list)
        sql = '''UPDATE reddit
                SET export_count = export_count+1
                WHERE submission_id in (''' + id_string + ''')'''

        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
