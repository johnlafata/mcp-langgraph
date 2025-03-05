# from fastapi import FastAPI

import os
from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(level=logging.INFO)

from mcp.server.fastmcp import FastMCP
import requests
from typing import List, Any

mcp = FastMCP("Trello")
# reference https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/

@mcp.tool()
def get_trello_boards(key: str, token: str) -> str:
    """List trello boards for the authenticated user.
    Args:
        key: api key
        token: account token
    """
    url=f"https://api.trello.com/1/members/me/boards?fields=id,name,url&key={key}&token={token}"
    response = requests.get(url)

    return response.json()

@mcp.tool()
def get_lists_on_board(key: str, token: str, idBoard: str) -> str:
    """retrieve the list of lists on the trello board with the id given vor the authenticated user
    Args:
        key: api key
        token: account token
        idBoard: board id
    """
    url=f"https://api.trello.com/1/boards/{idBoard}/lists?fields=id,name&key={key}&token={token}"
    response = requests.get(url)
    return response.json()

@mcp.tool()
def get_cards_from_a_list(key: str, token: str, idList: str) -> str:
    """retrieve the cards in a list with the id given for the authenticated user
    Args:
        key: api key
        token: account token
        idList: list id
    """
    url=f"https://api.trello.com/1/lists/{idList}/cards?fields=id,name&key={key}&token={token}"
    response = requests.get(url)
    return response.json()

def get_cards_from_a_list_on_a_board(key: str, token: str, board_name: str, list_name: str) -> str:
    """retrieve the cards in a list with the id given for the authenticated user
    Args:
        key: api key
        token: account token
        board_name: board name
        list_name: list name
    """
    # get the id of the board
    board_response=get_trello_boards(key, token)
    board_id=None;
    for board in board_response:
        if board.get("name").lower()==board_name.lower():
            board_id=board.get("id")
            break
    if board_id is None:
        return "Board not found"
    list_response=get_lists_on_board(key, token, board_id)
    list_id=None
    # get the id of the list on that board
    for list in list_response:
        if list.get("name").lower()==list_name.lower():
            list_id=list.get("id")
            break
    if list_id is None:
        return "List not found"
    # get the cards using the list id
    # return the list of cards
    card_list=get_cards_from_a_list(key, token, list_id)
    return card_list.json()

if __name__ == "__main__":
    mcp.run()
