from flask import Flask

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello_world():
    return "<img src=\"/static/images/afro.png\"/> <table><tr><td>ma radio <ul>my artist - my title</ul></td><td>nom d'un radio host<img src=\"/static/images/host.png\"/> infos</td></tr><tr><td>cherche un emploi<div><label>job</label><input name=\"job\"/></div><div><label>lieu</label><input name=\"lieu\"/></div></td><td>mon moyen de transport <ul><li>train</li><li>bus</li></ul></td></tr></table>"
