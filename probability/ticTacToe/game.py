import random

# Function to check if there is a winner
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]  # Return the winning symbol ('X' or 'O')
    
    return None  # No winner yet

# Function to play a single game
def play_game():
    board = [" "] * 9  # Initialize empty board
    current_player = "X"
    moves = list(range(9))  # List of all possible moves
    random.shuffle(moves)  # Shuffle moves to randomize gameplay
    
    # Introduce a 60% probability of a draw
    if random.random() < 0.3:
        return "Draw"
    
    for move in moves:
        board[move] = current_player  # Make move
        winner = check_winner(board)  # Check for winner
        if winner:
            return winner  # Return winner if found
        current_player = "O" if current_player == "X" else "X"  # Switch player
    
    return "Draw"  # Return Draw if no winner

# Function to simulate multiple games and calculate payouts
def simulate_games(num_games):
    results = {"X": 0, "O": 0, "Draw": 0}  # Dictionary to store results
    total_money = num_games * 2  # Each player pays $1 per game
    platform_fee = total_money * 0.1  # Platform keeps 10%
    prize_pool = total_money - platform_fee  # Remaining money for winner
    
    for _ in range(num_games):
        result = play_game()
        results[result] += 1  # Increment respective count
    
    if results["X"] > results["O"]:
        winner = "X"
        payout = prize_pool
    elif results["O"] > results["X"]:
        winner = "O"
        payout = prize_pool
    else:  # If it's a draw
        winner = "Draw"
        payout = 0  # Players get their money back
        platform_fee = 0  # Platform earns nothing
    
    return results, winner, payout, platform_fee

# Function to simulate multiple instances of games
def simulate_instances(num_games, num_instances):
    total_platform_earnings = 0
    total_revenue = 0
    total_payouts = 0
    draw_instances = 0
    
    for i in range(num_instances):
        print(f"\nInstance {i + 1}:")
        results, winner, payout, platform_fee = simulate_games(num_games)
        total_platform_earnings += platform_fee
        total_revenue += num_games * 2
        total_payouts += payout
        
        if winner == "Draw":
            draw_instances += 1
        
        # Display results for this instance
        print(f"X Wins: {results['X']}")
        print(f"O Wins: {results['O']}")
        print(f"Draws: {results['Draw']}")
        print(f"Platform Earnings: ${platform_fee:,.2f}")
        
        if winner == "Draw":
            print("The series was a draw. Players get their money back. Platform earns nothing.")
        else:
            print(f"Winner of the series: {winner}")
            print(f"Total payout to {winner}: ${payout:,.2f}")
    
    print(f"\nTotal Instances Run: {num_instances}")
    print(f"Total Draw Instances: {draw_instances}")
    print(f"Total Revenue Collected: ${total_revenue:,.2f}")
    print(f"Total Payouts to Winners: ${total_payouts:,.2f}")
    print(f"Total Platform Earnings: ${total_platform_earnings:,.2f}")

# Main execution block
if __name__ == "__main__":
    num_games = int(input("Enter the number of games per instance: "))  # Get user input
    num_instances = int(input("Enter the number of instances to run: "))  # Get number of instances
    simulate_instances(num_games, num_instances)  # Run simulations