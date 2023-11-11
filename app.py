from flask import Flask, flash, render_template, redirect, url_for, request, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'StRoNgRaNdOmolanokhi42'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, user_id, name, password, rating):
        self.id = user_id
        self.name = name
        self.password = password
        self.rating = int(rating)

users = {
    '1': User('1', 'Tom', '123', '12'),
    '2': User('2', 'Bob', '123', '3'),
    '3': User('3', 'Paul', '123', '42'),
    '4': User('4', 'Jim', '123', '21'),
    '5': User('5', 'Kate', '123', '7'),
    '6': User('6', 'Jessy', '123', '9'),
}
#for user_id, user in users.items():
    #print(user.name, user.rating)

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

@app.route('/')
@app.route('/index.html')
@login_required
def home():
    print("Home route accessed")
    return render_template('index.html')

@app.route('/map')
@login_required
def map():
    print("Map route accessed")
    return render_template('map.html')

@app.route('/ratings')
@login_required
def ratings():
    print("Map route accessed")
    return render_template('ratings.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		for user_id, user in users.items():
			if user.name == form.username.data and user.password == form.password.data:
				login_user(user)
				return redirect(url_for('home'))
				flash('Invalid username or password', 'error')
	return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
