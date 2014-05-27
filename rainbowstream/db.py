from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Map


class RainbowDB():

    engine=None

    def __init__(self):
        self.engine = create_engine('sqlite:///rainbow.db', echo=False)

    def store(self, tweet_id):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        m = Map(tweet_id)
        session.add(m)
        session.commit()

    def rainbow_query(self, rid):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        res = session.query(Map).filter("rainbow_id =:rid").params(rid=rid).all()
        return res

    def tweet_query(self, tid):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        res = session.query(Map).filter("tweet_id =:tid").params(tid=tid).all()
        return res
