# coding=utf-8
from bs4 import BeautifulSoup

import re


class GetText():
    u"""Klasse zum Herauslesen der Repliken für die Beziehungen."""

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
        :return: Suppe wird zurückgegeben
        """
        soup = BeautifulSoup(tei, 'html.parser')
        return soup

    def drama_total(self, soup):
        u"""
        Gibt komplettes Drama zurück.

        :param soup:  Suppe der TEI-Datei
        :return: bs-Liste des kompletten Dramas
        """
        return soup.find_all('sp')

    def drama_act(self, soup, which_act):
        u"""
        Gibt einzelne Akte zurück.

        :param soup:  Suppe der TEI-Datei
        :param which_act: Eingegebner Akt
        :return: bs-Liste des gewählten Akts
        """
        div = soup.find_all('div', type='act')
        act = div[which_act].find_all('sp')
        return act

    def how_many_acts(self, soup):
        u"""
        Gibt zurück wie viele Akte ein Drama hat.

        :param soup: Suppe
        :return: Anzahl der Akte
        """
        div = soup.find_all('div', type='act')
        return len(div)

    def fill_replik_dict_p(self, act, replik):
        u"""
        Füllt Nested-Dictionary.

        Repliken werden zu InnerKeys mit Value 0

        :param act: TEI-Datei als bs-Liste
        :param replik: Dictionary mit Beziehung als OuterKey
        :return: Dictionary mit Repliken als InnerKey
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
                            # Abfrage auf Handshake: Wenn Sprecher1 = Sprecher3 -- Sprecher 2 spricht zu Sprecher 1
                            if i + 2 < len(act):
                                if type(act[i + 2].speaker) is not type(None):
                                    if act[i].speaker.text == act[i + 2].speaker.text:
                                        text = act[i + 1].p.text
                                        if dict_name in replik:
                                            replik[dict_name][text] = 0
                            else:
                                text = act[i + 1].p.text
                                if dict_name in replik:
                                    replik[dict_name][text] = 0
            i += 1
        return replik

    def fill_replik_dict_lg(self, act, replik):
        u"""
        Füllt Nested-Dictionary.

        Repliken werden zu InnerKeys mit Value 0

        :param act: TEI-Datei als bs-Liste
        :param replik: Dictionary mit Beziehung als OuterKey
        :return: Dictionary mit Repliken als InnerKey
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
                            # Abfrage auf Handshake: Wenn Sprecher1 = Sprecher3 -- Sprecher 2 spricht zu Sprecher 1
                            if i + 2 < len(act):
                                if type(act[i + 2].speaker) is not type(None):
                                    if act[i].speaker.text == act[i + 2].speaker.text:
                                        text = act[i + 1].lg.text
                                        if dict_name in replik:
                                            replik[dict_name][text] = 0
                            else:
                                text = act[i + 1].lg.text
                                if dict_name in replik:
                                    replik[dict_name][text] = 0
            i += 1
        return replik

    def which_type(self, act, replik):
        u"""
        Entscheidet welche fill_replik-Funktion aufgerufen wird.

        :param act: TEI-Datei als bs-Liste
        :param replik: Dictionary mit Beziehung als OuterKey
        :return: Dictionary mit Repliken als InnerKey
        """
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
