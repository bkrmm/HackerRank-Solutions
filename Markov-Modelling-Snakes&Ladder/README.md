# Markov Snakes and Ladders - HackerRank Solution

A Python simulation solution for the **Markov Snakes and Ladders** challenge from HackerRank, using Monte Carlo simulation to compute the expected number of die rolls required to reach square 100.

## 🎯 Problem Description

This challenge involves simulating the classic Snakes and Ladders board game with the following modifications:
- **Biased Die**: The die has custom probabilities for each face (1-6)
- **Markov Process**: Each state transition depends only on the current position
- **Exact Landing**: Must land exactly on square 100 to win
- **Roll Waste**: Rolls that would exceed square 100 are wasted

### Rules
1. Start at square 1, goal is to reach square 100
2. Roll a biased 6-sided die according to given probabilities
3. Move forward by the die value
4. If landing on a ladder bottom, climb to the top automatically
5. If landing on a snake head, slide to the tail automatically
6. Rolls that would go past square 100 are ignored (stay at current position)
7. Game must complete within 1000 rolls (otherwise ignored)

## 📁 Files

- `markov_snakes_ladders.py` - Main solution file
- `debug_markov.py` - Debug version with detailed simulation output
- `analyze_markov.py` - Analysis version with statistics and insights
- `sample_input.txt` - Sample test cases for testing
- `README.md` - This documentation file

## 🔧 Solution Approach

### Monte Carlo Simulation
The solution uses Monte Carlo simulation to estimate the expected number of rolls:

1. **Input Parsing**: Parse die probabilities, ladders, and snakes from input
2. **Game Simulation**: Simulate individual games using biased die rolls
3. **Statistical Analysis**: Run 5000 simulations per test case
4. **Result Calculation**: Compute average rolls and round to nearest integer

### Key Implementation Details

```python
def simulate_game(probabilities, ladders, snakes, max_rolls=1000):
    position = 1
    rolls = 0
    
    # Create cumulative probabilities for die simulation
    cumulative_probs = []
    cumsum = 0
    for prob in probabilities:
        cumsum += prob
        cumulative_probs.append(cumsum)
    
    while position < 100 and rolls < max_rolls:
        rolls += 1
        
        # Simulate biased die roll
        rand_val = random.random()
        die_value = 6  # Default
        for i, cum_prob in enumerate(cumulative_probs):
            if rand_val <= cum_prob:
                die_value = i + 1
                break
        
        # Apply game rules...
```

## 📥 Input Format

```
T                           # Number of test cases
p1,p2,p3,p4,p5,p6          # Die probabilities (sum = 1.0)
num_ladders,num_snakes      # Count of ladders and snakes
start1,end1 start2,end2...  # Ladder positions (bottom,top)
head1,tail1 head2,tail2...  # Snake positions (head,tail)
```

## 📤 Output Format

```
expected_rolls_1            # Expected rolls for test case 1
expected_rolls_2            # Expected rolls for test case 2
...
```

## 🚀 Usage

### Run the main solution:
```bash
python markov_snakes_ladders.py < sample_input.txt
```

### Run debug version for detailed output:
```bash
python debug_markov.py < sample_input.txt
```

### Run analysis version for statistics:
```bash
python analyze_markov.py < sample_input.txt
```

## 📊 Example

### Sample Input:
```
3
0.17,0.16,0.17,0.16,0.17,0.17
4,4
3,54 12,50 17,67 42,99
62,18 88,24 95,56 97,78
0.17,0.16,0.17,0.16,0.17,0.17
0,0


0.17,0.16,0.17,0.16,0.17,0.17
4,4
3,54 12,50 17,67 42,99
62,18 88,24 95,56 97,78
```

### Sample Output:
```
42
33
42
```

## 🧠 Algorithm Complexity

- **Time Complexity**: O(T × N × R) where T = test cases, N = simulations per test (5000), R = average rolls per game
- **Space Complexity**: O(L + S) where L = number of ladders, S = number of snakes

## 🔍 Key Features

- **Accurate Simulation**: Implements all game rules precisely
- **Biased Die Handling**: Properly simulates non-uniform die probabilities
- **Statistical Robustness**: Uses 5000 simulations for stable results
- **Error Handling**: Ignores games that don't complete within 1000 rolls
- **Debugging Support**: Multiple versions for development and testing

## 📈 Performance Considerations

- **Random Seed**: Not set for true randomness in competition
- **Simulation Count**: 5000 provides good balance of accuracy vs. speed
- **Memory Efficient**: Minimal memory usage with streaming approach
- **Timeout Handling**: 1000 roll limit prevents infinite games

## 🎲 Mathematical Background

This problem is a Markov Chain where:
- **States**: Board positions (1-100)
- **Transitions**: Determined by die probabilities and board features
- **Absorbing State**: Position 100 (game end)
- **Expected Value**: Average time to absorption

## 🐛 Known Limitations

- Results may vary from expected due to random simulation nature
- Complex board configurations might require more simulations
- Floating point precision could affect very close probability values

## 🔗 Problem Link

[HackerRank - Markov Snakes and Ladders](https://www.hackerrank.com/challenges/markov-snakes-and-ladders/problem)

## 📝 Notes

- The solution allows ±10% deviation as per HackerRank scoring rules
- Results are rounded to the nearest integer
- All edge cases (empty ladders/snakes, boundary conditions) are handled

---

**Author**: Your Name  
**Language**: Python 3  
**Category**: Mathematics, Probability, Simulation  
**Difficulty**: Medium-Hard
