from flask import Flask, render_template

# from bridge import ()

from decorator import (
    testpizza
)

from Bridge import (
    testShap
)
app = Flask(__name__)

def html(text: str) -> str:
    return text.replace("\n", "<br/>").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")


@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/bridge')
def bridge():
    test1: testShap = testShap()

    return render_template(
        'bridge.html',
        decorator=test1
    )


@app.route('/decorator')
def decorator():
    test: testpizza() = testpizza()

    return render_template(
        'decorator.html',
        decorator=test
    )



