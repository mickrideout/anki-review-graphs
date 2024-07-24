# Combined metric for time and score.
# For a positive score normalised duration change must show improvement and the chosen button be 3 or 4. Otherwise score is negative.
from .MetricBase import MetricBase

class TimeAndScoreMetric(MetricBase):

    def __init__(self, reviewStats):
        super().__init__(reviewStats)

    def getScores(self):
        allReviews = self._getAllReviewTuples()
        scores = {}
        for review in allReviews:
            # (reviewTime, cardID, usn, buttonPressed, newInterval, previousInterval, newFactor, reviewDuration, reviewType)
            reviewDate = self._getDateString(review[1][0])
            # calculate normalised duration change \( \Delta T_{norm} = \frac{\Delta T}{T_{last}} = \frac{T_{current} - T_{last}}{T_{last}} \).
            durationChange = (review[1][7] / 1000) - (review[0][7] / 1000) / review[0][7] * -1
            score = 0
            if (review[1][3] == 3 or review[1][3] == 4) and (durationChange > 0):
                # positive score
                score = 1
            else:
                # negative score
                score = -1 
            if reviewDate in scores:
                scores[reviewDate].append(score)
            else:
                scores[reviewDate] = [score]
        for date in scores:
            scores[date] = sum(scores[date]) / len(scores[date])
        return scores
                