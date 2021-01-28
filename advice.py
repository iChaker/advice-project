from flask import Flask, Response
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Counter
import random
app = Flask(__name__)


good_advice_list = ["Show up fully","Don't try to impress everyone","The simplest solution is often the best"]

bad_advice_list = ["Always be positive","All decisions should be based on logic","Fake it till you make it"]

good_advice_graph = Counter('good_advice_request','total number of good advice served')
bad_advice_graph =  Counter('bad_advice_request','total number of bad advice served')

@app.route('/goodadvice')
def good_advice():
    good_advice_graph.inc()
    return random.choice(good_advice_list)


@app.route('/badadvice')
def bad_advice():
    bad_advice_graph.inc()
    return random.choice(bad_advice_list)

@app.route('/metrics')
def requests_count():
    G_count = prometheus_client.generate_latest(good_advice_graph)
    B_count = prometheus_client.generate_latest(bad_advice_graph)
    return Response([G_count,B_count],mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug = True, use_reloader = True)