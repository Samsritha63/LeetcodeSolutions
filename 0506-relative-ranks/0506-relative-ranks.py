class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score=sorted(score,reverse=True)
        ranks=["0"]*len(score)
        for i in range(len(sorted_score)):
            if i == 0:
                indexx=score.index(sorted_score[i])
                ranks[indexx]="Gold Medal"
            elif i==1:
                indexx=score.index(sorted_score[i])
                ranks[indexx]="Silver Medal"
            elif i==2:
                indexx=score.index(sorted_score[i])
                ranks[indexx]="Bronze Medal"
            else:
                indexx=score.index(sorted_score[i])
                ranks[indexx]=str(i+1)
        return ranks
        