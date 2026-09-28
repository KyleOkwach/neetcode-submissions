class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        counter, prev = 0, 0

        for p, s in sorted(pair)[::-1]:
            time = (target - p) / s
            if prev < time:
                counter += 1
                prev = time
        
        return counter
