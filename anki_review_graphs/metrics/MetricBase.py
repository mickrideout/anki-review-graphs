# Base class for metrics.
from abc import ABC, abstractmethod
from datetime import datetime

class MetricBase(ABC):

    # Review stats is list of 9-tuples:
    # (reviewTime, cardID, usn, buttonPressed, newInterval, previousInterval, newFactor, reviewDuration, reviewType)
    # [
    #     [1594194095746, 1485369733217, -1, 3,   4, -60, 2500, 6157, 0],
    #     [1594201393292, 1485369902086, -1, 1, -60, -60,    0, 4846, 0]
    # ],
    def __init__(self, reviewStats):
        self.reviewStats = reviewStats
        self.cardDict = self._getCardDict(reviewStats)

    # return a dict of cardID -> review tuple
    def _getCardDict(self, reviewStats):
        cardDict = {}
        for review in reviewStats:
            cardId = review[1]
            if cardId in cardDict:
                cardDict[cardId].append(review)
            else:
                cardDict[cardId] = [review]
        for cardId in cardDict:
            cardDict[cardId] = sorted(cardDict[cardId], key=lambda x: x[0])
        return cardDict
    
    def _getAllReviewTuples(self):
        allTuples = []
        for cardId in self.cardDict:
            reviewCount = len(self.cardDict[cardId])
            if reviewCount > 1:
                # start from second review
                for i in range(1, reviewCount):
                    allTuples.append([self.cardDict[cardId][i-1], self.cardDict[cardId][i]])
        return allTuples
    
    # get date string from epoch
    def _getDateString(self, timestamp):
        return datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')

    

    # return list of tuples of (date, score)
    @abstractmethod
    def getScores(self):
        pass

