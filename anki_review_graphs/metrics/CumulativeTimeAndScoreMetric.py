from .TimeAndScoreMetric import TimeAndScoreMetric

class CumulativeTimeAndScoreMetric(TimeAndScoreMetric):

    def __init__(self, reviewStats):
        super().__init__(reviewStats)

    def getScores(self):
        scores = super().getScores()
        keys = sorted(list(scores.keys()))
        cumlative_score = 0
        for date in keys:
            cumlative_score += scores[date]
            scores[date] = cumlative_score
        return scores