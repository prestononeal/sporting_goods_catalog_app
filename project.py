# The main program for the Item Catalog Web App
from flask import Flask
app = Flask(__name__)


@app.route('/login/')
def login():
    return 'The login screen for the app'


@app.route('/logout/')
def logout():
    return 'The logout screen for the app'


@app.route('/')
@app.route('/catalog/')
def catalog_main():
    return 'The main catalog page'


@app.route('/catalog/category/<int:category_id>/')
def category_main(category_id):
    return 'Show all the items in a specific category: {}'.format(category_id)


@app.route('/catalog/category/add/')
def category_add():
    return 'Add a new category'


@app.route('/catalog/category/<int:category_id>/edit/')
def category_edit(category_id):
    return 'Editing category {}'.format(category_id)


@app.route('/catalog/category/<int:category_id>/delete/')
def category_delete(category_id):
    return 'Deleting category {}'.format(category_id)


@app.route('/catalog/category/<int:category_id/item/<int:item_id>/')
def item_main(category_id, item_id):
    return 'Showing description of item {}'.format(item_id)


@app.route('/catalog/category/<int:category_id/item/add/')
def item_add(category_id):
    return 'Add a new item'


@app.route('/catalog/category/<int:category_id/item/<int:item_id>/edit/')
def item_edit(category_id, item_id):
    return 'Editing item {}'.format(item_id)


@app.route('/catalog/category/<int:category_id/item/<int:item_id>/delete/')
def item_delete(category_id, item_id):
    return 'Deleting item {}'.format(item_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
