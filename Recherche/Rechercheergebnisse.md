# Rechercheergebnisse

## SentiWS - SentimentWortschatz der Universität Leipzig 

R. Remus, U. Quasthoff & G. Heyer: SentiWS - a Publicly Available German-language Resource for Sentiment Analysis.
In: Proceedings of the 7th International Language Ressources and Evaluation (LREC'10), pp. 1168-1171, 2010

- beinhaltet Wörter mit positivem oder negativem Sentiment in Intervall von [-1;1] und PoS-Tag 
- Adjektive und Adverben, die explizit Sentiment enthalten; Nomen und Verben, die implizit Sentiment enthalten 
- kurz für SentimentWortschatz
- ein Wort kann verschiedene Einträge, bspw. nach PoS, haben
- wichtig zu beachten, dass Wertigkeit von Worten je nach Kontext unterschiedlich ist 
- Quellen: 
	- General Inquirer (GI) lexicon - ins Deutsche übersetzt mithilfe von Google Übersetzer und danach manuell aussortiert 
	- Kookkurrenzanalyse von Kundenrezensionen, die von den Autoren selbst als sehr positiv oder sehr negativ getagged wurden 
		 - aus je 5100 positiven und negativen Reviews wurde mithilfe von Kookkurrenzanalyse getaggte Wörter mit noch nicht getaggten Wörtern ausgewählt und per Hand selektiert (sinnvoll für "domain-dependent terminology", z.B. Kundenrezensionen - Reklamation, Fehlkauf, etc.)

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
