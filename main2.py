import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
player_driver = webdriver.Chrome(options=chrome_options)
player_driver.get('https://www.espn.com/nba/stats')

team_driver = webdriver.Chrome(options=chrome_options)
team_driver.get('https://www.espn.com/nba/stats/_/view/team')
time.sleep(5)

def get_top_5_data(players_xpath, teams_xpath):
    players = player_driver.find_elements(By.XPATH, players_xpath)
    teams = team_driver.find_elements(By.XPATH, teams_xpath)
    length = min(len(players), len(teams), 5)
    player_data = [f"{players[i].text}" for i in range(length)]
    team_data = [f"{teams[i].text}" for i in range(length)]
    return player_data, team_data


points_players = '/html/body/div[1]/div/div/div/div/main/div[2]/div[2]/div/div/section[1]/div/div[4]/div[1]/div/div[2]/div/div/div[2]/table/tbody'
points_teams = '/html/body/div[1]/div/div/div/div/main/div[2]/div[2]/div/div/section[1]/div/div[4]/div[1]/div/div[2]/div/div/div[2]/table/tbody'

rebounds_players = '/html/body/div[1]/div/div/div/div/main/div[2]/div[2]/div/div/section[1]/div/div[4]/div[2]/div/div[2]/div/div/div[2]/table/tbody'
rebounds_teams = '/html/body/div[1]/div/div/div/div/main/div[2]/div[2]/div/div/section[1]/div/div[4]/div[2]/div/div[3]/div/div/div[2]/table/tbody'

blocks_players = '/html/body/div[1]/div/div/div/div/main/div[2]/div[2]/div/div/section[1]/div/div[4]/div[2]/div/div[3]/div/div/div[2]/table/tbody'
blocks_teams = '/html/body/div[1]/div/div/div/div/main/div[2]/div[2]/div/div/section[1]/div/div[4]/div[2]/div/div[4]/div/div/div[2]/table/tbody'





points_leaders, team_points_leaders = get_top_5_data(points_players, points_teams)
rebounds_leaders, team_rebounds_leaders = get_top_5_data(rebounds_players, rebounds_teams)
blocks_leaders, team_blocks_leaders = get_top_5_data(blocks_players, blocks_teams)

data = {
    "": ["Players", "Teams"],
    "Points Per Game": [", ".join(points_leaders), ", ".join(team_points_leaders)],
    "Rebounds Per Game": [", ".join(rebounds_leaders), ", ".join(team_rebounds_leaders)],
    "Blocks Per Game": [", ".join(blocks_leaders), ", ".join(team_blocks_leaders)],
}

df = pd.DataFrame(data)
df.to_csv('nba_top_5_players_teams_season2324.csv', index=False)

player_driver.quit()
team_driver.quit()