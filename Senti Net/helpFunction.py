

class HelpFunction():

    colors = {
        'c': '\033[36m',
        'y': '\033[33m',
        'b': '\033[34m',
    }

    def colorize(self, string, color):

        if color not in self.colors:
            return string
        return self.colors[color] + string + '\033[37m'

    def hilfe(self):
        u"""Funktion zur Beschreibung des Programms."""
        print(self.colorize("Willkommen im Help-Center! \nHier erklären wir dir, wie \
    man unser Tool benutzt. \nMit dem SentiNet kannst du dir \
    für beliebige deutsche Dramen (soweit auf DraCor.org \
    verfügbar) ein Netzwerk der Figurenbeziehungen darstellen \
    lassen. Du kannst dir sowohl das Netzwerk für das gesamte \
    Drama als auch die Netzwerke für einzelne Akte anzeigen \
    lassen. \
    Die Kanten im Netzwerk stellen die Beziehungen zwischen \
    den Charakteren dar. Die Label der Kanten zeigen die \
    Sentiment-Werte an, die die Figuren zueinander haben.\n\n \
    Benutzung: \n 1. Wähle im Hauptmenü Drama analysieren \n \
    2. Gib den Namen des gewählten Dramas ein. \n \
    3. Gib den Nachnamen des Autors deines gewählten Dramas ein\n \
    4. Dir wird die Anzahl der Akte, die das Drama hat, \
    angezeigt. \n 5. Gib ein, welchen Akt du untersuchen \
    willst oder wähle 0 für das gesamte Drama.\
    \n 6. FERTIG -- dir wird das ausgewählte Netzwerk angezeigt. \
                        \n\n", 'b'))
        input(self.colorize("Um zum Hauptmenü zurückzukehren, drück Enter!", 'c'))
