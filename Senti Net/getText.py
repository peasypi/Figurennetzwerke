from bs4 import BeautifulSoup

import re


class GetText():

    def create_replik_dict(self, csv_drama):
        u"""
        Erstellt ein Nested-Dictionary mit Figurenbeziehungen als Key.

        :param draname: Name und Autor des Dramas in richtigem Format
        :param csv_drama: CSV-Datei als CSV-Liste
        :return: CSV-Datei als CSV-Liste
        """
        replik = {}
        for character in csv_drama:
            replik["{}-{}".format(character[0], character[2])] = {}
            replik["{}-{}".format(character[2], character[0])] = {}
        return replik

    def stir_the_soup(self, tei):
        u"""
        Verwandelt tei-String in eine Suppe.

        :param tei: TEI-Datei als String
        :param sp: Schöne Suppe
        :return: Suppe wird zurückgegeben
        """
        soup = BeautifulSoup(tei, 'html.parser')
        return soup

    def drama_total(self, soup):
        return soup.find_all('sp')

    def drama_act(self, soup, which_act):
        div = soup.find_all('div', type='act')
        act = div[which_act].find_all('sp')
        return act

    def how_many_acts(self, soup):
        div = soup.find_all('div', type='act')
        return len(div)

    def fill_replik_dict_p(self, act, replik):
        u"""
        Füllt Nested-Dictionary.

        Repliken werden zu InnerKeys mit Value 0

        :param tei: TEI-Datei als String
        :param sp: Schöne Suppe
        :return: Suppe wird zurückgegeben
        """
        i = 0
        while i < len(act):
            if type(act[i].speaker) is not type(None):
                if i + 1 < len(act):
                    if type(act[i + 1].speaker) is not type(None):
                        if type(act[i + 1].p) is not type(None):
                            speaker1 = act[i].speaker.text
                            speaker1 = re.sub(r"\.", '', speaker1.lower())
                            speaker1 = re.sub(r" ", '_', speaker1.lower())
                            speaker2 = act[i + 1].speaker.text
                            speaker2 = re.sub(r"\.", '', speaker2.lower())
                            speaker2 = re.sub(r" ", '_', speaker2.lower())
                            dict_name = "{}-{}".format(speaker2, speaker1)
                            text = act[i + 1].p.text
                            if dict_name in replik:
                                replik[dict_name][text] = 0
            i += 1
        return replik

    def fill_replik_dict_lg(self, act, replik):
        u"""
        Füllt Nested-Dictionary.

        Repliken werden zu InnerKeys mit Value 0

        :param tei: TEI-Datei als String
        :param sp: Schöne Suppe
        :return: Suppe wird zurückgegeben
        """
        i = 0
        while i < len(act):
            if type(act[i].speaker) is not type(None):
                if i + 1 < len(act):
                    if type(act[i + 1].speaker) is not type(None):
                        if type(act[i + 1].lg) is not type(None):
                            speaker1 = act[i].speaker.text
                            speaker1 = re.sub(r"\.", '', speaker1.lower())
                            speaker1 = re.sub(r" ", '_', speaker1.lower())
                            speaker2 = act[i + 1].speaker.text
                            speaker2 = re.sub(r"\.", '', speaker2.lower())
                            speaker2 = re.sub(r" ", '_', speaker2.lower())
                            dict_name = "{}-{}".format(speaker2, speaker1)
                            text = act[i + 1].lg.text
                            if dict_name in replik:
                                replik[dict_name][text] = 0
            i += 1
        return replik

    def which_type(self, act, replik):
        l = 0
        lg_list = []
        p_list = []
        while l < len(act):
            if type(act[l].lg) is not type(None):
                lg_list.append(act[l].lg)
            if type(act[l].p) is not type(None):
                p_list.append(act[l].p)
            l = l + 1

        if len(lg_list) > len(p_list):
            replik = self.fill_replik_dict_lg(act, replik)
        else:
            replik = self.fill_replik_dict_p(act, replik)

        return replik

    '''def fill_replik_dict(self, sp, replik):
        u"""
        Füllt Nested-Dictionary.

        Repliken werden zu InnerKeys mit Value 0

        :param tei: TEI-Datei als String
        :param sp: Schöne Suppe
        :return: Suppe wird zurückgegeben
        """
        i = 0
        while i < len(sp):
            if type(sp[i].speaker) is not type(None):
                if i + 1 < len(sp):
                    if type(sp[i + 1].speaker) is not type(None):
                        if type(sp[i + 1].lg) is not type(None):
                            speaker1 = sp[i].speaker.text
                            speaker1 = re.sub(r"\.", '', speaker1.lower())
                            speaker1 = re.sub(r" ", '_', speaker1.lower())
                            speaker2 = sp[i + 1].speaker.text
                            speaker2 = re.sub(r"\.", '', speaker2.lower())
                            speaker2 = re.sub(r" ", '_', speaker2.lower())
                            dict_name = "{}-{}".format(speaker2, speaker1)
                            text = sp[i + 1].lg.text
                            if dict_name in replik:
                                replik[dict_name][text] = 0
            i += 1
        return replik'''
