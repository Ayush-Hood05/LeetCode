class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        step_left = 0
        step_right = 0
        blank = 0
        for i in range (0, len(moves)):
            if moves[i] == 'L':
               step_left +=1
            elif moves[i] == 'R':
                step_right +=1
            else :
                blank +=1
        return abs(step_left - step_right) + blank 

        