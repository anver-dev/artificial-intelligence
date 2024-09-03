class Result:
    def __init__(self, iterationNumber, bestCost, time):
        self.iterationNumber = iterationNumber
        self.bestCost = bestCost
        self.time = time
        
    def _get_iteration_number(self):
        return self.iterationNumber
    
    def setIterationNumber(self, iterationNumber):
        self.iterationNumber = iterationNumber
    
    def _get_best_cost(self):
        return self.bestCost
    
    def setBestCost(self, bestCost):
        self.bestCost = bestCost
    
    def get_time(self):
        return self.time
    
    def setTime(self, time):
        self.time = time
        
    def _get_human_readable_time(self) -> str:
        minutes = int(self.time / 60)
        seconds = int(self.time % 60)
        milliseconds = int((self.time * 1000) % 1000)
        nanoseconds = int((self.time * 1000000) % 1000)
    
        return f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}:{nanoseconds:03d}"