from tqdm import tqdm
from textblob_de import TextBlobDE as tb


class GetSentiment():

    def get_sentis(self, replik):
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
