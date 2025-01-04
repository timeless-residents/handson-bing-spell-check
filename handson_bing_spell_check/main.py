"""
This module provides a function to check spelling using the Bing Spell Check API.
It includes proper error handling and debugging information.
"""

import json
import os

import requests
from dotenv import load_dotenv


def check_spelling(text, api_key):
    """
    Check spelling using Bing Spell Check API with proper error handling
    and debugging information.

    Args:
        text (str): Text to check for spelling
        api_key (str): Bing Spell Check API key

    Returns:
        dict: JSON response from the API
    """
    # Updated endpoint URL (using HTTPS)
    endpoint = "https://api.bing.microsoft.com/v7.0/spellcheck"

    # Updated headers based on Microsoft's documentation
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Ocp-Apim-Subscription-Key": api_key,
    }

    # Updated parameters
    params = {"mkt": "en-US", "mode": "proof", "text": text}  # Note: Case sensitive

    try:
        # Make the request with debugging information
        print(f"Making request to: {endpoint}")
        print(f"Headers: {json.dumps(headers, indent=2)}")
        print(f"Parameters: {json.dumps(params, indent=2)}")

        response = requests.post(endpoint, headers=headers, params=params, timeout=10)

        # Print response status and headers for debugging
        print(f"\nResponse Status: {response.status_code}")
        print(f"Response Headers: {json.dumps(dict(response.headers), indent=2)}")

        # Check if the response was successful
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"\nError making request: {str(e)}")
        if hasattr(e.response, "text"):
            print(f"Error response: {e.response.text}")
        return None


def main():
    """
    Main function to perform spell check using Bing Spell Check API.

    This function sets the API key and the text to be checked for spelling errors.
    It then calls the check_spelling function with the provided text and API key,
    and prints the API response if the spell check is successful.

    Note:
        Replace the placeholder API key with your actual Bing Spell Check API key.

    Returns:
        None
    """
    # Your API key
    # Load environment variables from a .env file
    load_dotenv()

    # Get the API key from environment variables
    api_key = os.getenv("BING_SPELL_CHECK_API_KEY")

    # Test text
    text_to_check = "Hollo, wrld!"

    # Attempt the spell check
    result = check_spelling(text_to_check, api_key)

    if result:
        print("\nAPI Response:")
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
