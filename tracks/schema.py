from datetime import datetime, timedelta
from ninja import Schema

class TrackSchema(Schema):
    title: str
    artist: str
    duration: str
    last_play: datetime

class NotFoundSchema(Schema):
    message: str