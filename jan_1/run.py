from io import BytesIO
from flask import Flask, render_template, send_file, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import prettyplotlib as ppl
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/fig/')
def fig():
    fig, ax = plt.subplots(1)
    ppl.bar(ax, np.arange(10), np.abs(np.random.randn(10)))
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


@app.route('/image/')
def images():
    return render_template("image.html")


if __name__ == '__main__':
    app.run(debug=True)