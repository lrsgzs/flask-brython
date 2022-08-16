"""
    Flask-Brython
    ~~~~~~~~~~~~~~~~~
    :copyright: (c) 2022 by lrsgzs.
"""

from flask import *

class Brython(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["brython"] = self
        app.jinja_env.globals["brython"] = self
        bybp = Blueprint('brython', __name__, static_folder="static", static_url_path="/ace" + app.static_url_path)
        app.register_blueprint(bybp)

    @staticmethod
    def load():
        """Load brython.js。 | 加载brython.js。"""
        jzs = [
            "brython.min.js",
            "brython_stdlib.min.js"
        ]
        tp = ('<script src="', '"></script>')
        jzjbs = []
        for i in jzs:
            jzjbs.append(tp[0] + url_for("brython.static", filename="js/" + i) + tp[1])
        wq = ""
        for i in jzjbs:
            wq = wq + i + "\n"
        return Markup(wq)

    @staticmethod
    def create(code="print('helloworld')"):
        """Create brython.js Runner. | 创建brython.js代码运行器。

        :param: code: init code | 初始代码
        :return: use 'brython.js Runner' code | 用'brython.js代码运行器'的代码
        """
        a = '<script type="text/python">\n' + code + '\n</script>\n<button onclick="brython()">运行Run</button>'
        return Markup(a)