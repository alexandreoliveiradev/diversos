import json
import sys
import re
from datetime import datetime
from collections import defaultdict

# ----------------------------
# Configuration
# ----------------------------
DATE_PATTERN = re.compile(r"\d{2}\.\d{2}\.\s\d{2}:\d{2}")
ROUND_PATTERN = re.compile(r"Ronda\s+\d+", re.IGNORECASE)

# ----------------------------
# Function to parse games
# ----------------------------
def parse_games_to_json(file_path):
    games = []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    i = 0
    while i < len(lines):
        # Skip round headers like "Ronda 14"
        if ROUND_PATTERN.fullmatch(lines[i]):
            i += 1
            continue

        # Only start parsing when a date line is found
        if not DATE_PATTERN.fullmatch(lines[i]):
            i += 1
            continue

        try:
            raw_date = lines[i]  # e.g., "29.12. 20:15"
            day, month, time = raw_date.split(".")[0], raw_date.split(".")[1], raw_date.split(".")[2].strip()
            month_int = int(month)
            # Determine season year
            if month_int >= 8:
                year = 2025
            elif month_int <= 6:
                year = 2026
            else:
                year = 2025  # fallback, in case data has Mar-Jul (optional)

            dt = datetime.strptime(f"{raw_date} {year}", "%d.%m. %H:%M %Y")

            game = {
                "date": dt.strftime("%Y-%m-%d (%A)"),  # formatted for output
                "datetime": dt,                        # keep for logic
                "team1": lines[i + 1],
                "team2": lines[i + 3],
                "score": f"{int(lines[i + 5])}:{int(lines[i + 6])}"
            }

            games.append(game)
            i += 7  # move to next game block
        except (IndexError, ValueError):
            i += 1  # skip malformed block safely

    return games

# ----------------------------
# Main script
# ----------------------------
if __name__ == "__main__":
    file_path = r"C:\Users\alexd\Documents\repos\diversos\games_text.txt"
    games = parse_games_to_json(file_path)
    
    try:
        day = int(sys.argv[1]) if len(sys.argv) > 1 else 0
        if day < 0 or day > 6:
            print("Invalid day argument. Must be 0-6 or null for Monday.")
            exit()
    except ValueError:
        print("Invalid argument. Must be an integer 0-6 or null for Monday.")
        exit()  

    # Count day (0 mon, 1 tue, etc) games per team
    day_games = defaultdict(int)
    for game in games:
        if game["datetime"].weekday() == day: 
            day_games[game["team1"]] += 1
            day_games[game["team2"]] += 1
    
    day_str = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }.get(day, "Monday")

    print("\n" + day_str + " games per team:\n")
    # Include all teams, even if 0
    all_teams = set()
    for game in games:
        all_teams.add(game["team1"])
        all_teams.add(game["team2"])

    for team in sorted(all_teams):
        if day_games.get(team, 0) > 0:
            print(f"{team}: {day_games.get(team, 0)}")
