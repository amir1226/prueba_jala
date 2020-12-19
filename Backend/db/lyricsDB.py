# from sqlalchemy import Column, ForeignKey, Integer, String
# from db.db_connection import Base, engine
from pydantic import BaseModel


class lyricsDB(BaseModel):
    artist: str
    song: str
    foreignLyric: str
    spanishLyric: str


database = {
    1: [lyricsDB(**{
        "artist": "prueba",
        "song": "prueba",
        "foreignLyric": "prueba",
        "spanishLyric": "prueba"
    })],
    2: [lyricsDB(**{
        "artist": "Queen",
        "song": "we will rock you",
        "foreignLyric": "Buddy you're a boy make a big noise",
        "spanishLyric": "derecho de peticion"
    })]
}

for (k) in database:
    print(k)


"""class lyricsDB(Base):
    __tablename__ = "lyrics"
    id = Column(Integer, primary_key=True, autoincrement=True)
    artist = Column(String)
    song = Column(String)
    foreignLyric = Column(String)
    spanishLyric = Column(String)


Base.metadata.create_all(bind=engine)"""
