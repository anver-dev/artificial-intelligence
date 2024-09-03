import time

from result import Result
from hillClimbing import HillClimbingOptimizer
from file import write_results_to_file, print_log

_UPPER_LIMIT = 501
_LOWER_LIMIT = -500


results = []
hill_climbing = HillClimbingOptimizer(_UPPER_LIMIT, _LOWER_LIMIT)

for iteration in range(1, 31):
    epsilon = 5
    
    cycles = 9999999
    stagnation_threshold = 9999999
    
    start_time = time.time()
    calculated_cost = hill_climbing._init(epsilon, cycles, stagnation_threshold)
    end_time = time.time()
    
    duration = end_time - start_time

    result = Result(iteration, calculated_cost, duration)

    print(f"Iteration {iteration} time elapsed: {result._get_human_readable_time()}")
    results.append(result)

print_log(results)
write_results_to_file(results)