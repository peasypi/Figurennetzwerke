u"""Semantischen Analyse eines Dramas in sozialen Netzwerkgraphen."""
from pyfiglet import Figlet
from getData import GetData
from getText import GetText
from getSentiment import GetSentiment
from Graphdaten import Graphdaten
# from graphMalen import GraphMalen
from helpFunction import HelpFunction

import click
import os


@click.command()
@click.option('--dramaname', help='Name des Dramas.')
@click.option('--autor', help='Nachname des Autors.')
@click.option('--act', help='Akt des Dramas.')


def main(dramaname, autor, act):
    u"""Main zum Ausführen des Programms."""
    gd = GetData()
    gt = GetText()
    gs = GetSentiment()
    # gm = GraphMalen()
    graph = Graphdaten()

    if dramaname:
        dramaname = dramaname
    else:
        dramaname = click.prompt('Gib den Namen eines Dramas ein')
    if autor:
        autor = autor
    else:
        autor = click.prompt('Gib den Nachnamen des Autors ein')
    draname = gd.eingabe_drama(dramaname, autor)
    tei = gd.get_tei(draname)
    csv_drama = gd.get_csv(draname)
    replik = gt.create_replik_dict(csv_drama)
    soup = gt.stir_the_soup(tei)
    if act:
        pass
    else:
        print("Das ausgewählte Drama hat {} Akte".format(gt.how_many_acts(soup)))
        act = click.prompt('Gib den Akt ein, den du analysieren willst (falls du das Netzwerk für das gesamte Drama haben möchtest, wähle 0)')
    which_act = int(act) - 1
    if which_act == -1:
        total = gt.drama_total(soup)
        replik = gt.which_type(total, replik)
    else:
        act = gt.drama_act(soup, which_act)
        replik = gt.which_type(act, replik)
    # act = drama_act(soup, which_act)
    # replik = fillReplik_dic(act, replik)
    replik = gs.get_sentis(replik)
    all_in_all = gs.average_senti(replik)
    gesprocheneworte = gs.gesprocheneworte(replik)
    characternames = graph.get_nodes(csv_drama)
    edges = graph.get_edges(all_in_all, gesprocheneworte)
    nodes = graph.get_sex(characternames, soup)
    ids = graph.get_ids(characternames)
    links = graph.get_links(edges, ids)
    ''' Ab dem Punkt, weiß ich nicht so richtig, was zutun ist..
        -> irgendwie mit Flask verbinden, sollte wahrscheinlich kein Problem
        für dich sein! x3'''
    data = graph.get_json_dict(links, nodes)
    print(data)
    # nodes = gm.get_nodes(csv_drama)
    # edges = gm.get_edges(all_in_all)
    # labels_edges = gm.get_labels(edges)
    # graph = gm.graph(edges, nodes)
    # gm.malen(graph, labels_edges, draname, which_act + 1)
    os.system('clear')
    menu()


def menu():
    u"""Erstellt Cli Menü."""
    hf = HelpFunction()
    menu_items = [
        {"Drama analysieren": main},
        {"Help": hf.hilfe},
        {"Exit": exit},
    ]
    while True:
        os.system('clear')
        f = Figlet(font='roman')
        print(hf.colorize(str(f.renderText('Senti Net')), 'b'))
        print(hf.colorize("Version 2.0, jetzt auch endlich mit SentiWS \n", 'c'))
        # Print some badass ascii art header here !
        for item in menu_items:
            for key, value in item.items():
                print (hf.colorize("[{}]: {}".format(str(menu_items.index(item)), key), 'y'))
        choice = input(hf.colorize(">> ", 'b'))
        try:
            if int(choice) < 0:
                raise ValueError
            # Call the matching function
            list(menu_items[int(choice)].values())[0]()
        except (ValueError, IndexError):
            pass

if __name__ == '__main__':
    menu()
