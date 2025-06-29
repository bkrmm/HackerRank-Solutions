import random
import sys

def parse_input():
    """Parse the input format for the Snakes and Ladders problem."""
    T = int(input().strip())
    test_cases = []
    
    for _ in range(T):
        # Parse die probabilities
        prob_line = input().strip()
        probabilities = [float(x) for x in prob_line.split(',')]
        
        # Parse number of ladders and snakes
        counts_line = input().strip()
        num_ladders, num_snakes = map(int, counts_line.split(','))
        
        # Parse ladders
        ladders = {}
        if num_ladders > 0:
            ladders_line = input().strip()
            ladder_pairs = ladders_line.split(' ')
            for pair in ladder_pairs:
                start, end = map(int, pair.split(','))
                ladders[start] = end
        else:
            input()  # Read empty line
            
        # Parse snakes
        snakes = {}
        if num_snakes > 0:
            snakes_line = input().strip()
            snake_pairs = snakes_line.split(' ')
            for pair in snake_pairs:
                head, tail = map(int, pair.split(','))
                snakes[head] = tail
        else:
            input()  # Read empty line
            
        test_cases.append((probabilities, ladders, snakes))
    
    return test_cases

def simulate_game(probabilities, ladders, snakes, max_rolls=1000):
    """Simulate a single game of Snakes and Ladders."""
    position = 1
    rolls = 0
    
    # Create cumulative probabilities for die roll simulation
    cumulative_probs = []
    cumsum = 0
    for prob in probabilities:
        cumsum += prob
        cumulative_probs.append(cumsum)
    
    while position < 100 and rolls < max_rolls:
        rolls += 1
        
        # Roll the biased die
        rand_val = random.random()
        die_value = 6  # Default to 6 if no probability matches
        for i, cum_prob in enumerate(cumulative_probs):
            if rand_val <= cum_prob:
                die_value = i + 1
                break
        
        # Calculate new position
        new_position = position + die_value
        
        # Check if roll would exceed 100 - important rule!
        if new_position > 100:
            continue  # Roll is wasted, stay at current position
            
        position = new_position
        
        # Check for ladders first
        if position in ladders:
            position = ladders[position]
        # Check for snakes
        elif position in snakes:
            position = snakes[position]
            
        # Check if we've reached exactly 100
        if position >= 100:
            break
    
    # Return number of rolls if game completed, otherwise None
    return rolls if position >= 100 else None

def solve_test_case(probabilities, ladders, snakes, num_simulations=5000):
    """Solve a single test case by running multiple simulations."""
    total_rolls = 0
    successful_games = 0
    
    for _ in range(num_simulations):
        rolls = simulate_game(probabilities, ladders, snakes)
        if rolls is not None:  # Game completed within 1000 rolls
            total_rolls += rolls
            successful_games += 1
    
    if successful_games == 0:
        return 0  # No games completed
    
    average_rolls = total_rolls / successful_games
    return round(average_rolls)

def main():
    """Main function to solve all test cases."""
    test_cases = parse_input()
    
    for probabilities, ladders, snakes in test_cases:
        result = solve_test_case(probabilities, ladders, snakes)
        print(result)

if __name__ == "__main__":
    main()
