import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.nba.com/stats')
time.sleep(5)

def get_top_5_data(players_xpath, teams_xpath):
    players = driver.find_elements(By.XPATH, players_xpath)
    teams = driver.find_elements(By.XPATH, teams_xpath)
    length = min(len(players), len(teams), 5)
    player_data = [f"{players[i].text}" for i in range(length)]
    team_data = [f"{teams[i].text}" for i in range(length)]
    return player_data, team_data


points_players = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[1]/div/table'
points_teams = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[5]/div/div[4]/div[1]/div/table'

rebounds_players = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[2]/div/table'
rebounds_teams = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[5]/div/div[4]/div[2]/div/table'

assists_players = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[3]/div/table'
assists_teams = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[5]/div/div[4]/div[3]/div/table'

blocks_players = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[4]/div/table'
blocks_teams = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[5]/div/div[4]/div[4]/div/table'

steals_players = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[5]/div/table'
steals_teams = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[5]/div/div[4]/div[5]/div/table'

fg_percentage_players = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[6]/div/table'
fg_percentage_teams = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[5]/div/div[4]/div[6]/div/table'

three_pointers_players = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[7]/div/table'
three_pointers_teams = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[5]/div/div[4]/div[7]/div/table'

three_point_percentage_players = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[4]/div[8]/div/table'
three_point_percentage_teams = '/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/section[5]/div/div[4]/div[8]/div/table'


points_leaders, team_points_leaders = get_top_5_data(points_players, points_teams)
rebounds_leaders, team_rebounds_leaders = get_top_5_data(rebounds_players, rebounds_teams)
assists_leaders, team_assists_leaders = get_top_5_data(assists_players, assists_teams)
blocks_leaders, team_blocks_leaders = get_top_5_data(blocks_players, blocks_teams)
steals_leaders, team_steals_leaders = get_top_5_data(steals_players, steals_teams)
fg_percentage_leaders, team_fg_percentage_leaders = get_top_5_data(fg_percentage_players, fg_percentage_teams)
three_pointers_made_leaders, team_three_pointers_made_leaders = get_top_5_data(three_pointers_players, three_pointers_teams)
three_point_percentage_leaders, team_three_point_percentage_leaders = get_top_5_data(three_point_percentage_players, three_point_percentage_teams)

data = {
    "": ["Players", "Teams"],
    "Points Per Game": [", ".join(points_leaders), ", ".join(team_points_leaders)],
    "Rebounds Per Game": [", ".join(rebounds_leaders), ", ".join(team_rebounds_leaders)],
    "Assists Per Game": [", ".join(assists_leaders), ", ".join(team_assists_leaders)],
    "Blocks Per Game": [", ".join(blocks_leaders), ", ".join(team_blocks_leaders)],
    "Steals Per Game": [", ".join(steals_leaders), ", ".join(team_steals_leaders)],
    "Field Goal Percentage": [", ".join(fg_percentage_leaders), ", ".join(team_fg_percentage_leaders)],
    "Three Pointers Made": [", ".join(three_pointers_made_leaders), ", ".join(team_three_pointers_made_leaders)],
    "Three Point Percentage": [", ".join(three_point_percentage_leaders), ", ".join(team_three_point_percentage_leaders)],
}

df = pd.DataFrame(data)
df.to_csv('nba_top_5_players_teams.csv', index=False)
driver.quit()

print("Data scraped and saved to nba_top_5_players_teams.csv")
