# Packages
from flask import render_template
import talisker.requests

# Local
from canonicalwebteam.flask_base.app import FlaskBase
from canonicalwebteam.discourse_docs import (
    DiscourseAPI,
    DiscourseDocs,
    DocParser,
)

app = FlaskBase(
    __name__,
    "multipass.run",
    template_folder="../templates",
    static_folder="../static",
    template_404="404.html",
    template_500="500.html",
)


@app.route("/")
def index():
    return render_template("index.html")


url_prefix = "/docs"
server_docs_parser = DocParser(
    api=DiscourseAPI(
        base_url="https://discourse.ubuntu.com/",
        session=talisker.requests.get_session(),
    ),
    category_id=24,
    index_topic_id=8294,
    url_prefix=url_prefix,
)
server_docs = DiscourseDocs(
    parser=server_docs_parser,
    document_template="/docs/document.html",
    url_prefix=url_prefix,
)

server_docs.init_app(app)
