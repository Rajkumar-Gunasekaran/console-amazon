def min_teams(team_size1, team_size2, participants):
    for i in range(participants // team_size1 + 1):
        for j in range(participants // team_size2 + 1):
            if team_size1 * i + team_size2 * j == participants:
                return i + j
    return -1

# Example usage:
team_size1 = 3
team_size2 = 5
participants = 11
print(min_teams(team_size1, team_size2, participants))  # Output: 3