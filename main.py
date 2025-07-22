import random

def run_simulation(steps=10000000):
    """Run simulation implementing Monty Hall-style game with second guess after removing a wrong number."""
    winning_counts = {1: 0, 2: 0, 3: 0}
    initial_guess_counts = {1: 0, 2: 0, 3: 0}
    final_guess_counts = {1: 0, 2: 0, 3: 0}
    
    initial_wins = 0
    final_wins = 0
    stayed_with_original = 0
    switched_guess = 0
    
    print(f"Running Monty Hall-style simulation for {steps:,} steps...")
    
    # Run the simulation
    for _ in range(steps):
        # Step 1: Choose winning number and initial guess
        winning_number = random.randint(1, 3)
        initial_guess = random.randint(1, 3)
        
        winning_counts[winning_number] += 1
        initial_guess_counts[initial_guess] += 1
        
        # Check initial guess
        if initial_guess == winning_number:
            initial_wins += 1
        
        # Step 2: Remove one wrong number (not winning number, not initial guess)
        available_numbers = {1, 2, 3}
        
        # Find numbers to potentially remove (wrong numbers that aren't the initial guess)
        wrong_numbers = available_numbers - {winning_number}
        removable_numbers = wrong_numbers - {initial_guess}
        
        # If initial guess was wrong, we can remove it too, but we'll prioritize others
        if initial_guess != winning_number and len(removable_numbers) == 0:
            # This happens when initial guess is wrong and there's only one other wrong number
            removable_numbers = {initial_guess}
        
        # Remove one wrong number
        if removable_numbers:
            removed_number = random.choice(list(removable_numbers))
            available_numbers.remove(removed_number)
        else:
            # Edge case: remove any wrong number
            wrong_numbers_list = list(wrong_numbers)
            if wrong_numbers_list:
                removed_number = random.choice(wrong_numbers_list)
                available_numbers.remove(removed_number)
        
        # Step 3: Make final guess from remaining numbers
        available_list = list(available_numbers)
        final_guess = random.choice(available_list)
        final_guess_counts[final_guess] += 1
        
        # Track if player stayed or switched
        if final_guess == initial_guess:
            stayed_with_original += 1
        else:
            switched_guess += 1
        
        # Check final guess
        if final_guess == winning_number:
            final_wins += 1
    
    # Calculate and display results
    print(f"\nResults after {steps:,} steps:")
    print("=" * 60)
    
    print("\nWinning Number Distribution:")
    print("-" * 30)
    for number in [1, 2, 3]:
        count = winning_counts[number]
        percentage = (count / steps) * 100
        print(f"Number {number}: {count:,} times ({percentage:.2f}%)")
    
    print("\nInitial Guess Distribution:")
    print("-" * 30)
    for number in [1, 2, 3]:
        count = initial_guess_counts[number]
        percentage = (count / steps) * 100
        print(f"Number {number}: {count:,} times ({percentage:.2f}%)")
    
    print("\nFinal Guess Distribution:")
    print("-" * 30)
    for number in [1, 2, 3]:
        count = final_guess_counts[number]
        percentage = (count / steps) * 100
        print(f"Number {number}: {count:,} times ({percentage:.2f}%)")
    
    print("\nWin Statistics:")
    print("-" * 30)
    initial_win_percentage = (initial_wins / steps) * 100
    final_win_percentage = (final_wins / steps) * 100
    
    print(f"Initial guess wins: {initial_wins:,} ({initial_win_percentage:.2f}%)")
    print(f"Final guess wins: {final_wins:,} ({final_win_percentage:.2f}%)")
    print(f"Improvement: {final_win_percentage - initial_win_percentage:.2f} percentage points")
    
    print("\nStrategy Analysis:")
    print("-" * 30)
    stay_percentage = (stayed_with_original / steps) * 100
    switch_percentage = (switched_guess / steps) * 100
    print(f"Stayed with original: {stayed_with_original:,} ({stay_percentage:.2f}%)")
    print(f"Switched guess: {switched_guess:,} ({switch_percentage:.2f}%)")
    
    print(f"\nExpected initial win rate: ~33.33% (1/3)")
    print(f"Expected final win rate: ~50.00% (1/2 after removal)")
    print("=" * 60)

if __name__ == "__main__":
    run_simulation()
