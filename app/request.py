import urllib.request, json


def configure_request(app):
    global quotes_url
    
    quotes_url = app.config["QUOTES_URL"]
    


def get_quotes():
    """
    Function that gets the json response to our url request
    """
    get_quotes_url = quotes_url

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response["quotes"]:
            quotes_results_list = get_quotes_response["quotes"]
            quotes_results = process_quotes(quotes_results_list)

    return 