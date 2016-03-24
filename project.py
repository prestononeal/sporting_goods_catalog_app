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
          'name': 'Ball', 'description': 'Kick it.'},
         {'id': 2, 'category': {'name': 'Baseball', 'id': 2},
          'name': 'Bat', 'description': 'Hit stuff with it.'},
         {'id': 3, 'category': {'name': 'Volleyball', 'id': 3},
          'name': 'Net', 'description': 'Get a ball over it.'},
         {'id': 4, 'category': {'name': 'Baseball', 'id': 2},
          'name': 'Mitt', 'description': 'Catch stuff with it.'},
         {'id': 5, 'category': {'name': 'Volleyball', 'id': 3},
          'name': 'Shoes', 'description': 'Run with them.'}]


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
    # Get the current category so information can be generated for it
    # in the rendered page
    for cat in categories:  # TODO: change this to db lookup
        if cat.get('id') == category_id:
            category = cat
    category_items = []
    for item in items:
        if item.get('category').get('id') == category_id:
            category_items.append(item)
    return render_template('category.html', category=category,
                           categories=categories, items=category_items)


@app.route('/catalog/item/<int:item_id>/')
def item_main(item_id):
    # Show the item info place
    for item in items:
        if item.get('id') == item_id:
            current_item = item
    return render_template('item.html', categories=categories,
                           item=current_item)


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
