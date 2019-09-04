import networkx as nx
import matplotlib.pyplot as plt


class GraphMalen():

    def get_nodes(self, csv_drama):
        nodes = []
        for character in csv_drama:
            if character[0] not in nodes:
                nodes.append(character[0])
            if character[2] not in nodes:
                nodes.append(character[2])
        return nodes

    def get_edges(self, all_in_all):
        edges = []
        for key, value in all_in_all.items():
            edges.append(key.split("-"))
        nils = 0
        while nils < len(edges):
            for key, value in all_in_all.items():
                edges[nils].append(value)
                nils += 1
        return edges

    def get_labels(self, edges):
        labels_edges = {}
        for e in edges:
            labels_edges[(e[0], e[1])] = round(e[2], 3)
        return labels_edges

    def graph(self, edges, nodes):

        g = nx.MultiDiGraph()

        for node in nodes:
            g.add_node(node)

        for edge in edges:
            g.add_edge(edge[0], edge[1])

        return g

    def malen(self, g, labels_edges, draname, which_act):

        fig = plt.figure(figsize=(12, 12))
        ax = plt.subplot(111)
        temp = ""
        titel = ""
        for wort in draname.split('-'):
            temp = temp + " " + wort.upper()
        temp = temp.split(' ')
        temp.insert(2, ":")
        for wort in temp:
            titel = titel + wort + " "
        titel = "{}, AKT {}".format(titel, which_act)
        ax.set_title(titel, fontsize=20, color='#088A68')

        pos = nx.shell_layout(g)
        nx.draw(g, pos, edge_color='black', width=1, linewidths=1,
                node_size=500, node_color='#F7D358', alpha=0.9,
                labels={node: node for node in g.nodes()})
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels_edges,
                                     label_pos=0.3, font_color='#088A68')

        plt.tight_layout()
        plt.savefig("/Users/Nils/Desktop/{}_Akt{}.png".format(draname, which_act), format="PNG")
        plt.show()
