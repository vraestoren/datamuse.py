from requests import Session

class Datamuse:
	def __init__(self) -> None:
		self.api = "https://api.datamuse.com"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

	def _get(self, endpoint: str, params: dict = None) -> dict:
		return self.session.get(
			f"{self.api}{endpoint}", params=params or {}).json()

	def _build_params(self, **kwargs) -> dict:
		return {
			key: value for key, value in kwargs.items() if value is not None}

	def get_words(
			self,
			ml: str = None,
			sl: str = None,
			sp: str = None,
			rel_jja: str = None,
			rel_jjb: str = None,
			rel_syn: str = None,
			rel_ant: str = None,
			rel_trg: str = None,
			rel_spc: str = None,
			rel_gen: str = None,
			rel_com: str = None,
			rel_par: str = None,
			rel_bga: str = None,
			rel_bgb: str = None,
			rel_rhy: str = None,
			rel_nry: str = None,
			rel_hom: str = None,
			rel_cns: str = None,
			v: str = None,
			topics: str = None,
			lc: str = None,
			rc: str = None,
			max: int = None,
			md: str = None,
			qe: str = None) -> dict:
		params = self._build_params(
			ml=ml,
			sl=sl,
			sp=sp,
			rel_jja=rel_jja,
			rel_jjb=rel_jjb,
			rel_syn=rel_syn,
			rel_ant=rel_ant,
			rel_trg=rel_trg,
			rel_spc=rel_spc,
			rel_gen=rel_gen,
			rel_com=rel_com,
			rel_par=rel_par,
			rel_bga=rel_bga,
			rel_bgb=rel_bgb,
			rel_rhy=rel_rhy,
			rel_nry=rel_nry,
			rel_hom=rel_hom,
			rel_cns=rel_cns,
			v=v,
			topics=topics,
			lc=lc,
			rc=rc,
			max=max,
			md=md,
			qe=qe
		)
		return self._get("/words", params)

	def get_similar_words(self, word: str, max: int = None) -> dict:
		return self.get_words(ml=word, max=max)

	def get_words_that_starts_with(
			self,
			word: str,
			starts_with: str,
			max: int = None) -> dict:
		return self.get_words(ml=word, sp=f"{starts_with}*", max=max)

	def get_words_that_ends_with(
			self,
			word: str,
			ends_with: str,
			max: int = None) -> dict:
		return self.get_words(ml=word, sp=f"*{ends_with}", max=max)

	def get_words_that_sounds_like(
			self, word: str, max: int = None) -> dict:
		return self.get_words(sl=word, max=max)

	def get_words_spelled_like(
			self, pattern: str, max: int = None) -> dict:
		return self.get_words(sp=pattern, max=max)

	def get_words_that_rhyme_with(
			self, word: str, max: int = None) -> dict:
		return self.get_words(rel_rhy=word, max=max)

	def get_near_rhymes(
			self, word: str, max: int = None) -> dict:
		return self.get_words(rel_nry=word, max=max)

	def get_word_adjectives(
			self, word: str, max: int = None) -> dict:
		return self.get_words(rel_jjb=word, max=max)

	def get_word_nouns(
			self, word: str, max: int = None) -> dict:
		return self.get_words(rel_jja=word, max=max)

	def get_synonyms(
			self, word: str, max: int = None) -> dict:
		return self.get_words(rel_syn=word, max=max)

	def get_antonyms(
			self, word: str, max: int = None) -> dict:
		return self.get_words(rel_ant=word, max=max)

	def get_words_triggered_by(
			self, word: str, max: int = None) -> dict:
		return self.get_words(rel_trg=word, max=max)

	def get_homophones(
			self, word: str, max: int = None) -> dict:
		return self.get_words(rel_hom=word, max=max)

	def get_words_that_follow(
			self, word: str, max: int = None) -> dict:
		return self.get_words(rel_bga=word, max=max)

	def get_words_that_precede(
			self, word: str, max: int = None) -> dict:
		return self.get_words(rel_bgb=word, max=max)

	def get_suggestions(
			self, word: str, max: int = None) -> dict:
		params = self._build_params(s=word, max=max)
		return self._get("/sug", params)
