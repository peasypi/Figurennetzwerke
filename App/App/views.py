from App import app
from App.getData import GetData
from App.getText import GetText
from App.getSentiment import GetSentiment
from App.Graphdaten import Graphdaten
from flask import render_template, request

import json


@app.route('/')
def index():
    u"""Übergibt Daten der Json-Datei an Javascript."""
    with open("App/data1.json", "r") as json_file:
        data = json.load(json_file)
    return render_template("Graphnetz_v3.html", data=data)


@app.route('/', methods=['POST'])
def my_form_post():
    u"""
    Fügt Daten des analysierenden Dramas zur Json-Datei hinzu.

    Bekommt Namen, Autor und Akt des zu analysierenden Dramas
    """
    gd = GetData()
    name = request.form['Name']
    autor = request.form['Autor']
    actauswahl = request.form['Akt']
    draname = gd.eingabe_drama(name, autor)
    input_data = sentinet(draname, actauswahl)
    with open("App/data1.json", "r") as json_file:
        data = json.load(json_file)
        data.append(input_data)
    return render_template("Graphnetz_v3.html", data=data)


def sentinet(draname, actauswahl):
    u"""
    Führt Programm aus.

    :param draname: Name+Autor des Dramas
    :param actauswahl: ausgewählter Akt
    :return: Json-like-Data
    """
    gd = GetData()
    gt = GetText()
    gs = GetSentiment()
    graph = Graphdaten()
    # act = 0
    tei = gd.get_tei(draname)
    csv_drama = gd.get_csv(draname)
    replik = gt.create_replik_dict(csv_drama)
    soup = gt.stir_the_soup(tei)
    which_act = int(actauswahl) - 1
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

    data = graph.get_json_dict(links, nodes)
    return data
