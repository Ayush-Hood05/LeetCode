class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        # Earilest time find karenge 
        # land then water senario 

        land_finish = float('inf')
        water_finish = float('inf')

        land_water = float('inf')
        water_land = float('inf')

        # first land then water
        for i in range (0,len(landStartTime)):
            land_finish = min(land_finish , landStartTime[i] + landDuration[i])

        for i in range (0,len(waterStartTime)):
            water_finish = min(water_finish , waterStartTime[i] + waterDuration[i])
            land_water = min(land_water , max(waterStartTime[i],land_finish) + waterDuration[i])

        # first water than land
        for i in range (0,len(landStartTime)):
            water_land = min(water_land,max(landStartTime[i],water_finish) + landDuration[i])    

        return min(land_water,water_land)