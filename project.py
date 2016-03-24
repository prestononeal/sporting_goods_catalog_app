'''
The main program for the Item Catalog Web App
'''
from flask import Flask, render_template, url_for
app = Flask(__name__)


# Temporary database items. TODO: remove
categories = [{'name': 'Soccer', 'id': 1},
              {'name': 'Baseball', 'id': 2},
              {'name': 'Volleyball', 'id': 3}]


items = [{'id': 1, 'category': {'name': 'Soccer', 'id': 1},
          'item': 'Ball'},
         {'id': 2, 'category': {'name': 'Baseball', 'id': 2},
          'item': 'Bat'},
         {'id': 3, 'category': {'name': 'Volleyball', 'id': 3},
          'item': 'Net'},
         {'id': 4, 'category': {'name': 'Baseball', 'id': 2},
          'item': 'Mitt'},
         {'id': 5, 'category': {'name': 'Volleyball', 'id': 3},
          'item': 'Shoes'}]


@app.route('/login/')
def login():
    return 'The login screen for the app'


@app.route('/logout/')
def logout():
    return 'The logout screen for the app'


@app.route('/')
@app.route('/catalog/')
def catalog_main():
    # Get the three latest items
    newest_items = items[-3:]
    return render_template('catalog.html', categories=categories,
                           items=newest_items)


@app.route('/catalog/category/<int:category_id>/')
def category_main(category_id):
    return 'Show all the items in a specific category: {}'.format(category_id)


@app.route('/catalog/item/<int:item_id>/')
def item_main(item_id):
    return 'Showing description of item {}'.format(item_id)


@app.route('/catalog/item/add/')
def item_add():
    return 'Add a new item'


@app.route('/catalog/item/<int:item_id>/edit/')
def item_edit(item_id):
    return 'Editing item {}'.format(item_id)


@app.route('/catalog/item/<int:item_id>/delete/')
def item_delete(item_id):
    return 'Deleting item {}'.format(item_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
