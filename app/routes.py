from flask import Blueprint, render_template, request

from app.models import get_completion_from_groq



# Create a Blueprint object
main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/about")
def about():
    print("About page accessed")
    return render_template("about.html")



@main.route('/submit_message', methods=['POST'])
def submit_message():
    print("submit_message route accessed")
    message = request.form.get('message')  # get the message from the form
    # print("Message:", message)
    response = get_completion_from_groq(message)
    print(response)
    return response


