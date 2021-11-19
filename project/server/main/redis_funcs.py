import json
import redis
from server import config
from threading import Lock

# get redis connection and add 'size' to generate item keys
redis_connection = redis.from_url(config.Config.REDIS_URL)
if 'size' not in redis_connection.scan_iter("*"):
    redis_connection.set('size', '0')

lock = Lock()


# add new item to redis
def put_item(item):
    """
    Adds new Item to reddis database
    :param item: dict containing Item params
    """

    lock.acquire()

    db_size = redis_connection.get('size').decode('utf-8')
    redis_connection.set('size', int(db_size) + 1)

    lock.release()

    item["id"] = 'item' + db_size

    redis_connection.set(item["id"], json.dumps(item))


# get list of items for html
def item_list():
    """
    Collects information about all Items stored in reddis database
    :return: list of Items
    """

    itemlist = []
    for key in redis_connection.scan_iter("item*"):
        item = redis_connection.get(key)

        itemlist.append(json.loads(item))

    return itemlist


# get specific item to contact seller
def get_item(item_id):
    """
    Collects information about specified Item
    Parameter 'mail_link' added for item_page.html
    :param item_id: Item key in reddis database
    :return: dict containing Item params
    """

    item = json.loads(redis_connection.get(item_id))
    item["mail_link"] = 'mailto:' + item["mail"]

    return item
