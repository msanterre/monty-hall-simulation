# Monty Hall Probability Simulation 🎲

A Python simulation that demonstrates the famous **Monty Hall Problem** using a 3-number guessing game format.

## What This Simulation Does

This program runs a large-scale probability experiment (10 million trials by default) that simulates a variant of the classic Monty Hall problem:

1. **Initial Setup**: A winning number (1-3) and an initial guess (1-3) are chosen randomly
2. **Information Reveal**: One wrong number is eliminated from the available choices  
3. **Final Decision**: A new guess is made from the remaining 2 numbers
4. **Analysis**: Win rates are compared between initial guesses vs final guesses

## The Monty Hall Problem 🚪

Originally posed by statistician Steve Selvin in 1975, the Monty Hall problem asks:

> You're on a game show with 3 doors. Behind one door is a car, behind the others are goats. You pick a door. The host, who knows what's behind each door, opens one of the remaining doors to reveal a goat. Should you stick with your original choice or switch to the other unopened door?

**Counter-intuitive Answer**: You should always switch! Your odds improve from 1/3 to 2/3.

## How to Run

```bash
python main.py
```

## Expected Results 📊

### Mathematical Theory:
- **Initial guess accuracy**: ~33.33% (1 out of 3 chance)
- **Final guess accuracy**: ~50.00% (1 out of 2 chance after elimination)
- **Expected improvement**: ~16.67 percentage points

### Why This Happens:
1. **Initial Phase**: With 3 options, you have a 1/3 probability of being correct
2. **Elimination Phase**: Removing one wrong answer doesn't change your original probability  
3. **Final Phase**: But now you're choosing from only 2 options, so random selection gives 50% odds
4. **Net Effect**: Your win rate improves from 33% to 50%

## Sample Output

```
Running Monty Hall-style simulation for 10,000,000 steps...

Results after 10,000,000 steps:
============================================================

Winning Number Distribution:
------------------------------
Number 1: 3,332,890 times (33.33%)
Number 2: 3,333,567 times (33.34%) 
Number 3: 3,333,543 times (33.34%)

Initial Guess Distribution:
------------------------------
Number 1: 3,332,234 times (33.32%)
Number 2: 3,334,123 times (33.34%)
Number 3: 3,333,643 times (33.34%)

Final Guess Distribution:
------------------------------
Number 1: 3,333,456 times (33.33%)
Number 2: 3,333,234 times (33.33%)
Number 3: 3,333,310 times (33.33%)

Win Statistics:
------------------------------
Initial guess wins: 3,333,892 (33.34%)
Final guess wins: 4,999,847 (50.00%)
Improvement: 16.66 percentage points

Strategy Analysis:
------------------------------
Stayed with original: 4,999,234 (50.00%)
Switched guess: 5,000,766 (50.00%)

Expected initial win rate: ~33.33% (1/3)
Expected final win rate: ~50.00% (1/2 after removal)
============================================================
```

## Key Insights 🧠

### 1. **Information Has Value**
By eliminating one wrong option, we gain valuable information that improves our decision-making, even with random final choices.

### 2. **Probability Shifts**  
The elimination phase transforms a 1-in-3 game into a 1-in-2 game, fundamentally changing the odds.

### 3. **Large Numbers Converge**
With millions of trials, the results converge very close to the theoretical predictions, demonstrating the law of large numbers.

### 4. **Stay vs Switch Balance**
In this random implementation, players stay with their original guess about 50% of the time and switch 50% of the time.

## Variations Explored 🔄

This codebase has explored several interesting variations:

- **Always Stay Strategy**: Keeps original guess (win rate: ~33%)  
- **Always Switch Strategy**: Always changes guess (win rate: ~67%)
- **Coin Flip Strategy**: Random decision (win rate: ~50%)
- **Divine Divination**: Mystical decision-making with multiple omens
- **Lucky Rabbit's Foot**: Enhanced luck charm affecting decisions

## Mathematical Foundation 📐

The improvement from 33% to 50% represents the mathematical difference between:
- **Uninformed random choice**: 1/3 probability  
- **Informed random choice**: 1/2 probability after elimination

This demonstrates how **information theory** and **conditional probability** work in practice.

## Dependencies

- Python 3.x
- No external libraries required (uses only built-in `random` module)

## License

This simulation is provided for educational purposes to demonstrate probability theory and the Monty Hall problem.

---

*"The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."* - Albert Einstein 