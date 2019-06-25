# Rechercheergebnisse

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
	- Untersuchung:Vergleich "normaler" Gruppen mit "dramatischen" Gruppen durch Gruppenentropie (Abweichung von "normalen" elektiven Redundanzwerten als ästhetisches Maß für Dramen)