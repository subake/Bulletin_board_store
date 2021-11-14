import json
import redis
from server import config

# get redis connection
redis_connection = redis.from_url(config.Config.REDIS_URL)
if 'size' not in redis_connection.scan_iter("*"):
    redis_connection.set('size', '0')


# add new item to redis
def put_item(item):
    db_size = redis_connection.get('size').decode('utf-8')
    redis_connection.set('size', int(db_size) + 1)

    item["id"] = 'item' + db_size

    redis_connection.set(item["id"], json.dumps(item))


# get list of items for html
def item_list():
    itemlist = []
    for key in redis_connection.scan_iter("item*"):
        item = redis_connection.get(key)

        itemlist.append(json.loads(item))

    return itemlist


def get_item(item_id):
    item = json.loads(redis_connection.get(item_id))
    item["mail_link"] = 'mailto:' + item["mail"]
    return [item]
