from pydantic import BaseModel


class lyricIn(BaseModel):
    artist: str
    song: str
    foreignLyric: str


class countIn(BaseModel):
    text: str


def count_words_and_lines(model: countIn):
    text_to_count = model.text
    lines = text_to_count.split("\n")
    lines_count = len(lines)
    words_count_aux = list(map(lambda line: len(line.split()), lines))
    words_count = sum(words_count_aux)
    return(lines_count, words_count)
