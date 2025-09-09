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
def play_game(draw_chance):
    board = [" "] * 9  # Initialize empty board
    current_player = "X"
    moves = list(range(9))  # List of all possible moves
    random.shuffle(moves)  # Shuffle moves to randomize gameplay

    if random.random() < draw_chance:
        return "Draw"

    for move in moves:
        board[move] = current_player
        winner = check_winner(board)
        if winner:
            return winner
        current_player = "O" if current_player == "X" else "X"

    return "Draw"

# Function to simulate a single best-of-N series
def simulate_games(num_games, draw_chance):
    results = {"X": 0, "O": 0, "Draw": 0}
    total_money = 2  # Flat entry fee per series
    platform_fee = total_money * 0.20
    prize_pool = total_money - platform_fee

    for _ in range(num_games):
        result = play_game(draw_chance)
        results[result] += 1

    if results["X"] > results["O"]:
        winner = "X"
        payout = prize_pool
    elif results["O"] > results["X"]:
        winner = "O"
        payout = prize_pool
    else:
        winner = "Draw"
        payout = 0

    return results, winner, payout, platform_fee

# Function to simulate multiple tournament instances
def simulate_instances(num_games, num_instances, draw_chance):
    total_platform_earnings = 0
    total_revenue = 0
    total_payouts = 0
    draw_instances = 0
    total_draw_refunds = 0

    for i in range(num_instances):
        print(f"\nInstance {i + 1}:")
        results, winner, payout, platform_fee = simulate_games(num_games, draw_chance)
        instance_revenue = 2  # Each instance generates $2 in total

        if winner == "Draw":
            draw_instances += 1
            total_draw_refunds += instance_revenue
            platform_fee = 0  # Platform earns nothing on a draw

        total_platform_earnings += platform_fee
        total_revenue += instance_revenue
        total_payouts += payout

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
    print(f"Total Refunded Due to Draws: ${total_draw_refunds:,.2f}")

    calculated_total = total_platform_earnings + total_payouts + total_draw_refunds
    if round(total_revenue, 2) != round(calculated_total, 2):
        print(f"\nERROR: Accounting mismatch!")
        print(f"  Revenue:            ${total_revenue:,.2f}")
        print(f"  Platform Earnings:  ${total_platform_earnings:,.2f}")
        print(f"  Payouts:            ${total_payouts:,.2f}")
        print(f"  Refunds (Draws):    ${total_draw_refunds:,.2f}")
        print(f"  Difference:         ${total_revenue - calculated_total:,.6f}")
        raise AssertionError("Mismatch in accounting!")

# Main execution block
if __name__ == "__main__":
    num_games = int(input("Enter the number of games per instance (e.g., 3, 5, or 7): "))
    num_instances = int(input("Enter the number of instances to run: "))
    draw_chance = float(input("Enter the likelihood of a draw (0 to 1): "))
    simulate_instances(num_games, num_instances, draw_chance)
