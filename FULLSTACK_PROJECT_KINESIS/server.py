from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)


app.secret_key = 'your_secret_key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Reboot@1234'
app.config['MYSQL_DB'] = 'Project'


mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']  

       
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO Signup (Name, UserName, Email, Password) VALUES (%s, %s, %s, %s)', 
                       (name, username, email, password))
        mysql.connection.commit()
        cursor.close()

        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('loginreal.html')
@app.route("/loginreal", methods=['GET', 'POST'])
def loginreal():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check credentials
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM Signup WHERE UserName = %s', [username])
        user = cursor.fetchone()
        cursor.close()
        if username and user[4] == password:  
            session['username'] = username
            return redirect('/original')
        else:
            return render_template('loginreal.html', message='Invalid credentials')

    return render_template('loginreal.html')



@app.route('/original')
def original():
    if 'username' not in session:
        return redirect('/login')
    return render_template('original.html', username=session['username'])

@app.route('/cricket', methods=['GET', 'POST'])
def cricket():
    if request.method == 'POST':
      
        player_name = request.form['player_name']
        player_age = request.form['player_age']
        player_location = request.form['player_location']
        player_role = request.form['player_role']
        batting_style = request.form['batting_style']
        bowling_style = request.form['bowling_style']
        experience = request.form['experience']
        player_contact_number=request.form['player_contact_number']

        try:
           
            if not player_name or not player_age or not player_location or not player_role or not batting_style or not bowling_style or not experience or not player_contact_number:
                return "All fields are required!"
            
            
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO cricket (`Player Name`, `Age`, `Location`, `Role`, `Batting Style`, `Bowling Style`, `Experience Level`,`Contact Number`) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
                           (player_name, player_age, player_location, player_role, batting_style, bowling_style, experience, player_contact_number))
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", e)
            return f"Failed to add player profile: {str(e)}. Please check your database setup."

        return redirect('/filter_cricket')
    
    return render_template('cricket.html')

@app.route('/filter_cricket', methods=['GET', 'POST'])
def filter_cricket():
    players = []
    if request.method == 'POST':
        location = request.form.get('location')

        try:
           
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM cricket WHERE Location = %s', [location])
            players = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print("Error:", e)
            return "Failed to fetch profiles. Please check your database setup."

    return render_template('filter_cricket.html', players=players)



@app.route('/basketball', methods=['GET', 'POST'])
def basketball():
    if request.method == 'POST':
        # Collect form data
        player_name = request.form['player_name']
        player_age = request.form['player_age']
        player_location = request.form['player_location']
        player_height = request.form['player_height']
        player_position = request.form['player_position']
        dominant_hand = request.form['dominant_hand']
        experience = request.form['experience']
        player_contact_number = request.form['player_contact_number']

        try:
            
            if not player_name or not player_age or not player_location or not player_height or not player_position or not dominant_hand or not experience or not player_contact_number:
                return "All fields are required!"
            
            
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO basketball (`Player Name`, `Age`, `Location`, `Height`, `Position`, `Dominant Hand` ,`Experience`, `Contact Number`) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
                           (player_name, player_age, player_location, player_height, player_position, dominant_hand, experience, player_contact_number))
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", e)
            return f"Failed to add player profile: {str(e)}. Please check your database setup."
        return redirect('/filter_basketball')
    return render_template('basketball.html')

@app.route('/filter_basketball', methods=['GET', 'POST'])
def filter_basketball():
    players = []
    if request.method == 'POST':
        location = request.form.get('location')

        try:
            
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM basketball WHERE Location = %s', [location])
            players = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print("Error:", e)
            return "Failed to fetch profiles. Please check your database setup."

    return render_template('filter_basketball.html', players=players)


@app.route('/volleyball', methods=['GET', 'POST'])
def volleyball():
    if request.method == 'POST':
       
        player_name = request.form['player_name']
        player_age = request.form['player_age']
        player_location = request.form['player_location']
        player_position = request.form['player_position']
        player_height = request.form['player_height']
        experience_level = request.form['experience_level']
        player_contact_number = request.form['player_contact_number']

        try:
            
            if not player_name or not player_age or not player_location or not player_height or not player_position or not experience_level or not player_contact_number:
                return "All fields are required!"
            
            
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO volleyball (`Player Name`, `Age`, `Location`, `Height`, `Position`, `Experience Level`, `Contact Number`) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                           (player_name, player_age, player_location, player_height, player_position, experience_level, player_contact_number))
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", e)
            return f"Failed to add player profile: {str(e)}. Please check your database setup."
        return redirect('/filter_volleyball')
    return render_template('volleyball.html')

@app.route('/filter_volleyball', methods=['GET', 'POST'])
def filter_volleyball():
    players = []
    if request.method == 'POST':
        location = request.form.get('location')

        try:
           
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM volleyball WHERE Location = %s', [location])
            players = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print("Error:", e)
            return "Failed to fetch profiles. Please check your database setup."

    return render_template('filter_volleyball.html', players=players)

@app.route('/football', methods=['GET', 'POST'])
def football():
    if request.method == 'POST':
       
        player_name = request.form['player_name']
        player_age = request.form['player_age']
        player_location = request.form['player_location']
        player_position = request.form['player_position']
        preffered_foot = request.form['preffered_foot']
        playing_style=request.form['playing_style']
        experience = request.form['experience']
        player_contact_number = request.form['player_contact_number']

        try:
            if not player_name or not player_age or not player_location or not preffered_foot or not player_position or not experience or not player_contact_number:
                return "All fields are required!"
            
            
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO football (`Player Name`, `Age`, `Location`, `Position`, `Preffered Foot` , `Playing Style`, `Experience Level`, `Contact Number`) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s ,%s)''',
                           (player_name, player_age, player_location, player_position, preffered_foot, playing_style, experience, player_contact_number))
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", e)
            return f"Failed to add player profile: {str(e)}. Please check your database setup."
        return redirect('/filter_football')
    return render_template('football.html')

@app.route('/filter_football', methods=['GET', 'POST'])
def filter_football():
    players = []
    if request.method == 'POST':
        location = request.form.get('location')

        try:
            
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM football WHERE Location = %s', [location])
            players = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print("Error:", e)
            return "Failed to fetch profiles. Please check your database setup."

    return render_template('filter_football.html', players=players)

@app.route('/hockey', methods=['GET', 'POST'])
def hockey():
    if request.method == 'POST':
        
        player_name = request.form['player_name']
        player_age = request.form['player_age']
        player_location = request.form['player_location']
        player_height = request.form['player_height']
        player_position = request.form['player_position']
        experience_level = request.form['experience_level']
        player_contact_number = request.form['player_contact_number']

        try:
           
            if not player_name or not player_age or not player_location or not player_height or not player_position or not experience_level or not player_contact_number:
                return "All fields are required!"
            
            
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO hockey (`Player Name`, `Age`, `Location`,  `Height`, `Position`, `Experience Level`, `Contact Number`) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                           (player_name, player_age, player_location, player_height, player_position, experience_level, player_contact_number))
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", e)
            return f"Failed to add player profile: {str(e)}. Please check your database setup."
        return redirect('/filter_hockey')
    return render_template('hockey.html')

@app.route('/filter_hockey', methods=['GET', 'POST'])
def filter_hockey():
    players = []
    if request.method == 'POST':
        location = request.form.get('location')

        try:
           
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM hockey WHERE Location = %s', [location])
            players = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print("Error:", e)
            return "Failed to fetch profiles. Please check your database setup."

    return render_template('filter_hockey.html', players=players)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(delattr)


