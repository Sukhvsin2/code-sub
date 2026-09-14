class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        # pairs = []
        # # create pairs
        # for i in range(len(position)):
        #     pairs.append((position[i], speed[i]))
        
        pairs = zip(position, speed)

        # sorted pairs
        pairs = sorted(pairs)[::-1]

        for p, s in pairs:
            # cal time = (distance - covered dis ) / speed
            stack.append((target-p)/s)
            # need at least 2 car's time to calculate the fleet. 
            # if recent added car's time is less or equal it means they will match speed.
            # which means this the current car either surpass or match the speed.
            # so count in single fleet so pop the recent added car's time.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()


        return len(stack)