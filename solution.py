import json

def read_data_from_json(file_name: str = 'data.json'):
    """Reads data from a JSON file."""
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def filter_messages_by_user(messages, user_id):
    """Filters messages based on the user_id."""
    return [message for message in messages if message["user_id"] == user_id]

def solution(array_of_users, target_id):
    """Sorts users based on unread messages and adds a 'Tag' field."""
    for user in array_of_users:
        user_messages = filter_messages_by_user(user.get("messages", []), target_id)
        has_unread_messages = any(not message["read"] for message in user_messages)
        user["Tag"] = "unread" if has_unread_messages else "read"

    return array_of_users

# Read data from JSON file
data_array = read_data_from_json('data.json')

# Example usage:
sorted_array = solution(data_array, 30)
print(sorted_array)
