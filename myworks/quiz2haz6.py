def record_match(scores_dict, team_name, points):

    if points < 0:
        print("Invalid score!")
        return False
    else:
        if team_name not in scores_dict:
            scores_dict[team_name] = []

        scores_dict[team_name].append(points)
        print(f"Recorded {points} pts for {team_name}.")
        return True

def get_standings(scores_dict):
    standings = []
    for team in scores_dict:
        team_name = team
        total_points = sum(scores_dict[team])
        match_count = len(scores_dict[team])
        standings.append((team_name, total_points, match_count))
    return standings

team_scores = {
    "Dragons": [12, 15, 10],
    "Vipers": [8, 9],
    "Phoenix": []
}

user_input = input("Enter team name (or 'done' to finish): ")

while user_input != "done":
    point_input = int(input("Enter match points: "))
    record_match(team_scores, user_input, point_input)
    user_input = input("Enter team name (or 'done' to finish): ")

standlist = get_standings(team_scores)

print("\n --- TOURNAMENT STANDINGS ---")

for team, total, matches in standlist:
    if matches <= 0:
        print(f"{team}: No matches played")
    else:
        print(f"{team}: {total} pts ({matches} matches)")
