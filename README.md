# <div align="center"> <img src="https://www.datamuse.com/api/datamuse-logo-rgb.png" width="200" style="vertical-align:middle;" /> datamuse.py </div>

> Web-API for [Datamuse](https://www.datamuse.com/api) a word-finding query engine for developers. Find words by meaning, sound, spelling, rhyme, and linguistic relationships.


## Quick Start
```python
from datamuse import Datamuse

datamuse = Datamuse()

# Find words similar in meaning to "ocean"
print(datamuse.get_similar_words("ocean"))

# Find rhymes for "love"
print(datamuse.get_words_that_rhyme_with("love"))

# Autocomplete suggestions for "hap"
print(datamuse.get_suggestions("hap"))
```

---

## Words

| Method | Description |
|--------|-------------|
| `get_words(...)` | Raw query with full control over all API params |
| `get_similar_words(word, max)` | Words with similar meaning |
| `get_synonyms(word, max)` | Synonyms of a word |
| `get_antonyms(word, max)` | Antonyms of a word |
| `get_words_that_sounds_like(word, max)` | Words that sound similar |
| `get_words_spelled_like(pattern, max)` | Words matching a spelling pattern |
| `get_words_that_starts_with(word, starts_with, max)` | Words meaning `word` and starting with a prefix |
| `get_words_that_ends_with(word, ends_with, max)` | Words meaning `word` and ending with a suffix |
| `get_words_that_rhyme_with(word, max)` | Perfect rhymes |
| `get_near_rhymes(word, max)` | Near rhymes |
| `get_homophones(word, max)` | Words that sound identical |
| `get_word_adjectives(word, max)` | Adjectives commonly used to describe a noun |
| `get_word_nouns(word, max)` | Nouns commonly modified by an adjective |
| `get_words_triggered_by(word, max)` | Words statistically associated with a word |
| `get_words_that_follow(word, max)` | Words that frequently follow a word |
| `get_words_that_precede(word, max)` | Words that frequently precede a word |
| `get_suggestions(word, max)` | Autocomplete suggestions |

---

## `get_words` Parameters

| Parameter | Description |
|-----------|-------------|
| `ml` | Meaning like — words with similar meaning |
| `sl` | Sounds like — phonetic similarity |
| `sp` | Spelled like — supports wildcards (`*`, `?`) |
| `rel_syn` | Synonyms |
| `rel_ant` | Antonyms |
| `rel_jja` | Nouns modified by an adjective |
| `rel_jjb` | Adjectives that modify a noun |
| `rel_trg` | Words triggered by / associated with |
| `rel_spc` | More specific than (hyponyms) |
| `rel_gen` | More general than (hypernyms) |
| `rel_com` | Comprises / part-of |
| `rel_par` | Part of / comprises |
| `rel_bga` | Words that frequently follow |
| `rel_bgb` | Words that frequently precede |
| `rel_rhy` | Perfect rhymes |
| `rel_nry` | Near rhymes |
| `rel_hom` | Homophones |
| `rel_cns` | Consonant match |
| `topics` | Bias results toward a topic (comma-separated) |
| `lc` | Left context — word that appears to the left |
| `rc` | Right context — word that appears to the right |
| `v` | Vocabulary — e.g. `enwiki` for Wikipedia |
| `md` | Metadata flags: `d` definitions, `p` parts of speech, `s` syllables, `r` pronunciation, `f` frequency |
| `qe` | Query echo — repeat a constraint field in the response |
| `max` | Maximum number of results (default: `100`) |

---

## Spelling Patterns (`sp`)

| Pattern | Matches |
|---------|---------|
| `b*` | Words starting with `b` |
| `*ing` | Words ending with `ing` |
| `b*ing` | Words starting with `b` and ending with `ing` |
| `b??` | Words starting with `b` with exactly 3 letters |
