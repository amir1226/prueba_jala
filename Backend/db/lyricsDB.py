# from sqlalchemy import Column, ForeignKey, Integer, String
# from db.db_connection import Base, engine
from pydantic import BaseModel
from typing import List


class lyricsDB(BaseModel):
    artist: str
    song: str
    foreignLyric: str
    spanishLyric: str


database = {}


def search_in_database(newlyric: lyricsDB):
    artist_name = newlyric.artist.lower()
    song_name = newlyric.song.lower()
    if artist_name in database.keys():
        for each_song in database[artist_name]:
            if each_song.song == song_name:
                return each_song.spanishLyric
    return None


def include_new(newlyric: lyricsDB):
    artist_name = newlyric.artist.lower()
    if artist_name in database.keys():
        database[artist_name].append(newlyric)
    else:
        database[artist_name] = [newlyric]
