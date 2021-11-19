from server.main.redis_funcs import put_item, item_list, get_item
from flask import render_template, Blueprint, request, redirect

main_blueprint = Blueprint("main", __name__, template_folder='templates')


# endpoint for store main page
@main_blueprint.route("/", methods=["GET"])
def home():
    """
    Renders Store main page
    Page with all Items on the platform and 'Add new Item' option
    :return: rendered page
    """

    lst = item_list()
    return render_template('index.html', sell_flag=0, items=lst)


# endpoint for adding item info
@main_blueprint.route("/add_item", methods=["GET"])
def add_new_item():
    """
    Opens form for new Item on Store main page
    Page with all Items on the platform and new Item form
    :return: rendered page
    """

    lst = item_list()
    return render_template('index.html', sell_flag=1, items=lst)


# endpoint for putting item for sale
@main_blueprint.route("/put_on_sale", methods=["POST", "GET"])
def put_on_sale():
    """
    Puts new Item into reddis database
    :return: redirect to Store main page
    """

    item = {
        "status": 'for_sale',
        "category": request.form['item-type'],
        "name": request.form['item-name'],
        "price": request.form['item-price'],
        "description": request.form['item-description'],
        "mail": request.form['seller-email']
    }

    put_item(item)

    return redirect('/')


# endpoint for contacting item seller
@main_blueprint.route('/purchase/<item_id>', methods=["GET"])
def purchase_item(item_id):
    """
    Renders Item page
    Page with informaiton about selected Item
    :return: rendered Item page
    """

    item = get_item(item_id)

    return render_template('item_page.html', item=item)
