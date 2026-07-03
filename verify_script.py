import sys
import os

# Add the current directory to path so we can import swgoh_tracker
sys.path.append(os.getcwd())

from swgoh_tracker.api_client import fetch_player_data
from swgoh_tracker.data_manager import add_member, remove_member, load_members, DATA_FILE

def test_api():
    print("Testing API...")
    # Using the ally code provided by user: 829582985
    data = fetch_player_data("829582985")
    if data:
        print("API Success!")
        print(f"Name: {data.get('data', {}).get('name')}")
    else:
        print("API Failed!")

def test_data_manager():
    print("\nTesting Data Manager...")
    # Clean up before test
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    
    add_member("123456789")
    members = load_members()
    if "123456789" in members:
        print("Add Member: Success")
    else:
        print("Add Member: Failed")

    remove_member("123456789")
    members = load_members()
    if "123456789" not in members:
        print("Remove Member: Success")
    else:
        print("Remove Member: Failed")

if __name__ == "__main__":
    test_api()
    test_data_manager()
