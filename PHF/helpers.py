
STAT_COLUMNS = [
    'jersey',
    'player_name',
    'team',
    'position',
    'games_played',
    'goals',
    'assists',
    'points',
    'shots_on_goal',
    'plus_minus',
    'faceoff_record',
    'blocks',
    'penalty_minutes',
    'takeaways',
    'giveaways',
    'shot_pct',
    'power_play_goal',
    'short_hand_goal',
    'game_winning_goal',
    'points_per_game',
    'faceoff_win_pct',
    'shots_blocked',
    'shots',
]

GAME_STAT_COLUMNS = [
    'jersey',
    'player_name',
    'position',
    'goals',
    'assists',
    'points',
    'penalty_minutes',
    'plus_minus',
    'shots_on_goal',
    'blocks',
    'giveaways',
    'takeaways',
    'faceoff_record',
    'faceoff_win_pct',
    'power_play_goal',
    'short_hand_goal',
    'shots_blocked',
    'shots',
    'faceoff_won',
    'faceoff_lost',
    'team',
]

FINAL_STAT_COLUMNS = [
    'player_name',
    'player_id',
    'jersey',
    'team',
    'position',
    'season',
    'season_id',
    'season_type',
    'league',
    'division_id',
    'games_played',
    'goals',
    'assists',
    'points',
    'points_per_game',
    'shots',
    'shots_blocked',
    'shots_on_goal',
    'shot_pct',
    'power_play_goal',
    'short_hand_goal',
    'game_winning_goal',
    'plus_minus',
    'faceoff_record',
    'faceoff_win_pct',
    'faceoff_won',
    'faceoff_lost',
    'blocks',
    'penalty_minutes',
    'takeaways',
    'giveaways',
]

GAME_FINAL_STAT_COLUMNS = [
    'player_name',
    'player_id',
    'jersey',
    'team',
    'position',
    'game_id',
    'goals',
    'assists',
    'points',
    'shots',
    'shots_blocked',
    'shots_on_goal',
    'shot_pct',
    'power_play_goal',
    'short_hand_goal',
    'plus_minus',
    'faceoff_record',
    'faceoff_win_pct',
    'faceoff_won',
    'faceoff_lost',
    'blocks',
    'penalty_minutes',
    'takeaways',
    'giveaways',
]

STANDINGS_COLS = [
    'team_name',
    'gp',
    'wins',
    'losses',
    'ties',
    'points',
    'regulation_wins',
    'overtime_wins',
    'shootout_wins',
    'goals_scored',
    'goals_allowed',
    'goal_differential',
    'penalty_minutes',
    'next_game',
]

ROSTER_NAMES = [
    'jersey',
    'player_name',
    'position',
    'height',
    'date_of_birth',
    'country',
    'home_town',
    'college',
    'player_id',
    'player_photo',
    'is_captain',
    'feet', 
    'inches',
]

ROSTER_COLUMNS = [
    'player_name',
    'player_id',
    'jersey',
    'position',
    'date_of_birth',
    'season',
    'team',
    'team_id',
    'height',
    'feet', 
    'inches',
    'home_town',
    'country',
    'college',
    'is_captain',
    'player_photo'
]

GOALIE_COL = [
    'jersey',
    'player_name',
    'team',
    'games_played',
    'wins',
    'losses',
    'ties',
    'overtime_losses',
    'time_on_ice',
    'shots_against',
    'goals_allowed',
    'save_pct',
    'goals_against_average',
    'shutouts',
    'saves',
    'penalty_minutes',
    'goals',
    'assists',
    'games_started',
    'minutes',
    'seconds',
    'minutes_played',
]

FINAL_GOALIE_COLUMNS = [
    'player_name',
    'player_id',
    'jersey',
    'team',
    'position',
    'season',
    'season_id',
    'season_type',
    'league',
    'division_id',
    'games_played',
    'games_started',
    'time_on_ice',
    'minutes_played',
    'wins',
    'losses',
    'ties',
    'overtime_losses',
    'shots_against',
    'saves',
    'goals_allowed',
    'save_pct',
    'goals_against_average',
    'shutouts',
    'penalty_minutes',
    'goals',
    'assists',
]

TEAM_SKATER_COLS = [
    'jersey',
    'player_name',
    'position',
    'games_played',
    'goals',
    'assists',
    'points',
    'shots_on_goal',
    'plus_minus',
    'faceoff_record',
    'blocks',
    'penalty_minutes',
    'takeaways',
    'giveaways',
    'shot_pct',
    'power_play_goal',
    'short_hand_goal',
    'game_winning_goal',
    'points_per_game',
    'faceoff_win_pct',
    'shots_blocked',
    'shots',
    'season_type',
    'player_id',
    'faceoff_won',
    'faceoff_lost',
    'team'
]

TEAM_GOALIE_COLS = [
    'jersey',
    'player_name',
    'games_played',
    'wins',
    'losses',
    'ties',
    'overtime_losses',
    'time_on_ice',
    'shots_against',
    'goals_allowed',
    'save_pct',
    'goals_against_average',
    'shutouts',
    'saves',
    'penalty_minutes',
    'goals',
    'assists',
    'games_started',
    'season_type',
    'player_id',
    'minutes',
    'seconds',
    'minutes_played',
    'team'
]

START_NAMES = ["team", "period_1_scoring", "total_scoring"]
IN_PROG_NAMES = ["team","period_1_scoring","period_2_scoring", "total_scoring"]
REG_NAMES = ["team","period_1_scoring","period_2_scoring",
                "period_3_scoring", "total_scoring"]
OT_ONLY_NAMES = ["team","period_1_scoring","period_2_scoring",
                    "period_3_scoring", "overtime_scoring",
                    "total_scoring"]
SHOOTOUT_SCORING_INIT_NAMES = ["team","period_1_scoring","period_2_scoring",
                    "period_3_scoring", "overtime_scoring",
                    "shootout_made_scoring",  "total_scoring", "shootout_missed_scoring"]
SHOOTOUT_NAMES = ["team","period_1_scoring","period_2_scoring",
                    "period_3_scoring", "overtime_scoring",
                    "shootout_made_scoring", "shootout_missed_scoring", "total_scoring"]
SHOOTOUT_SHOT_INIT_NAMES = ["team","period_1_shots","period_2_shots",
                            "period_3_shots", "overtime_shots", "total_shots",
                            "shootout_made_shots","shootout_missed_shots"]
SHOOTOUT_SHOT_NAMES = ["team","period_1_shots","period_2_shots",
                        "period_3_shots", "overtime_shots",
                        "shootout_made_shots","shootout_missed_shots", "total_shots"]

PHF_SCHEDULE = ['type', 'id', 'league_id', 'season_id', 'tournament_id', 'game_id', 'game_date',
       'winner', 'attendance', 'home_team_id', 'home_team',
       'home_team_short', 'home_team_logo_url', 'away_team_id', 'away_team',
       'away_team_short', 'away_team_logo_url', 'home_division_id',
       'home_division', 'away_division_id', 'away_division', 'home_score',
       'away_score', 'facility_id', 'facility', 'facility_address', 'rink_id',
       'rink', 'game_type',
       'number', 'datetime', 'datetime_tz', 'time_zone', 'time_zone_abbr',
       'updated_at', 'created_at', 'notes', 'status', 'overtime', 'shootout',
       'allow_players', 'tickets_url', 'watch_live_url', 'external_url',
       'has_play_by_play', 'highlight_color']