from math import sin
from math import sqrt
import random

class HillClimbingOptimizer:
    def __init__(self, upper_limit, lower_limit):
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit

    def _init(self, epsilon, cycles_limit, stagnation_threshold): 
        current_cost = 0
        stagnation_counter = 0
        cycle_count = 0

        current_solution = self._generate_current_solution()
        current_cost = self._cost_of(current_solution)

        while stagnation_counter < stagnation_threshold and cycle_count < cycles_limit:
            cycle_count += 1
            
            adjacent_solution = self._adjacent_of_with_epsilon(current_solution, epsilon)
            adjacent_cost = self._cost_of(adjacent_solution)
            
            if adjacent_cost > current_cost:
                stagnation_counter += 1
                continue
            
            current_cost = adjacent_cost
            current_solution = adjacent_solution
            
            if adjacent_cost < current_cost:
                stagnation_counter = 0
            else:
                stagnation_counter += 1


        return current_cost

    def _cost_of(self, solution):
        a = solution[0]
        b = solution[1]
    
        return self._schwefel_function(a, b)

    def _schwefel_function(self, a, b):
        return (float) (418.9829 * 2 - a * sin(sqrt(abs(a))) - b * sin(sqrt(abs(b))))

    def _generate_current_solution(self):
        solution = [0, 0]

        for i in range(len(solution)):
            solution[i] = random.random() * (self.lower_limit - self.lower_limit) + self.lower_limit

        return solution

    def _adjacent_of_with_epsilon(self, current_solution, epsilon):
        solution = [0, 0]

        for i in range(len(solution)):
            solution[i] = current_solution[i] + epsilon * random.random() * (-2) + 1
            
        solution = self._handle_adjacent_solution(solution)

        return solution
    
    def _handle_adjacent_solution(self, adjacent_solution):
        if (adjacent_solution[0] < self.lower_limit):
            adjacent_solution[0] = self.lower_limit - (adjacent_solution[0] - (self.lower_limit))
        
        if (adjacent_solution[1] > self.upper_limit):
            adjacent_solution[1] = self.upper_limit - (adjacent_solution[1] - (self.upper_limit));
        
        return adjacent_solution