from server.main.redis_funcs import put_item, item_list, get_item
from flask import render_template, Blueprint, request, redirect

main_blueprint = Blueprint("main", __name__, template_folder='templates')


# endpoint for monitoring all job status
@main_blueprint.route("/", methods=["GET"])
def home():
    lst = item_list()
    return render_template('index.html', sell_flag=0, purchase_flag=0, items=lst)


# endpoint for adding job
@main_blueprint.route("/add_item", methods=["GET"])
def add_new_item():
    lst = item_list()
    return render_template('index.html', sell_flag=1, purchase_flag=0, items=lst)


# endpoint for adding job
@main_blueprint.route("/add_wait_job", methods=["POST", "GET"])
def add_wait_job():
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


# endpoint for deleting a job
@main_blueprint.route('/purchase/<item_id>', methods=["GET"])
def purchase_item(item_id):
    # get job from connected redis queue
    l = get_item(item_id)
    # redirect to job list page
    return render_template('index.html', sell_flag=0, purchase_flag=1, items=l)
