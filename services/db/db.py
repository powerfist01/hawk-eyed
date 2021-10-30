import sqlite3
from datetime import datetime
from flask import g

class DB:
    db_name = 'important.db'
    def __init__(self):
        pass

    def get_db(self):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(self.db_name)
        return db

    def create_instagram_upload_table(self):

        sql = '''
            create table insta_crypto_log (
                id int primary key auto increment not null,
                image varchar(100) not null,
                created_at date not null
            )
        '''

        self.get_db().execute(sql)

    def insert_into_insta_crypto_log(self, image):

        created_at = datetime.date()
        query = '''
            insert into insta_crypto_log (image, created_at) values (%s, %s)
        '''

        args = (image, created_at)

        db = self.get_db()
        db.cursor().execute(query, args)
        db.commit()

    def get_insta_crypto_log_table_data(self):

        query = '''
            select * from insta_log_crypto
        '''

        cur = self.get_db().execute(query)
        data = cur.fetchall()
        cur.close()

        return data
