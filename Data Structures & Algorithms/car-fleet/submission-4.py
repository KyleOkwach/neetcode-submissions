class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets, prev = 0, 0

        for p, s in cars:
            time = (target - p) / s
            if prev < time:
                fleets += 1
                prev = time
        
        return fleets