import random
import sys
import time

def fillList(limit):
    array = []
    for i in range(limit):
        array.append(i)
    random.shuffle(array)
    return array
    

def round(limit):
    match = False
    rounds = 0
    user1 = fillList(limit)
    user2 = fillList(limit)
    user1full = []
    user2full = []
    
    
    while match == False and limit > rounds:
        user1full.append(user1[rounds])
        user2full.append(user2[rounds])
                 
        if user1[rounds] in user2full or user2[rounds] in user1full: 
            match = True
            #print(f"found a match in {rounds+1} rounds.")
        rounds = rounds + 1
        
    return rounds
    
def simulate(simulations, limit):
    sum = 0
    for i in range(simulations):
        sum = sum + round(limit);    
    avg = sum/simulations
    print(f"With a total number of {limit} items in the list")
    print(f"""The average number of rounds to get a match 
in {simulations} simulations was: {avg}""")
                    

if __name__ == "__main__":
    start_time = time.perf_counter()
    if len(sys.argv) < 3:
        print("Invalid input, please write value of simulations and items")
        exit()
    simulations = (int)(sys.argv[1])    
    limit = (int)(sys.argv[2])
    simulate(simulations, limit)
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"And it took: {duration:.6f} seconds.")
     