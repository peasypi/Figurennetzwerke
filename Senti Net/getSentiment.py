import spacy
from spacy_sentiws import spaCySentiWS
from spacy.lang.de.stop_words import STOP_WORDS
import re
from tqdm import tqdm
# from textblob_de import TextBlobDE as tb


class GetSentiment():

    nlp = spacy.load('de')
    sentiws = spaCySentiWS(sentiws_path='/Users/pia/Desktop/SentiWS_v2.0/')
    nlp.add_pipe(sentiws)

    def get_sentis(self, replik):
        for key in tqdm(replik):
            for innerkey in replik[key]:
                text = re.sub(r"\.{0,3},*!*\?*-*", "", innerkey)
                text = self.nlp(text)
                textwostop = ""
                senti = 0
                tokenanzahl = 0
                # replik[key][innerkey] = senti.sentiment.polarity
                for token in text:
                    if str(token) not in STOP_WORDS:
                        textwostop = textwostop + " " + str(token)
                textwostop = self.nlp(textwostop)
                for tok in textwostop:
                    lemma = tok.lemma_
                    lemma = self.nlp(lemma)
                    for lem in lemma:
                        if lem._.sentiws is None:
                            tokenanzahl = tokenanzahl + 1
                        else:
                            senti = senti + lem._.sentiws
                            tokenanzahl = tokenanzahl + 1
                if len(list(text)) == 1:
                    tokenanzahl = tokenanzahl - 1
                # replik[key][innerkey] = senti / tokenanzahl
                replik[key][innerkey] = senti
        return replik

    def average_senti(self, replik):
        all_in_all = {}
        for key in replik:
            gesamtsentiment = 0
            anzahlreplik = 0
            for innerkey, value in replik[key].items():
                    anzahlreplik = anzahlreplik + 1
                    gesamtsentiment = (gesamtsentiment + value)
                    # all_in_all[key] = gesamtsentiment / anzahlreplik
                    all_in_all[key] = gesamtsentiment
        return all_in_all

    def gesprocheneworte(self, replik):
        gesprocheneworte = {}
        for key in replik:
            anzahlworte = 0
            for innerkey in replik[key]:
                for wort in innerkey.split():
                    anzahlworte += 1
            if anzahlworte == 0:
                pass
            else:
                gesprocheneworte[key] = anzahlworte

        return gesprocheneworte

'''def get_sentis(self, replik):
        for key in tqdm(replik):
            for innerkey in replik[key]:
                senti = tb(innerkey)
                replik[key][innerkey] = senti.sentiment.polarity
        return replik


    def average_senti(self,replik):
        all_in_all = {}
        for key in replik:
            x = 0
            for innerkey, value in replik[key].items():
                x = (x + value)
                all_in_all[key] = x
        for key, value in all_in_all.items():
            all_in_all[key] = value / len(replik[key])
        return all_in_all
'''
