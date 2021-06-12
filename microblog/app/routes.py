from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/portfolio.html')
@app.route('/portfolio')
def portfolio():
    user = {'username': 'Matt'}
    projects = [
        {
            'id': '123',
            'title': 'Project 1',
            'description': 'About Project 1'},
        {
            'id': '456',
            'title': 'Project 2',
            'description': 'The greatest program in the world'},
        {
            'id': '789',
            'title': 'Project 3',
            'description': 'Hello World, generated with machine learning and blockchain with microservices'}]
    return render_template('portfolio.html', title='Portfolio', projects=projects, user=user)
