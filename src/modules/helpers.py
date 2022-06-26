import string


def get_xpath(key) -> string:


    #TODO add the xpaths afterwards
    xpaths = {
        "username_field" : "some xpath",
        "password_field" : "some xpath",
        "login_btn" : "some xpath"
    }

    return xpaths[key]
  


def construct_list_xpath(outer, inner) -> string:

    xpath = f"/html/body/div[{outer}]/ul/li[{inner}]/a"
    return xpath



def get_url(key) -> string:

    urls = {
        "login" : "https://something_goes_here"
    }

    return urls[key]
