from fastapi import FastAPI
import requests
from typing import List, Any

import os
from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(level=logging.INFO)

from pydantic_trello_model import TrelloBoard
import json


def get_trello_board_list() -> str:
    key=os.getenv('TRELLO_API_KEY')
    logging.debug(f'key: {key}')
    token=os.getenv('TRELLO_ACCOUNT_TOKEN')
    logging.debug(f'token: {token}') 
    url=f"https://api.trello.com/1/members/me/boards?fields=name,url&key={key}&token={token}"
    response = requests.get(url)

    return response.json()

def get_lists_on_board(idBoard: str) -> str:
    key=os.getenv('TRELLO_API_KEY')
    logging.debug(f'key: {key}')
    token=os.getenv('TRELLO_ACCOUNT_TOKEN')
    logging.debug(f'token: {token}') 
    url=f"https://api.trello.com/1/boards/{idBoard}/lists?key={key}&token={token}"
    response = requests.get(url)
    return response.json()


def get_cards_from_a_list(idList: str) -> str:
    key=os.getenv('TRELLO_API_KEY')
    logging.debug(f'key: {key}')
    token=os.getenv('TRELLO_ACCOUNT_TOKEN')
    logging.debug(f'token: {token}') 
    url=f"https://api.trello.com/1/lists/{idList}/cards?fields=id,name&key={key}&token={token}"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    # print(get_trello_board_list())
    # print(get_trello_board_by_name("garage"))
    print(get_lists_on_board("59ea562b43d6fb027bbe7742"))
    print("---")
    print(get_cards_from_a_list("65fc76b2ab28f5bab326822c"))

