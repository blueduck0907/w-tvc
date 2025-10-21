# PORK UP - Website

Website chính thức của công ty TNHH PORK UP - chuyên sản xuất và kinh doanh thịt heo quay đóng gói ăn liền.

## 🍖 Về Sản Phẩm

**THỊT HEO QUAY ĐÓNG GÓI ĂN LIỀN** với 3 hương vị độc đáo:
- **Vị Truyền Thống**: Hương vị cổ điển, đậm đà
- **Vị Sả Ớt**: Cay nồng, kích thích vị giác  
- **Vị Hương Thảo**: Tinh tế, sang trọng

## 🚀 Tính Năng Website

### ⚡ Performance & Cache
- **Preload Images**: Tự động preload tất cả hình ảnh
- **LocalStorage Cache**: Cache thông minh với expiry 24h
- **Service Worker**: Offline caching cho trải nghiệm mượt mà
- **SPA Navigation**: Chuyển trang không reload

### 🎨 Design & UX
- **Responsive Design**: Tối ưu cho mọi thiết bị
- **Dark Theme**: Giao diện đen chuyên nghiệp với accent vàng
- **Smooth Animations**: Hiệu ứng mượt mà
- **Loading States**: Trạng thái loading thông minh

### 📱 Pages
- **Trang Chủ**: Giới thiệu sản phẩm với STANDEE banner
- **Giới Thiệu**: Chi tiết 3 hương vị sản phẩm
- **Sản Phẩm**: Thông số kỹ thuật và tính năng
- **Liên Hệ**: Thông tin công ty và chứng nhận

## 🛠️ Công Nghệ

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Styling**: Custom CSS với Flexbox/Grid
- **Cache**: Service Worker + LocalStorage
- **Images**: Optimized PNG/JPG với lazy loading

## 📦 Cài Đặt & Chạy

### Yêu Cầu
- Python 3.7+
- Flask
- Modern Browser (Chrome, Firefox, Safari, Edge)

### Cài Đặt
```bash
# Clone repository
git clone https://github.com/blueduck0907/w-tvc.git
cd w-tvc

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
python app.py
```

### Truy Cập
Mở trình duyệt và truy cập: `http://localhost:5000`

## 📁 Cấu Trúc Dự Án

```
w-tvc/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── static/               # Static files
│   ├── style.css         # Main stylesheet
│   ├── sw.js            # Service Worker
│   ├── LOGO.png         # Company logo
│   ├── STANDEE.png      # Main banner
│   ├── banner*.png      # Product banners
│   └── dk_*.jpg         # Certificates
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Homepage
│   ├── gioi_thieu.html  # About page
│   ├── san_pham.html    # Products page
│   └── lien_he.html     # Contact page
└── README.md            # Documentation
```

## 🎯 Tính Năng Nổi Bật

### Cache Management
- **Smart Preloading**: Tự động preload images và pages
- **Cache Validation**: Kiểm tra cache validity
- **Offline Support**: Hoạt động offline với Service Worker

### User Experience
- **Instant Navigation**: Chuyển trang tức thì
- **Loading Feedback**: Trạng thái loading thông minh
- **Mobile Optimized**: Responsive design hoàn hảo

### Performance
- **Fast Loading**: Tối ưu tốc độ tải trang
- **Image Optimization**: Compress và cache hình ảnh
- **Code Splitting**: Chia nhỏ code để tải nhanh

## 📞 Liên Hệ

**Công ty TNHH PORK UP**
- **Địa chỉ**: 175 A6, KP Bình Khởi, Phường Sơn Đông, Tỉnh Vĩnh Long
- **Năm thành lập**: 2025
- **Slogan**: AN TOÀN - TIỆN LỢI

## 📄 License

© 2025 PORK UP. All rights reserved.

---

**Developed with ❤️ for PORK UP**