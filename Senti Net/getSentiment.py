import spacy
from spacy_sentiws import spaCySentiWS
# from tqdm import tqdm
# from textblob_de import TextBlobDE as tb


class GetSentiment():

    nlp = spacy.load('de')
    sentiws = spaCySentiWS(sentiws_path='/Users/pia/Desktop/SentiWS_v2.0/')
    nlp.add_pipe(sentiws)

    def get_sentis(self, replik):
        for key in replik:
            for innerkey in replik[key]:
                text = self.nlp(innerkey)
                senti = 0
                l = 0
                # replik[key][innerkey] = senti.sentiment.polarity
                for token in text:
                    if token._.sentiws is not None:
                        l = l + 1
                        senti = senti + token._.sentiws
                        replik[key][innerkey] = senti / l
        return replik

    def average_senti(self, replik):
        all_in_all = {}
        for key in replik:
            x = 0
            le = 0
            for innerkey, value in replik[key].items():
                if value != 0:
                    le = le + 1
                    x = (x + value)
                    all_in_all[key] = x / le
        return all_in_all


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
