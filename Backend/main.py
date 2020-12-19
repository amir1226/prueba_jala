from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, APIRouter, HTTPException, FastAPI
import requests
from db.lyricsDB import database, lyricsDB
from models.lyric_models import lyricIn

# Api information
api_key = "a_ItVQVpy8n2JpN7SO382k7W0vMPV3O27WE9QQ0PXkAAAPDX9HEHRS5VJmcPuOPGzZoH2U0PglLUVbv2W0"
url = "https://api-b2b.backenster.com/b1/api/v3/translate"

app = FastAPI()


origins = [
    "http://localhost", "http://localhost:8081",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello to translate lyrics API"}


@app.post("/translatelyric")
async def translate(lyricFront: lyricIn):
    for k in database:
        if database[k][0] == lyricFront.artist and database[k][1] == lyricFront.song:
            return {"traduccion": database[k][3]}

    data = lyricFront.foreignLyric
    BODY = {
        "from": "en_GB",
        "to": "es_CO",
        "data": data,
        "platform": "api"}
    HEADERS = {"Authorization": "Bearer {}".format(api_key)}

    response = requests.post(url, data=BODY, headers=HEADERS)

    if response.status_code == 200:
        dictionary = response.json()
        translate = dictionary['targetTransliteration']
    else:
        raise HTTPException(
            status_code=403, detail="Error: Can't contact Api translator")

    new_lyric = lyricsDB(**lyricFront.dict(), spanishLyric=translate)
    max_key = max(list(database.keys()))
    database[max_key+1] = new_lyric

    return {"traduccion": new_lyric.spanishLyric}

    """ if len(session.query(lyricsDB).all()) > 0:
         all_lyrics = session.query(lyricsDB).all()
         for lyric in all_lyrics:
             if lyric.artist == lyricFront.artist and lyric.artist == lyricFront.artist:
                 return {"traduccion": lyric.spanishLyric}
    """
