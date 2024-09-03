from typing import List

from result import Result

FILE_NAME = 'results_5.csv'
ITERATION_HEADER = "#"
BEST_COST_HEADER = "BEST COST"
TIME_HEADER = "TIME"

def write_results_to_file(content: List[Result]) -> None:
    try:
        with open(FILE_NAME, 'w') as file:
            for result in content:
                file.write(f"{result._get_iteration_number()},{result._get_best_cost()},{result.get_time()}\n")
        
        print(f"-"*50)
        print(f"File '{FILE_NAME}' saved successfully.")
        print(f"-"*50)
    except Exception as e:
        print(f"Error saving file '{FILE_NAME}': {str(e)}")

def print_log(results):
    print(f"-"*50)
    print(f"{'RESULTS |':^50}")
    result: Result

    max_width_iteration = max(len(str(result._get_iteration_number())) for result in results)
    max_width_best_cost = max(len(f"{result._get_best_cost()}".rstrip('0').rstrip('.')) for result in results)
    max_width_time = max(len(str(result._get_human_readable_time())) for result in results)

    print(f"| {str(ITERATION_HEADER):<{max_width_iteration}} "
        f"| {str(BEST_COST_HEADER):<{max_width_best_cost}} " 
        f"| {str(TIME_HEADER):<{max_width_time}} |")

    for result in results:
        print(f"| {str(result._get_iteration_number()):<{max_width_iteration}} "
            f"| {result._get_best_cost():<{max_width_best_cost}} "
            f"| {str(result._get_human_readable_time()):<{max_width_time}} |")
    
    print(f"\n")