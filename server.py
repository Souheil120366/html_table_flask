from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.errorhandler(404) 
def handle_error(error):
    res="<script>alert('Sorry! No response. Try again.')</script>"
    return res

@app.route('/')
def render_users():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template("index.html", user_info = users)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
