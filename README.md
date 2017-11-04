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


### Photo

##### Photo all

Get a single page from the list of all photos.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| page  | Page number to retrieve. (default: 1)  | optional |
| per_page  | Number of items per page. (default: 10) | optional |
| order_by  | How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest) | optional |


    api.photo.all()


##### Photo curated

Get a single page from the list of the curated photos.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| page  | Page number to retrieve. (default: 1)  | optional |
| per_page  | Number of items per page. (default: 10) | optional |
| order_by  | How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest) | optional |


    api.photo.curated()


##### Photo get

Get a single page from the list of the curated photos.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The photo’s ID.  | required |
| w  | Image width in pixels. | optional |
| h  | Image height in pixels. | optional |
| rect  | 4 comma-separated integers representing x, y, width, height of the cropped rectangle. | optional |


    api.photo.get("Dwu85P9SOIk")


##### Photo random

Retrieve a single random photo, given optional filters.

Note: You can’t use the collections and query parameters in the same request

Note: When supplying a count parameter - and only then - 
the response will be an array of photos, even if the value of count is 1.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| collections  | Public collection ID(‘s) to filter selection. If multiple, comma-separated | optional |
| featured  | Limit selection to featured photos. | optional |
| username  | Limit selection to a single user. | optional |
| query  | Limit selection to photos matching a search term. | optional |
| w  | Image width in pixels. | optional |
| h  | Image height in pixels. | optional |
| orientation  | Filter search results by photo orientation. Valid values are landscape, portrait, and squarish. | optional |
| count  | The number of photos to return. (Default: 1; max: 30) | optional |


    api.photo.random()


##### Photo stats

Retrieve total number of downloads, views and likes of a single photo, 
as well as the historical breakdown of these stats in a specific timeframe (default is 30 days).

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The public id of the photo. | required |
| resolution  | The frequency of the stats. | optional |
| quantity  | The amount of for each stat. | optional |


    api.photo.stats("LF8gK8-HGSg")


##### Photo like

Like a photo on behalf of the logged-in user. This requires the write_likes scope.

Note: This action is idempotent; sending the POST request to a single photo multiple times has no additional effect.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The photo’s ID. | required |


    api.photo.like("LF8gK8-HGSg")


##### Photo unlike

Remove a user’s like of a photo.

Note: This action is idempotent; sending the DELETE request to a single photo multiple times has no additional effect.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The photo’s ID. | required |


    api.photo.unlike("LF8gK8-HGSg")


### Search

##### Search photos

Get a single page of photo results for a query.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| query  | Search terms. | required |
| page  | Page number to retrieve. | optional |
| per_page  | Number of items per page. | optional |
| collections  | Collection ID(‘s) to narrow search. If multiple, comma-separated. | optional |


    api.search.photos("office")


##### Search collections

Get a single page of collection results for a query.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| query  | Search terms. | required |
| page  | Page number to retrieve. | optional |
| per_page  | Number of items per page. | optional |


    api.search.collections("office")


##### Search users

Get a single page of user results for a query.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| query  | Search terms. | required |
| page  | Page number to retrieve. | optional |
| per_page  | Number of items per page. | optional |


    api.search.users("yakupa")


### Collections

##### Collections all

Get a single page from the list of all collections.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| page  | Page number to retrieve. | optional |
| per_page  | Number of items per page. | optional |


    api.collection.all()


##### Collections featured

Get a single page from the list of featured collections.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| page  | Page number to retrieve. | optional |
| per_page  | Number of items per page. | optional |


    api.collection.featured()


##### Collections curated

Get a single page from the list of curated collections.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| page  | Page number to retrieve. | optional |
| per_page  | Number of items per page. | optional |


    api.collection.curated()


##### Collections get

Retrieve a single collection. 
To view a user’s private collections, the read_collections scope is required.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The collections’s ID. | required |


    api.collection.get("547584")


##### Collections get curated

Retrieve a single curated collection. 
To view a user’s private collections, the read_collections scope is required.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The curated collections’s ID. | required |


    api.collection.get_curated("547584")


##### Collections photos

Retrieve a collection’s photos.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The collections’s ID. | required |
| page  | Page number to retrieve. | optional |
| per_page  | Number of items per page. | optional |


    api.collection.photos("547584")


##### Collections curated photos

Retrieve a curated collection’s photos.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The curated collections’s ID. | required |
| page  | Page number to retrieve. | optional |
| per_page  | Number of items per page. | optional |


    api.collection.curated_photos("547584")


##### Collections related

Retrieve a list of collections related to this one.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The collection’s ID. | required |


    api.collection.related("547584")


##### Collections create

Create a new collection. 
This requires the write_collections scope.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| title  | The title of the collection. | required |
| description  | The collection’s description. | optional |
| private  | Whether to make this collection private. | optional |


    api.collection.create("New Test Collection")


##### Collections update

Update an existing collection belonging to the logged-in user. 
This requires the write_collections scope.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The collection’s ID. | required |
| title  | The title of the collection. | optional |
| description  | The collection’s description. | optional |
| private  | Whether to make this collection private. | optional |


    api.collection.update("547584")


##### Collections delete

Delete a collection belonging to the logged-in user.
This requires the write_collections scope.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| id  | The collection’s ID. | required |


    api.collection.delete("547584")


##### Collections add photo

Add a photo to one of the logged-in user’s collections.
Requires the write_collections scope.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| collection_id  | The collection’s ID. | required |
| photo_id  | The photo’s ID. | required |


    api.collection.add_photo("547584", "KSap1iDftvQ")


##### Collections remove photo

Remove a photo from one of the logged-in user’s collections.
Requires the write_collections scope.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| collection_id  | The collection’s ID. | required |
| photo_id  | The photo’s ID. | required |


    api.collection.remove_photo("547584", "KSap1iDftvQ")


### Stats

##### Stats total

Get a list of counts for all of Unsplash.


    api.stat.total()


##### Stats total

Get the overall Unsplash stats for the past 30 days.


    api.stat.month()
