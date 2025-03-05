"""Functions for fetching FPL data from the official API.

This module provides functions to retrieve user team data, player statistics,
fixtures, and manager details.
"""

import requests
import pandas as pd

def fetch_user_team(user_id, gameweek):
    """Fetch the user's team data for a specific gameweek.
    
    Args:
        user_id (int): The user's unique ID.
        gameweek (int): The gameweek number.

    Returns:
        dict: The user's team data for the specified gameweek.
    """
    url = f"https://fantasy.premierleague.com/api/entry/{user_id}/event/{gameweek}/picks/"
    response = requests.get(url).json()
    return response

def fetch_player_data():
    """Fetch player statistics, prices, and other relevant data.

    Returns:
        pd.DataFrame: A DataFrame containing player statistics.
    """
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(url).json()
    players = pd.DataFrame(response['elements'])
    return players

def fetch_fixtures():
    """Fetch the upcoming fixture data.
    
    Returns:
        pd.DataFrame: A DataFrame containing fixture data.
    """
    url = "https://fantasy.premierleague.com/api/fixtures/"
    response = requests.get(url).json()
    fixtures = pd.DataFrame(response)
    return fixtures

def fetch_manager_details(user_id):
    """Fetch the manager's name, team name, budget, and available transfers.
    
    Args:
        user_id (int): The user's unique ID.

    Returns:
        dict: The manager's details.
    """
    url = f"https://fantasy.premierleague.com/api/entry/{user_id}/"
    response = requests.get(url).json()
    return {
        "manager_name": response["name"],
        "team_name": response["player_first_name"] + " " + response["player_last_name"],
        "budget": response["last_deadline_bank"] / 10,
        "transfers": response["last_deadline_value"] / 10
    }
