from typing import List

from yake import KeywordExtractor


def get_keywords(raw_text: str) -> List[str]:
    keywords = KeywordExtractor(
        n=3, dedupLim=0.1, top=7,
    ).extract_keywords(raw_text)
    return [phrase for phrase, _ in keywords]
