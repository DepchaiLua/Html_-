/project-folder
│
├── app.py          # Server Python
├── templates/
│   ├── index.html  # Trang vượt bước 1
│   ├── key.html    # Trang hiển thị Key
│
└── static/
    └── style.css   # CSS (nếu cần)
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Vượt Bước 1</title>
</head>
<body>
    <h1>Vui lòng vượt qua bước xác minh</h1>
    <p>Click vào nút bên dưới để tiếp tục:</p>
    <form action="/verify" method="post">
        <button type="submit">Xác Minh</button>
    </form>
</body>
</html>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Your Key</title>
</head>
<body>
    <h1>Congratulation!</h1>
    <p>This is your key:</p>
    <strong>{{ ab19728b197f007bakiw2makogayy0saygex0b }}</strong>
</body>
</html>
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Bước 1: Trang chính
@app.route('/')
def index():
    return render_template('index.html')

# Bước 2: Xác minh
@app.route('/verify', methods=['POST'])
def verify():
    # Giả lập xác minh thành công
    return redirect(url_for('get_key'))

# Bước 3: Hiển thị key
@app.route('/key')
def get_key():
    key = "ab19728b197f007bakiw2makogayy0saygex0b-KEY-VIP"
    return render_template('key.html', key=key)

if __name__ == '__main__':
    app.run(debug=True)
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 50px;
}
button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
}
pip install flask
python app.py    
