# python-unsplash

A library that provides a Python interface to [the Unsplash API](https://unsplash.com/documentation).

## Installation

The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:

    pip install python-unsplash

You may also use Git to clone the repository from
Github and install it manually:

    git clone https://github.com/yakupadakli/python-unsplash.git
    cd python-unsplash
    python setup.py install

Python 2.7, 3.4, 3.5 and 3.6, is supported for now.

## Usage

Code is required for authenticated actions

    from unsplash.api import Api
    from unsplash.auth import Auth

    client_id = ""
    client_secret = ""
    redirect_uri = ""
    code = ""

    auth = Auth(client_id, client_secret, redirect_uri, code=code)
    api = Api(auth)

### User

##### User me

###### Require authentication.

Get the user’s profile.

    api.user.me()

##### User update

###### Require authentication.

Update the current user’s profile


| param  | Description |  |
| ------------- | ------------- | ------------- |
| username  | Username  | optional |
| first_name  | First name. | optional |
| last_name  | Last name. | optional |
| email  | Email. | optional |
| url  | Portfolio/personal URL. | optional |
| bio  | About/bio. | optional |
| instagram_username  | First | optional |
| first_name  | First | optional |
| first_name  | Instagram username. | optional |

    kwargs = {"first_name": "Yakup"}

    api.user.update(**kwargs)

##### User get

Retrieve public details on a given user.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| username  | Username  | required |
| w  | Profile image width in pixels.| optional |
| h  | Profile image height in pixels.  | optional |


    api.user.get("yakupa")


##### User portfolio

Retrieve a single user’s portfolio link.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| username  | Username  | required |


    api.user.portfolio("yakupa")


##### User photos

Get a list of photos uploaded by a user.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| username  | Username  | required |
| page  | Page number to retrieve. (default: 1)  | optional |
| per_page  | Number of items per page. (default: 10) | optional |
| order_by  | How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest)  | optional |
| stats  |  Show the stats for each user’s photo. (default: false) | optional |
| resolution  |  The frequency of the stats. (default: “days”) | optional |
| quantity  |  The amount of for each stat. (default: 30) | optional |


    api.user.portfolio("yakupa")


##### User likes

Get a list of photos liked by a user.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| username  | Username  | required |
| page  | Page number to retrieve. (default: 1)  | optional |
| per_page  | Number of items per page. (default: 10) | optional |
| order_by  | How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest)  | optional |

    api.user.likes("yakupa")


##### User collections

Get a list of collections created by the user.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| username  | Username  | required |
| page  | Page number to retrieve. (default: 1)  | optional |
| per_page  | Number of items per page. (default: 10) | optional |

    api.user.collections("yakupa")
