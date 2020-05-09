from bottle import run, route

@route('/')
def index():
    return '<h1>Hello, World!'

if __name__ == "__main__":
    run()