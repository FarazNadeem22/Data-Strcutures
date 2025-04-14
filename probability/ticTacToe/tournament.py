import random

# Function to simulate a single game
def play_game():
    # 70% chance of a tie
    if random.random() < 0.70:
        return "Tie"
    return random.choice(["X", "O"])

# Function to simulate a tournament round
def play_round(players):
    winners = []
    for i in range(0, len(players), 2):
        if i + 1 < len(players):
            result = play_game()
            if result != "Tie":
                winners.append(result)
            # If tie, neither player advances
            # If opponent gets a walkover, they advance
        else:
            winners.append(players[i])
    return winners

# Function to simulate the tournament
def simulate_tournament():
    total_revenue = 16 * 2  # $2 per player
    platform_fee = 6.5
    remaining_pot = total_revenue - platform_fee

    # Quarter-finalist payouts ($1 each)
    if len(play_round(list(range(16)))) >= 8:
        quarter_finalist_payout = 1 * 4
        remaining_pot -= quarter_finalist_payout
    else:
        quarter_finalist_payout = 0

    # Semi-finalist payouts ($1.50 each)
    semi_finalists = play_round(list(range(8)))
    if len(semi_finalists) >= 4:
        semi_finalist_payout = 1.5 * 2
        remaining_pot -= semi_finalist_payout
    else:
        semi_finalist_payout = 0

    # Winner and runner-up payouts
    final_round = play_round(semi_finalists)
    if len(final_round) == 2:
        winner_payout = remaining_pot * 0.75
        runner_up_payout = remaining_pot * 0.25 + 1.0 # Add extra $1 to runner-up
    elif len(final_round) == 1:
        # If only one finalist, they win the entire pot
        winner_payout = remaining_pot
        runner_up_payout = 0
    elif len(final_round) == 0:
        # If both finalists tie, split the pot equally
        winner_payout = remaining_pot * 0.5
        runner_up_payout = remaining_pot * 0.5
    else:
        # If no one makes it to the final, platform keeps the pot
        winner_payout = 0
        runner_up_payout = 0
        platform_fee += remaining_pot
        remaining_pot = 0

    return total_revenue, platform_fee, quarter_finalist_payout, semi_finalist_payout, winner_payout, runner_up_payout

# Function to simulate multiple tournaments (Monte Carlo simulation)
def simulate_tournaments(num_tournaments):
    total_revenue = 0
    total_platform_fee = 0
    total_quarter_finalist_payout = 0
    total_semi_finalist_payout = 0
    total_winner_payout = 0
    total_runner_up_payout = 0

    for _ in range(num_tournaments):
        revenue, platform_fee, qf_payout, sf_payout, winner_payout, runner_up_payout = simulate_tournament()
        total_revenue += revenue
        total_platform_fee += platform_fee
        total_quarter_finalist_payout += qf_payout
        total_semi_finalist_payout += sf_payout
        total_winner_payout += winner_payout
        total_runner_up_payout += runner_up_payout

    print("\nSimulation Results:")
    print(f"Total Tournaments Run: {num_tournaments}")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Total Platform Fees: ${total_platform_fee:,.2f}")
    print(f"Total Quarter-Finalist Payouts: ${total_quarter_finalist_payout:,.2f}")
    print(f"Total Semi-Finalist Payouts: ${total_semi_finalist_payout:,.2f}")
    print(f"Total Winner's Payout: ${total_winner_payout:,.2f}")
    print(f"Total Runner-Up's Payout: ${total_runner_up_payout:,.2f}")

# Main execution block
if __name__ == "__main__":
    num_tournaments = int(input("Enter the number of tournament instances to simulate: "))
    simulate_tournaments(num_tournaments)
