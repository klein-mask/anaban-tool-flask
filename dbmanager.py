import random

class SQLAlchemyManager:

    def __init__(self, *, db, Table):
        self.db = db
        self.session = self.db.session
        self.Table = Table
        self.select = self.Table.query.filter

    def insert(self, **kwargs):
        is_insert_success = False
        try:
            record = self.Table(kwargs)
            self.session.add(record)
            self.commit()
            is_insert_success = True
        except:
            pass

        return is_insert_success
    
    def get_latest(self):
        all_record = self.Table.query.all()
        return all_record[len(all_record)-1]
    
    def get_random(self):
        all_record = self.Table.query.all()
        return random.choice(all_record)
    
    def delete(self, record):
        self.session.delete(record)
        self.commit()
    
    def commit(self):
        self.session.commit()
    
    def show_all_record(self):
        all_record = self.Table.query.all()
        for record in all_record:
            print(record.__dict__)

