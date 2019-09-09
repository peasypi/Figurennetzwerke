# coding=utf-8
from bs4 import BeautifulSoup


class Graphdaten():
    u"""Klasse zur Erstellung der Graphdaten."""

    def get_nodes(self, csv_drama):
        u"""
        Speichert Charakternamen in einer Liste.

        :param csv_drama: CSV-Datei als Liste
        :return: Liste der Charakternamen
        """
        characternames = []
        for character in csv_drama:
            if character[0] not in characternames:
                characternames.append(character[0])
            if character[2] not in characternames:
                characternames.append(character[2])
        return characternames

    def get_edges(self, all_in_all, gesprocheneworte):
        u"""
        Speichert Kanten in einer Liste.

        Source, Target, Sentimentwert und gesprochene Worte.

        :param all_in_all: Dictionary mit Beziehungen und deren Sentimentwerte
        :param gesprocheneworte: Dictionary mit Beziehungen & gesprochenen Worten
        :return: Liste der Kanten
        """
        edges = []
        for key, value in all_in_all.items():
            edges.append(key.split("-"))
        nils = 0
        while nils < len(edges):
            for key, value in all_in_all.items():
                edges[nils].append(value)
                nils += 1
        pia = 0
        for key, value in gesprocheneworte.items():
            edges[pia].append(value)
            pia += 1
        return edges

    def get_sex(self, characternames, soup):
        u"""
        Speichert Geschlecht und Namen der Charaktere in einer Knoten-Liste.

        :param characternames: Liste der Charakternamen
        :param soup: TEI-Datei als Suppe
        :return: Liste der Knoten
        """
        nodes = []
        person = soup.find_all('person')
        for c in characternames:
            for index in range(len(person)):
                if c in person[index]['xml:id']:
                    sex = person[index]['sex']
            nodes.append({'name': c, 'sex': sex})

        return nodes

    def get_ids(self, characternames):
        u"""
        Ordnet Namen einen ID zu.

        :param characternames: Liste der Charakternamen
        :return: Dictionary with Charakternamen + Ids
        """
        ids = {}
        j = 0
        for cn in characternames:
            if cn not in ids:
                ids[cn] = j
                j = j + 1

        return ids

    def get_links(self, edges, ids):
        u"""
        Erstellt Liste der Kanten in benötigter Art.

        :param edges: Liste der Kanten
        :param ids: Dictionary mit Ids
        :return: Liste der Links
        """
        links = []
        for u in edges:
            if u[0] in ids and u[1] in ids:
                links.append({'source': ids[u[0]], 'target': ids[u[1]], 'senti': u[2], 'worte': u[3]})

        return links

    def get_json_dict(self, links, nodes):
        u"""
        Erstellt Json-Data.

        :param links: Liste der Links
        :param nodes: Liste der Knoten
        :return: Json-Data
        """
        data = {'nodes': nodes, 'links': links}

        return data
