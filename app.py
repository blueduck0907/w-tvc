from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", title="Trang chủ", message="Thịt heo đóng gói ăn nhanh – tiện lợi, an toàn, thơm ngon.")


@app.route("/gioi-thieu")
def gioi_thieu():
    return render_template("gioi_thieu.html", title="Giới thiệu")


@app.route("/san-pham")
def san_pham():
    return render_template("san_pham.html", title="Sản phẩm")


@app.route("/lien-he")
def lien_he():
    return render_template("lien_he.html", title="Liên hệ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
