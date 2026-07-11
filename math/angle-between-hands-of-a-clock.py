class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
       # hour hand calulation 
       # for 1hr hour hand moves 30D 
       # Minutes hand angle : 6D per min
       min_hand = 6 * minutes 
       hour_hand = 30*(hour%12) + 0.5*minutes
       diff= abs(hour_hand-min_hand)
       return min(diff,360-diff)