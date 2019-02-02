import requests

def search_businesses():

    api_key = "lJITUJtIDXfqLXFgchBz_M115VP9BGs22YfT0fWbRg0nKCrQFF1XP_2oARLGQStqlzcdRqCzSYPpcDLm2hZEXoLlqzKhlwX7q--UA7b9r2nYS-YqJbJjJmCX69hVXHYx"

    url = "https://api.yelp.com/v3/businesses/search"

    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }

    my_params = {
        "term": "restaurants",
        "location": "chicago",
        "limit": 3,
    }

    businesses_object = requests.get(url, headers=my_headers, params=my_params)

    businesses_dict = businesses_object.text

    print(businesses_dict)

#calling the search_businesses function
search_businesses()
