class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        #create a queue which can be accessed from front and back
        q=deque(sorted(tokens))
        # intialize score and max_score 
        score=0
        max_score=0
        #while the q is not empty
        while q:
            # 2 options to play token
            if power>=q[0]:
                points=q.popleft()
                power-=points
                score+=1
                max_score=max(score,max_score)
            elif score>0:
                points=q.pop()
                power+=points
                score-=1
            #if the 2 tokens doesnt have bandwidth
            else:
                break
        return max_score
        