from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, APIRouter, HTTPException, FastAPI
import requests
from db.lyricsDB import lyricsDB, include_new, search_in_database, database
from models.lyric_models import lyricIn, countIn, count_words_and_lines

# Api information
api_key = "a_ItVQVpy8n2JpN7SO382k7W0vMPV3O27WE9QQ0PXkAAAPDX9HEHRS5VJmcPuOPGzZoH2U0PglLUVbv2W0"
url = "https://api-b2b.backenster.com/b1/api/v3/translate"

app = FastAPI()


origins = [
    "http://localhost", "http://localhost:8081", "http://localhost:8080"
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
    search_lyric = search_in_database(lyricFront)
    if search_lyric:
        return {"translate": search_lyric}

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
    include_new(new_lyric)

    return {"translate": new_lyric.spanishLyric}


@app.post("/stats")
async def translate(text: countIn):
    count = count_words_and_lines(text)
    return {"lines": count[0], "words": count[1]}

"""
@app.get("/database")
async def obtain_database():
    return database
"""
