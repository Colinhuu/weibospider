from .basic_db import db_session
from .models import KeywordsWbdata

from decorators import db_commit_decorator


@db_commit_decorator
def insert_keyword_wbid(keyword_id, wbid):
    keyword_wbdata = KeywordsWbdata()
    keyword_wbdata.wb_id = wbid
    keyword_wbdata.keyword_id = keyword_id
    db_session.add(keyword_wbdata)
    db_session.commit()
