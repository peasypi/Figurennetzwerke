# coding=utf-8
import requests
import re


class GetData():
    u"""Klasse zum Crawlen der Daten."""

    def eingabe_drama(self, dramaname, autor):
        u"""
        Liest den Dramen- und Autorennamen ein.

        Ändert das Format, sodass beides in den Link für CSV & TEI eingefügt
        werden können

        :param dramaname: Name des ausgewählten Dramas
        :param autor: Nachname des Autoren des Dramas
        :return: String in richtigem Format
        """
        name = re.sub(r' ', "-", dramaname.lower())
        draname = autor.lower() + "-" + name
        return draname

    def get_tei(self, draname):
        u"""
        Crawlt TEI-Datei des Dramas von DraCor.

        :param draname: Name und Autor des Dramas in richtigem Format
        :param tei: TEI-Datei als String
        :return: TEI-Datei als String
        """
        headers_tei = {
            'accept': 'application/xml'
        }

        response_tei = requests.get('https://dracor.org/api/corpora/ger/play/{}/tei'.format(draname), headers=headers_tei, stream=True)
        tei = response_tei.text
        return tei

    def get_csv(self, draname):
        u"""
        Crawlt CSV-Datei des Social Networks des Dramas von DraCor.

        :param draname: Name und Autor des Dramas in richtigem Format
        :param csv_drama: CSV-Datei als CSV-Liste
        :return: CSV-Datei als CSV-Liste
        """
        headers_csv = {
            'accept': 'text/csv'
        }
        response_csv = requests.get('https://dracor.org/api/corpora/ger/play/{}/networkdata/csv'.format(draname), headers=headers_csv)
        csv_download = response_csv.text
        csv_download = csv_download.split('\n')
        csv_drama = []
        knypsolon = 1

        while knypsolon < len(csv_download):
            x = csv_download[knypsolon].split(',')
            csv_drama.append(x)
            knypsolon = knypsolon + 1

        return csv_drama
