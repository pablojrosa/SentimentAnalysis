import requests
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

def get_category_id(category_name):
    """
    Retrieves the ID of a category from the MercadoLibre API based on its name.

    Args:
        category_name (str): The name of the category.

    Returns:
        str or int: The ID of the category if found, or an error message if the request fails.

    """
    MELI_AUTH_TOKEN = os.getenv("MELI_AUTH_TOKEN")
    url = "https://api.mercadolibre.com/sites/MLA/categories"

    headers = {"Authorization": "Bearer " + MELI_AUTH_TOKEN}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        item_id = [item for item in json_response if item["name"] == category_name][0]["id"]
        return item_id
    else:
        return "Error at categories request"

def get_listed_items(category_id, num_pages):
    """
    Retrieves a list of item IDs from the MercadoLibre API based on the provided category ID and number of pages.

    Args:
        category_id (str): The ID of the category to search for items.
        num_pages (int): The number of pages to retrieve items from.

    Returns:
        list: A list of item IDs.

    Raises:
        str: If there is an error during the search items request.

    """
    MELI_AUTH_TOKEN = os.getenv("MELI_AUTH_TOKEN")
    url = "https://api.mercadolibre.com/sites/MLA/search?category=" + category_id

    headers = {"Authorization": "Bearer " + MELI_AUTH_TOKEN}

    all_results = []
    for page_number in range(1, num_pages + 1):
        params = {
            "limit": 50,
            "offset": (page_number - 1) * 50
        }
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            json_response = response.json()
            list_of_items = json_response["results"]
            for item in list_of_items:
                all_results.append({"id":item["id"],
                                   "title":item["title"]})
        else:
            return "Error at search items request"
    
    return all_results

def get_item_reviews(item_id, title, num_pages):
    """
    Retrieves reviews for a given item from the MercadoLibre API.

    Args:
        item_id (str): The ID of the item for which to retrieve reviews.
        num_pages (int): The number of pages of reviews to retrieve.

    Returns:
        list: A list of dictionaries representing the item reviews. Each dictionary contains the following keys:
            - item_id (str): The ID of the item.
            - rate (int): The rating given to the item.
            - content (str): The content of the review.

    Raises:
        str: If there is an error during the request to retrieve the item reviews.

    """
    MELI_AUTH_TOKEN = os.getenv("MELI_AUTH_TOKEN")

    url = "https://api.mercadolibre.com/reviews/item/"+item_id

    headers = {"Authorization": "Bearer " + MELI_AUTH_TOKEN}

    all_item_reviews = []
    for page_number in range(1, num_pages + 1):
        params = {
            "limit": 50,
            "offset": (page_number - 1) * 50
        }
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            json_response = response.json()
            list_of_reviews = json_response["reviews"]
            for item in list_of_reviews:
                item_review = {"title":title,
                "item_id":item_id,
                               "rate":item["rate"],
                               "content":item["content"]}
                all_item_reviews.append(item_review)
        else:
            return "Error at search items request"

    return all_item_reviews

def get_all_reviews(list_itmes, num_pages):
    """
    Retrieves and processes reviews for a list of items.

    This function fetches reviews for each item in the provided list and processes 
    them to determine their sentiment based on the review rating. The reviews are
    then saved to a CSV file.

    Args:
        list_itmes (list): A list of dictionaries, where each dictionary contains
                           information about an item, specifically including "id" 
                           and "title" keys.
        num_pages (int): The number of pages of reviews to retrieve for each item.

    Returns:
        None

    Side Effects:
        Writes a CSV file named 'item_reviews.csv' containing the reviews data 
        with an additional column for sentiment.
    """
    all_reviews = []
    for item_id in list_itmes:
        title = item_id["title"]
        item_reviews = get_item_reviews(item_id["id"],title, num_pages)
        all_reviews.extend(item_reviews)

    df_reviews = pd.DataFrame(all_reviews)

    df_reviews["sentiment"] = df_reviews["rate"].apply(lambda x: "Positive" if x >= 4 else "Negative")

    df_reviews.to_csv("data/item_reviews.csv", index=False)

def run_all():
    """
    Orchestrates the complete process of retrieving reviews for a specific category.

    This function fetches the category ID for "Celulares y Teléfonos", retrieves 
    a list of items within this category, and then gathers reviews for those items 
    by calling the `get_all_reviews` function.

    Args:
        None

    Returns:
        None
    """
    category_id = get_category_id("Celulares y Teléfonos")
    list_times = get_listed_items(category_id, 1)
    get_all_reviews(list_times, num_pages=1)

run_all()

