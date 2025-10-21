from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route("/")
def home():
    return render_template("index.html", title="Trang chủ", message="Thịt heo đóng gói ăn nhanh – tiện lợi, an toàn, thơm ngon.")


@app.route("/test")
def test():
    return "PORK UP website is working!"


@app.route("/gioi-thieu")
def gioi_thieu():
    return render_template("gioi_thieu.html", title="Giới thiệu")


@app.route("/san-pham")
def san_pham():
    return render_template("san_pham.html", title="Sản phẩm")


@app.route("/lien-he")
def lien_he():
    return render_template("lien_he.html", title="Liên hệ")


@app.route("/health")
def health():
    return {"status": "ok", "message": "PORK UP website is running"}


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


@app.errorhandler(404)
def not_found(error):
    return render_template("index.html", title="Trang chủ"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("index.html", title="Trang chủ"), 500


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

