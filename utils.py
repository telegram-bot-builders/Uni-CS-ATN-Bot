import pandas as pd

def filter_data(lst):
    filtered_data = [data for data in lst if (data['user']['linkedinUrl'] or data['user']['githubUrl']) and data['user']['profile']['countryName'] == 'United States'] 
    extracted_data = extract_user_info(filtered_data)
    return pd.DataFrame(extracted_data)


def extract_user_info(data):
    """
    Extracts specific user information from a list of user data dictionaries.

    Parameters:
    data (list): A list of dictionaries containing user data.

    Returns:
    list: A list of dictionaries with selected user information.
    """
    extracted_data = []

    for entry in data:
        user_info = entry['user'] # Convert string representation of dict to actual dict
        extracted_entry = {
            'username': user_info.get('username'),
            'linkedinUrl': user_info.get('linkedinUrl'),
            'githubUrl': user_info.get('githubUrl'),
            'country': user_info.get('profile', {}).get('countryName'),
            'currentRating': entry.get('currentRating')
        }
        extracted_data.append(extracted_entry)

    return extracted_data


if __name__ == '__main__':
    df = pd.read_csv('rankings.csv')
    df_filtered = filter_data(df)
    df_filtered.to_csv('filtered_rankings.csv', index=False)

