import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys

from datetime import datetime
from anki_review_graphs.AnkiConnect import AnkiConnect
from anki_review_graphs.metrics import TimeAndScoreMetric, MetricBase, CumulativeTimeAndScoreMetric

if len(sys.argv) < 2:
    print('Usage: anki-review-graphs.py <deckName1> <deckName2> ...' )
    sys.exit(1)
deck_count = len(sys.argv) - 1

ankiConnect = AnkiConnect()

def plot_stats(deckName, row, col):
    reviewStats = ankiConnect.getDeckReviewStats(deckName)
    metric = CumulativeTimeAndScoreMetric.CumulativeTimeAndScoreMetric(reviewStats)
    scores = metric.getScores()
    print(f"Deck: {deckName} Scores: {scores}")

    keys = sorted(list(scores.keys()))
    values = [scores[key] for key in keys]
    dates = [datetime.strptime(key, '%Y-%m-%d') for key in keys]

    plot = plt.subplot2grid((3, 3), (row, col), colspan=2, rowspan=2)
    plot.plot_date(dates, values, xdate=True, linestyle='-')
    plot.set_title(deckName)


col = 0
row = 0
for deckName in sys.argv[1:]:
    plot_stats(deckName, row, col)
    if col == 2:
        col = 0
        row += 2    
    else:
        col += 2

plt.show()