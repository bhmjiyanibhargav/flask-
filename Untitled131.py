#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # question 01
Q1. What is Flask Framework? What are the advantages of Flask Framework?
Flask is a micro web framework written in Python that is designed to be simple, lightweight, and easy to use. Flask allows developers to quickly and easily build web applications without the overhead of larger, more complex web frameworks.

Here are some advantages of using Flask:

Lightweight: Flask is a micro framework that only provides the essential features required to build a web application, making it lightweight and fast.

Flexible: Flask is highly flexible and can be customized to fit a wide range of needs and requirements.

Easy to learn: Flask is easy to learn and use, even for beginners, due to its simple and intuitive API.

Modular: Flask is modular, which means that it can be extended and customized using a wide range of third-party extensions and plugins.

Integrated with Python: Flask is written in Python and seamlessly integrates with other Python libraries and tools, making it an ideal choice for Python developers.

Well documented: Flask has comprehensive and well-organized documentation that makes it easy to get started and learn more about the framework.

Overall, Flask is a great choice for building simple, fast, and flexible web applications, especially for small to medium-sized projects that do not require the complexity and overhead of larger web frameworks.
# # question 02
Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in
Jupyter Notebook.

As an AI language model, I don't have access to the local machine to take screenshots. However, I can provide you with the code for a simple Flask application to display "Hello World!!". Here's an example:
# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!!'

if __name__ == '__main__':
    app.run()


# # question 03

# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


# # question 04
Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
route to show the following details:
Company Name: ABC Corporation
Location: India
Contact Detail: 999-999-9999
# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_details():
    return 'Company Name: ABC Corporation\nLocation: India\nContact Detail: 999-999-9999'

if __name__ == '__main__':
    app.run()


# # uestion 05
Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the
url_for() function.
# In[ ]:


from flask import Flask, url_for

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('hello'))


# In[ ]:




