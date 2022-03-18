#!/usr/bin/python3
""" Flask Server"""
import web_flask
handler = web_flask.app_run(debug=True)

if __name__ == '__main__':
    # Entry point when run via Python interpreter.
    print("== Running in debug mode ==")
    web_flask.app_run().run(host='0.0.0.0', port=5000, debug=True)
else:
    # Entry point when imported as a module.
    print("== Running in production mode ==")
    web_flask.app_run().run(host='0.0.0.0', port=5000, debug=False)

@web_flask.route('/')
def hello_route():
    return 'Hello HBNB!'
