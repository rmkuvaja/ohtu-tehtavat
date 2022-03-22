HINTA = 5
SUMMA = 5

class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti):
        kortti.lataa(SUMMA)

    def osta_lounas(self, kortti):
        kortti.osta(HINTA)
        self.myytyja_lounaita = self.myytyja_lounaita + 1
