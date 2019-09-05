# coding=utf-8
import networkx as nx
from bs4 import BeautifulSoup

class Graphdaten():

    def get_nodes(self, csv_drama):
        characternames = []
        for character in csv_drama:
            if character[0] not in characternames:
                characternames.append(character[0])
            if character[2] not in characternames:
                characternames.append(character[2])
        
        return characternames


    def get_edges(self, all_in_all, gesprocheneworte):
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
        nodes = []
        person = soup.find_all('person')
        for c in characternames:
            for index in range(len(person)):
                if c in person[index]['xml:id']:
                    sex = person[index]['sex']
            nodes.append({'name': c, 'sex': sex})

        return nodes


    def get_ids(self, characternames):
        ids = {}
        j = 0
        for cn in characternames:
            if cn not in ids:
                ids[cn]= j
                j = j+1

        return ids

    def get_links(self, edges, ids):
        links = []
        for u in edges:
            if u[0] in ids and u[1] in ids:
                links.append({'source': ids[u[0]], 'target': ids[u[1]], 'senti': u[2], 'worte': u[3] })

        return links

    def get_json_dict(self, links, nodes):
        data = {'nodes': nodes, 'links': links}

        return data
