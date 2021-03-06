﻿# Rechercheergebnisse

## SentiWS - SentimentWortschatz der Universität Leipzig 

R. Remus, U. Quasthoff & G. Heyer: SentiWS - a Publicly Available German-language Resource for Sentiment Analysis.
In: Proceedings of the 7th International Language Ressources and Evaluation (LREC'10), pp. 1168-1171, 2010

- kurz für SentimentWortschatz
- beinhaltet Wörter mit positivem oder negativem Sentiment in Intervall von [-1;1] mit vier Nachkommastellen und PoS-Tag 
- Adjektive und Adverben, die explizit Sentiment enthalten; Nomen und Verben, die implizit Sentiment enthalten 
- ein Wort kann verschiedene Einträge, bspw. nach PoS, haben
- wichtig zu beachten, dass Wertigkeit von Worten je nach Kontext unterschiedlich ist 
- Aufbau des Wörterbuches

 Wort | POS Tag | Weight  | Flexionen       
---|---|---|---
 harmonisch  | ADJX        | +0.5243      | harmonische 
 Krise       | NN          | -0.3631      | Krisen          

- Quellen: 
	- **General Inquirer (GI) lexicon** 
		- ins Deutsche übersetzt mithilfe von Google Übersetzer und danach manuell aussortiert 
	- **Kookkurrenzanalyse** 
		- Kundenrezensionen, die von den Autoren selbst als sehr positiv oder sehr negativ getagged wurden 
		- aus je 5100 positiven und negativen Reviews wurden Wörter mit einer besonders hohen Häufigkeit getaggt ('Marker') und mithilfe von Kookkurrenzanalyse Wörter mit ähnlichem Sentiment in Relation zum Marker ermittelt und per Hand selektiert (sinnvoll für "domain-dependent terminology", z.B. Kundenrezensionen - Reklamation, Fehlkauf, etc.)
	- **Wörterbuch der Kollokationen im Deutschen** 
		- Wörterbuch, welches Worte nach semantischer Ähnlichkeit zusammenstellt (ruhmreich + Ära)
		- mithilfe der vorangegangenen Quellen wurden die Basis-Wörter (vgl. Quasthoff 2010), in diesem Beispiel Ära, eingeteilt in zwei Gruppen: 
			- zusammenhängend mit Sentiment und unzusammenhängend mit Sentiment 
		- Wörter mit sehr seltener Häufigkeit konnten so ermittelt werden (sonnendurchflutet, bärenstark)
- Gewichtung der Sentimente wird berechnet durch *Pointwise Mutual Information* (PMI) (vgl. Turney & Littman)
- zipf'sche Verteilung der Sentimente:
	- geringe Anzahl an Wörtern mit hoher Gewichtung (d.h. sehr positiv/sehr negativ) 
	- hohe Anzahl an Wörtern mit mittlerer Gewichtung 
- Evaluation: 
	- bessere Leistung bei negativen Worten (F = 0.86) als bei positiven Wortformen (F = 0.82) 
	- häufige Fehler bei fehlenden Wörtern und Wortformen (Domänen-spezifisches Vokabular, Fremdwörter, Umgangssprache, Fehlschreibweise) 

## Contextual valence shifters

Polanyi L., Zaenen A. (2006) Contextual Valence Shifters. In: Shanahan J.G., Qu Y., Wiebe J. (eds) Computing Attitude and Affect in Text: Theory and Applications. The Information Retrieval Series, vol 20. Springer, Dordrecht

- Verstärkerungswörter, Superlative, Steigerungen
- Modaloperatoren, bspw. möglicherweise schwächen ein Wort, können neutralisieren
- so sind Wörter wie bspw. "sogar" oder "knapp" so markiert, dass sie Einfluss auf die Wertigkeit der nachfolgenden Wörter haben 
- Beispiel Kundenrezension: ein negativer Aspekt, der lange diskutiert wird, aber kurze Auflistung vieler positiver Aspekte 
- Nutzung "evaluierender Sprache" kann Indiz dafür sein, dass Text wenig wertend ist 
- indirekte Rede 
- Genre des Textes
- bspw. Filmrezension: stärkere Gewichtung an Anfang und Ende der Rezension 

## Das Drama als Forschungsprojekt der Kybernetik 

Cube, Felix von; Reichert, Waltraud (1965): Das Drama als Forschungsobjekt der Kybernetik. In: Helmut Kreuzer und Rul Gunzenhäuser (Hg.): Mathematik und Dichtung: Nymphenburger Verlagshandlung, S. 333–346.

- Entropie: mathematisches Maß für Information
	- Quelle mit Repertoire von n Zeichen, die mit Wahrscheinlichkeiten p von i auftreten; Nachricht entsteht durch Selektionsprozess als Anordnung der Quelle als zeitliche und räumliche Folge  
	- Information ist am größten, wenn alle Elemente mit der gleichen Häufigkeit auftreten; Information ist null, wenn nur ein einziges  Element auftritt
	- Häufigkeitsschemata z.B. Alphabet mit ausgezählten Häufigkeiten für die Buchstaben
	- Wahrscheinlichkeitsschemata z.B. stochastische Systeme 
- kybernetischer Begriff der Entropie als Maß für die Ordnung eines Systems
- *Shannon*sche Formel bedeutsam, da sie vom Bereich der Nachrichtenübertragung in den allgemeinen Bereich universaler Strukturen führt 
- Kybernetik als Wissenschaft gemeinsamer Strukturen und Systeme
- elektive Entropie: eine auf dem Prinzip der gegenseitigen Beziehungen von Elementen untereinander basierende ("gegenseitige Elektion") Entropie
	- Wahrscheinlichkeiten bzw. relative Häufigkeiten werden ersetzt durch die normierte Anzahl der auf ein Individuum entfallenden Wahlen 
	- Beispiel Drama: quantifizierte Beziehungen müssen durch Gesamtzahl der vorhandenen Beziehungen normiert werden 
		- Minimum der Funktion nimmt Wert 0 an, da Fall eintreten kann, dass nur *ein* Individuum gewählt wird 
		- bei Untersuchung von Dramen Nutzung der allgemeineren Form der elektiven Entropie ohne vorgegebene Wahlzahl 
		- weiterer Fall, dass innerhalb einer Gruppe keine positiven oder negativen Beziehungen auftreten 
- Drama unter dem Aspekt der ästhetischen Theorie Benses
	- Drama kann in Soziogramme zerlegt werden, wobei Beziehungen von Charakteren quantitativ erfasst werden können 
	- Bense definiert ästhetische Information durch Folgen der Anordnung von Zeichen 
	- ungleichmäßige und ungewöhnliche Verteilungen treten so auf - Ästhetik durch hohen Grad der Redundanz 
- Anwendung von Entropie bei Dramenanalyse 
	- Zeichen wird erst durch seinen Funktionscharakter in einer bestimmten Anordnung zum "Träger ästhetischer Information"
	- handelnde Personen können als Zeichen aufgefasst werden; nicht die einzelnen Personen sind dramatisch, sondern ihre Beziehung untereinander 
	- Untersuchung: Vergleich "normaler" Gruppen mit "dramatischen" Gruppen durch Gruppenentropie (Abweichung von "normalen" elektiven Redundanzwerten als ästhetisches Maß für Dramen)
	- - Begriff und Problematik des Entropiediagramms
	- Bewertung: Ausdruck der Bewertung durch +,0,-; auf Verfeinerung wird verzichtet, da so Interpretationsprobleme auftreten; getrennte Bewertungen bei positiven *und* negativen Zügen 
	- Phaseneinteilung: keine Beachtung der Szenen und Akte, da einerseits über mehrere Szenen unverändert, andererseits innerhalb einer Szene große Veränderung stattfinden kann; Phaseneinteilung beruhend auf kommunikativer Strukturänderungen 
	- beteiligte Personen: auch Personen, die in einer Phase erwähnt werden, nicht aber selbst auftreten, werden einbezogen 
	- Interpretation: Konflikte stellen sich durch hohe negative Werte dar, konfliktträchtige Situationen durch starke Differenzierung; Gleichgewichtszustand entweder durch Gleichgewicht der Sympathien oder Antipathien 
- Entropiediagramm des Dramas Antigone von Sophokles 
	- Aufteilung in fünf Phasen, eingeteilt durch Zeilennummern 
	- Nebenpersonen wurden vernachlässigt, da sie Entropiediagramm nicht (wesentlich) beeinflussen 
		- Nebenperson bedeutet: verändert zwar die äußere Handlung (z.B. ein Bote), beeinflusst aber nicht Beziehungen
	- Beispiel anhand der 1. Phase (Antigone berichtet vom Verbot Kreons, Polyneikes zu begraben, und fasst den Entschluss, gegen dieses Verbot zu handeln; Kreon erfährt, dass gegen sein Verbot gehandelt wurde und verflucht den noch unbekannten Täter 

|  	| A 	| I 	| K 	|  
|---	|-----	|-----	|-----	|
| A 	| - 	| 0/- 	| 0/- 	|  
| I 	| +/0 	| - 	| 0/0 	|  
| K 	| 0/0 	| 0/0 	| - 	| 


- Entropiediagramm  
	- bei einzelnen Phasen wird jeweils für Positiv und Negativ ermittelt, wie oft in einer Spalte (siehe Tabelle oben) eine Beziehung den jeweiligen Wert + bzw. - annimmt, daraus wird Entropie errechnet
	- aus diesen Werten wird Diagramm erstellt, welches für gesamtes Drama positive oder negative Beziehungsmuster (richtiges Wort?) darstellt 
- Ergebnisse: 
	- normierte elektive Entropie erreicht Wert 1 (in realen Gruppen konnte das nicht beobachtet werden 
	- Verlauf der Entropiediagramme unterschiedlicher Dramen sehr verschieden -> Klassifizierung von Dramen durch Entropiediagramme? 
		- hohe Werte im Bereich negativer Beziehungen von Beginn an: bereits bestehende Konflikte werden ausgetragen 
	- gegenseitige personale Beziehungen lassen sich quantifizieren  und darstellen 


## Das Konzept der elektiven Entropie 

Ilsemann, Hartmut: Das Konzept der elektiven Entropie. Hannover. Online verfügbar unter http://www.shak-stat.engsem.uni-hannover.de/mverfahr.html, zuletzt geprüft am 26.06.2019.

- Begriff der elektiven Entropie ausgehend von *Shannon*scher Informationstheorie (Entropie) 
- Information eines endlichen Schemas mit n Zeichen am größten, wenn Wahrscheinlichkeit, dass sie auftreten, gleich ist - tritt nur ein Element auf, ist Informationsgehalt Null (= Zustand maximaler Ordnung)
- gewandelter Begriff der Entropie wird bezogen auf Soziometrie nach Jacob Levy Moreno 
	- durch soziometrische Untersuchungen sollen soziale Gruppen durchleuchtet werden (z.B. Schulklassen); durch positive oder negative Wahlen, z.B. Wunschnachbarn für Sitzordnung
	- so werden Netze Entwickelt, die Sympathie und Antipathie innerhalb einer Gruppe darstellen 
- soziales System (nach Moreno) kann in kofliktreicher oder konfliktarmer Umgebung hohe oder niedrige Entropie besitzen
	- Einzelelemente sind keine Zeichen, sondern Wahlen der Individuen (deshalb *elektive Entropie*)
- Übertragung dieses Modells auf Dramen:
	- Figuren können nicht nach Sympathien und Antipathien befragt werden, weshalb aus Dialogen extrahiert werden muss, ob eine Person eine positive oder negative Einstellung gegenüber einer anderen Person hat
	- zur Vergleichbarkeit der Entropiewerte von Dramen ist der maximale Wert 1 (= normierter elektiver Entropiewert, kurz EEN)
	- Einteilung der Dramen in Phasen


## Sentiment Analyse-Verfahren für die quantitative Untersuchung von Lessings Dramen 

Schmidt, Thomas; Burghardt, Manuel; Dennerlein, Katrin (2018): "Kann man denn auch nicht lachend sehr ernsthaft sein?". Zum Einsatz von Sentiment Analyse-Verfahren für die quantitative Untersuchung von Lessings Dramen. In: Vogeler, Georg (Hg.): Kritik der digitalen Vernunft. Abstracts zur Jahrestagung des Verbandes Digital Humanities im deutschsprachigen Raum, 26.02. - 02.03.2018 an der Universität zu Köln. Köln: Universitäts- und Stadtbibliothek Köln, S. 244–249. 

- Lexikonbasierte Sentimentanalyse (SA): 
	- Wortliste, wobei jedes Wort mit Sentiment-Informationen ausgestattet ist (positive oder negative Konnotation, Polaritätsstärke) 
- SA-Parameter: 
	- unterschiedliche Sentiment-Lexika für die deutsche Sprache wurden untersucht (SentiWS, Berlin Affective Word List - Reloaded, NRC Emotion-Association Lexicon, Clemaride & Klenner, German Polarity Clues)
	- Lexikon-Erweiterungstool wurde untersucht (für historische linguistische Varianten der Originalwörter) 
	- Einfluss von Stoppwortlisten auf die Qualität der SA; dabei auch Untersuchung von Listen mit hochfrequenten Wörtern aus dem Korpus, welche zwar als sentiment-tragend ausgezeichnet werden, aufgrund ihrer hohen Nutzung allerdings ein Ungleichgewicht erzeugen (z.B. Fräulein) 
	- Evaluation eines Lemmatisierungstools, da einige SA-Lexika Wörter nur als Grundform enthalten haben 
- Metriken wurden auff unterschiedlichen Ebenen kalkuliert: Drama, Akt, Szene, Replik und Sprecherbeziehungen pro Drama, Akt, Szene, Replik 
- Gold Standard: 
	- Evaluationskorpus aus 200 Repliken, welche von fünf Personen bewertet wurden
		- sechswertig: sehr negativ, negativ, neutral, gemischt, positiv, sehr positiv (40prozentige Übereinstimmung) 
		- binär: positiv, negativ (77prozentige Übereinstimmung) 
- Evaluationsmaße: Accuracy, Recall, Precision, F-Werte
- Ergebnisse: 
	- Tool zur Erweiterung der Lexika verbessert Leistung 
	- Stoppwortlisten keinen merklich positiven Einfluss auf SentiWS
	- SentiWS lemmatisiert mittels Pattern-Lemmatisierer große Verbesserung 


## Character-to-Character Sentiment Analysis in Shakespeare's Plays 

Nalisnick, Eric T.; Baird, Henry S.: Character-to-character sentiment analysis in Shakespeare's plays. In: Hinrich Schuetze, Pascale Fung und Massimo Poesio (Hg.): Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics. Sofia, Bulgaria. ACL: Association for Computational Linguistics.

- Können Maschinen bzw. Computer Emotionen aus einem literarischen Werk extrahieren? 
- Emotionen werden oftmals subtil und nur indirekt transportiert
- Nutzung von Sentiment-Lexika und Dialog-Struktur, um Beziehungsdynamiken nachzuvollziehen 
- Bezug auf Methoden zur Zuordnung von Sprechakten in unstrukturierten Texten und der Extraktion von sozialen Netzen 
- Beziehungen einzelner Charaktere zueinander sollen analysiert werden, anstatt die Sentimente eines ganzen Texts bzw. die eines einzelnen Charakters 
- Extraktion der Beziehungen 
	- Wertigkeit der Beziehungen wird extrahiert, indem jeder Fall kontinuierlichen Sprechens mit einem Wert versehen wird (aus dem Sentiment-Lexikon) und davon ausgegangen wird, dass das Sentiment dieses Sprechaktes an den vorangegangenen Sprecher gerichtet ist 
	- die Annahme, dass Gesprochendes sich immer auf den Charakter bezieht, der vorher gesprochen hat, ist nicht immer wahr
	- oft bezieht sich Gesprochenes auch auf jemanden "Offstage"
- Beispiel Hamlet und Gertrude 
	- Sentimententwicklung siehe Abbildung 2: schwarze Linie beschreibt Hamlets Sentimente gegenüber Gertrude, während die grau Fläche Gertrudes Beziehung gegenüber Hamlet darstellt 
	- hoher Sentimentwert gegenüber seiner Mutter, obwohl er am Anfang davon ausgeht, dass Gertrude etwas mit dem Tod von König Hamlet zutun hatte 
	- schlagartige Veränderung der Sentimente: 
		- zum einen, als Hamlet seine Mutter mit seinen Anschuldigungen konfrontiert und sie diese klar von sich weist, der Geist von König Hamlet unterstützt die Mutter (Sentiment von -1 zu 22)
		- zum anderen, als Gertrude erlebt, wie Hamlet Polonius, einen Unschuldigen umbringt, und mit einem Geist redet (König Hamlet), den sie nicht sehen kann (Sentiment von 1 zu -19)
- Beispiel Romeo und Julia 
	- starke positive Sentimente, beruhend auf Gegenseitigkeit 
- künftige Forschung sollte tiefer in den Kontext von Dialogen eintauchen und nicht von der naiven Annahmen ausgehen, dass Gesprochenes immer auf den vorherigen Sprecher bezogen ist 
