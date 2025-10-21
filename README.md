# Web Mẫu Đơn Giản (Flask)

Dự án mẫu Flask với 1 trang chủ, HTML template và CSS cơ bản.

## Yêu cầu
- Python 3.10+ (khuyến nghị)
- Pip (đi kèm Python)

## Cài đặt
```powershell
# 1) (Tùy chọn) Tạo môi trường ảo
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) Cài dependencies
pip install -r requirements.txt
```

## Chạy ứng dụng
```powershell
# Cách 1: python trực tiếp
python app.py

# Cách 2: sử dụng flask cli
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run --host 0.0.0.0 --port 5000
```

Mở trình duyệt: `http://127.0.0.1:5000`

## Cấu trúc thư mục
```
E:\web_quynh
├─ app.py
├─ requirements.txt
├─ README.md
├─ templates
│  └─ index.html
└─ static
   └─ style.css
```

## Tùy biến
- Chỉnh nội dung ở `templates/index.html`
- Sửa style ở `static/style.css`
- Thêm route mới trong `app.py`
