"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    Measure sentence-length variation using the coefficient
    of variation: standard deviation divided by mean length.

    Returns 0.0 when fewer than two nonempty sentences exist.
    Higher values indicate greater variation.
    """
    lengths = [
        len(words(sentence))
        for sentence in sentences(text)
    ]

    lengths = [length for length in lengths if length > 0]

    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)

    if mean_length == 0:
        return 0.0

    return round(statistics.stdev(lengths) / mean_length, 4)


def type_token_ratio(text: str) -> float:
    """
    Measure vocabulary diversity using unique words divided
    by total words.

    Returns a value between 0.0 and 1.0.
    Returns 0.0 when no words are present.
    Higher values indicate greater vocabulary diversity.
    """
    tokens = words(text)

    if not tokens:
        return 0.0

    unique_words = len(set(tokens))
    total_words = len(tokens)

    return round(unique_words / total_words, 4)


def punctuation_density(text: str) -> float:
    """
    Measure punctuation relative to non-whitespace characters.

    Includes ASCII punctuation and common Unicode punctuation.
    Returns 0.0 for empty or whitespace-only text.
    Higher values indicate greater punctuation density.
    """
    import string
    import unicodedata

    characters = [char for char in text if not char.isspace()]

    if not characters:
        return 0.0

    punctuation_count = sum(
        1
        for char in characters
        if char in string.punctuation
        or unicodedata.category(char).startswith("P")
    )

    return round(punctuation_count / len(characters), 4)

# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    Combine three stylometry measurements into a conservative
    AI-likeness score between 0.0 and 1.0.

    Higher values indicate more AI-like writing patterns.
    The score is a heuristic, not proof of authorship.
    """
    tokens = words(text)
    sentence_list = [
        sentence for sentence in sentences(text)
        if words(sentence)
    ]

    if len(tokens) < 30 or len(sentence_list) < 2:
        return 0.5

    spread = sentence_length_spread(text)
    diversity = type_token_ratio(text)
    punctuation = punctuation_density(text)

    spread_ai = 1.0 - min(spread / 0.8, 1.0)
    diversity_ai = 1.0 - min(diversity / 0.8, 1.0)

    punctuation_ai = 0.5

    if punctuation < 0.02:
        punctuation_ai = 0.6
    elif punctuation > 0.20:
        punctuation_ai = 0.4

    raw_score = (
        0.45 * spread_ai
        + 0.40 * diversity_ai
        + 0.15 * punctuation_ai
    )

    score = 0.5 + 0.5 * (raw_score - 0.5)

    return round(max(0.0, min(1.0, score)), 4)

if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
