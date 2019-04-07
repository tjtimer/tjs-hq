"""
run.py
author: Tim "tjtimer" Jedro
created: 07.04.19
"""
from tjs_hq.app import prepare

app = prepare()


if __name__ == '__main__':
    app.run(host=app.config.HOST, port=app.config.PORT, workers=app.config.WORKERS, debug=app.config.DEBUG)
