from pydantic import BaseModel


class lyricIn(BaseModel):
    artist: str
    song: str
    foreignLyric: str
