# sporting_goods_catalog_app

A web application that provides a list of items within a variety of categories.
A user registration and authentication system is provided through Google OAuth 2.0 authentication so that users can post, edit, and delete their own items.

The HTML/CSS layout was borrowed heavily from [https://css-tricks.com/super-simple-two-column-layout/](https://css-tricks.com/super-simple-two-column-layout/)

Required: This app must be run in a Vagrant-configured VirtualBox VM. The Vagrant settings were applied from this project: [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)

To run this project:

1. Navigate to the root folder containing [project.py](project.py)
2. Run `python database_setup.py` to set up the database
3. Run `python database_populate.py` to populate the database with some initial data
4. Run `python project.py` to run the web app. Naviate to [http://localhost:8000](http://localhost:8000) in your browser.
5. Create new items. A user can edit and delete their own items.
