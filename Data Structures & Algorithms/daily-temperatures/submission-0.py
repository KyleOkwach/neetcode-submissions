class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # pair: [temp, index]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # while stack isn't empty and top item in stack is smaller than current
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)  # currentIndex - topItemIndex
            stack.append([t, i])
        return res