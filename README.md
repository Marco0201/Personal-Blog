# Personal-Blog
A repository that hosts my full-stack personal blog.

## Techs used

HTML, CSS, Bootstrap, Javascript, Python, Django, SQLite, PostgreSQL.

## Installation

``Keep in mind the examples below are Window's commands. Mac and Linux have different commands when doing the installation. This project uses Python 3.8.16 and Django 4.2.1``

Create a virtual environment using [python](https://www.python.org/):

```bash
python -m venv blog
```

Now activate the virtual environment.

```bash
blog/Scripts/activate
```

Now use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.txt file. While the virtual environment is activated.

```bash
pip install -r requirements.txt
```

## Login and Registration authentication

If you installed all the packages from the requirements.txt correctly then you should be able to use login and registration right away.


## Running the Project
``It is important to follow all the steps for running this project. Do not miss a single step!``

To run the project make sure to be in the right directory. You should be in the following directory: ``Personal-Blog\Blog\``

Now you should makemigrations and then migrate.

```python
python manage.py makemigrations

python manage.py migrate
```
Once you migrate you will need to un-comment all the code that was commented out in the forms.py file, inside the myblog folder. You should be in the following directory:
``Personal-Blog\Blog\myblog\forms.py``

Once you finish un-commenting out the code in the forms.py file , Then finally, you can run the server. Make sure you are back to the following directory: ``Personal-Blog\Blog\``

```python
python manage.py runserver
```

Additionally you can also create a superuser.

```python
#optional
python manage.py createsuperuser
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
