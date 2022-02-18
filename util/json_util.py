import json
from datetime import datetime, date

import isodate
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, (datetime, date)):
            return isodate.datetime_isoformat(o)
        return json.JSONEncoder.default(self, o)
