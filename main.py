from flask import Flask, request, render_template, redirect
from crud import *

app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/user', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Access form data
        user = request.form['user']
        password = request.form['pass']
        
        # Process the data (e.g., print it)
        print(f"Received data: user - {user}, password - {password}")
        userstatus = read(user, password)
        if userstatus == True:
            return render_template('usercorrect.html' , user=user)
        elif userstatus == False:
            return render_template('userincorrect.html', user=user)
        else:
            return redirect(location='/error')

# Route to create a user
@app.route('/create')
def createuser():
    return render_template('createuser.html')

@app.route('/create/usercreated', methods=['POST'])
def createuserdone():
    user = request.form['user']
    password = request.form['pass']
    checkuser = userexist(user)
    if checkuser == True:
        # html template change to this message
        return "User already exist."
    else:
        create(user, password)
        return "user created"

# Route to update a user
@app.route('/user/update')
def updateuser():
    return render_template('updateuser.html', user="user")

@app.route('/user/update/userupdated', methods=['POST'])
def updateuserdone():
    olduser = request.form['olduser']
    newuser = request.form['newuser']
    update(olduser, newuser)
    return "user updated"

# Route to delete a user
@app.route('/user/delete')
def deleteuser():
    return render_template('deleteuser.html', user="user")

@app.route('/user/delete/deleteduser', methods=['POST'])
def deleteuserdone():
    deleteuser = request.form['deleteuser']
    # newuser = request.form['newuser']
    delete(deleteuser)
    return "user deleted"

# Route to handle errors
@app.route('/error')
def error():
    return render_template('errordb.html')

if __name__ == '__main__':
    app.run(debug=True)
