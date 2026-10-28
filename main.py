import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Stock Simulation & Analysis Web App")

# 1. Mount thư mục 'static' để phục vụ file video / gif
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, 'static')

# Tự động tạo thư mục static/video nếu chưa có
os.makedirs(os.path.join(static_dir, 'video'), exist_ok=True)

# Mount đường dẫn /static vào FastAPI
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Mô Phỏng Giao Dịch Cổ Phiếu</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        </head>
        <body class="bg-dark text-white">
            <div class="container py-5 text-center">
                <h1 class="text-warning mb-4">Mô Phỏng Biến Động Giá Cổ Phiếu</h1>

                <!-- Hiển thị Video MP4 -->
                <div class="card bg-secondary p-3 mb-4 shadow">
                    <h4 class="text-light mb-3">1. Video Mô Phỏng (MP4)</h4>
                    <video controls autoplay loop muted width="100%" style="max-width: 800px; class="mx-auto rounded">
                        <source src="/static/video/clt_simulation.mp4" type="video/mp4">
                        Trình duyệt của bạn không hỗ trợ thẻ video HTML5.
                    </video>
                </div>

                <!-- Hoặc Hiển thị Ảnh GIF -->
                <div class="card bg-secondary p-3 mb-4 shadow">
                    <h4 class="text-light mb-3">2. Ảnh Động Mô Phỏng (GIF)</h4>
                    <img src="/static/video/clt_simulation.gif" alt="Stock Simulation" class="img-fluid rounded mx-auto" style="max-width: 800px;">
                </div>

            </div>
        </body>
    </html>
    """