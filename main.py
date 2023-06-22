from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
# import os
# os.system("pip install Flask-SQLAlchemy")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pythonwork'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/books')
def books():
    return render_template('book_cards.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return redirect(url_for('books'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You logged out, come back later!",'info')
    return redirect(url_for('login'))


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)


#html generator
# base_url = "https://books.toscrape.com/catalogue/page-{}.html"
# pages = 50
# books = []
#
# for page in range(1, pages + 1):
#     url = base_url.format(page)
#     response = requests.get(url)
#     content = response.content
#
#
#     soup = BeautifulSoup(content, 'html.parser')
#
#
#     book_cards = soup.find_all('article', class_='product_pod')
#
#
#     for card in book_cards:
#         title = card.h3.a['title']
#         price = card.find('p', class_='price_color').text[2:]
#         stock = card.find('p', class_='instock availability').text.strip()
#         books.append({'title': title, 'price': price, 'stock': stock})
#
# html = '''
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Book Cards</title>
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.2/css/bootstrap.min.css">
#     <style>
#         body {
#             padding-top: 20px;
#         }
#
#         .card {
#             margin-bottom: 20px;
#         }
#     </style>
# </head>
# <body>
#     <div class="container">
#         <h1 class="text-center mb-4">Book Cards</h1>
#
#         <!-- Book cards -->
#         <div class="row row-cols-1 row-cols-md-3 g-4">
# '''
#
# for book in books:
#     html += f'''
#             <div class="col">
#                 <div class="card h-100">
#                     <div class="card-body">
#                         <h5 class="card-title">{book['title']}</h5>
#                         <p class="card-text">Price: {book['price']}</p>
#                         <p class="card-text">Stock: {book['stock']}</p>
#                     </div>
#                 </div>
#             </div>
#     '''
#
# html += '''
#         </div>
#
#     </div>
#
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.2/js/bootstrap.bundle.min.js"></script>
# </body>
# </html>
# '''
#
# # Step 6: Save the generated HTML code to a file or use it on your website as desired
# with open('book_cards.html', 'w') as file:
#     file.write(html)