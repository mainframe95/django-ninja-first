from datetime import date
from typing import List, Optional
from ninja import NinjaAPI
from .models import Track
from .schema import TrackSchema, NotFoundSchema


tracksApi = NinjaAPI()

@tracksApi.get("tracks", response=List[TrackSchema])
def  tracks(request, title: Optional[str] = None):
    if title:
        return Track.objects.filter(title__icontains=title)
    return Track.objects.all()


@tracksApi.get("tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def  tracks(request, track_id:int):
    try:
        track = Track.objects.get(pk = track_id)
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": " Track does not exist"}
    

@tracksApi.post("tracks/", response= {201: TrackSchema})
def create_track(request, track: TrackSchema):
    track = Track.objects.create(**track.dict())
    return 201, track


@tracksApi.put("tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def  tracks(request, track_id:int, data: TrackSchema):
    try:
        track = Track.objects.get(pk = track_id)
        for attribute, value in data.dict().items():
            setattr(track, attribute, value)
        track.save()
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": " Track does not exist"}


@tracksApi.delete("tracks/{track_id}", response={200: None, 404: NotFoundSchema})
def  tracks(request, track_id:int, data: TrackSchema):
    try:
        Track.objects.delete(pk = track_id)
        return 200
    except Track.DoesNotExist as e:
        return 404, {"message": " Track does not exist"}