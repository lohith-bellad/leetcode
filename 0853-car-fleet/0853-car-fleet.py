class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = sorted(zip(position, speed), reverse=True)
        car_stack = []

        for (p, s) in fleet:
            time_to_reach = (target - p) / s

            car_stack.append(time_to_reach)

            if len(car_stack) > 1 and car_stack[-1] <= car_stack[-2]:
                car_stack.pop()
    
        return len(car_stack)

        
       