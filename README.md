# 📄 OCR Tự Động bằng PaddleOCR + Power Automate Desktop

## 🧠 Mục tiêu

Hệ thống này giúp **tự động đọc nội dung từ nhiều ảnh chứa thông tin vận chuyển (transport/trailer)** thông qua:
- Script Python sử dụng PaddleOCR để trích xuất văn bản từ ảnh
- Power Automate Desktop (PAD) chạy tự động theo vòng lặp và lấy kết quả

---

## 🗂️ Cấu trúc dự án

.
├── testpd.py # Script chính sử dụng PaddleOCR để đọc ảnh
├── OCRpaddleRPA.txt # Flow RPA chi tiết trong Power Automate Desktop
├── output/
│ ├── <ảnh>_output.txt # Kết quả OCR của từng ảnh
│ └── last_output.txt # Đường dẫn file kết quả gần nhất (để PAD đọc)
├── ocrimg/ # Thư mục chứa ảnh cần OCR (*.jpg, *.png)
└── requirements.txt # (Gợi ý) Danh sách thư viện cần cài


---

## ⚙️ Cấu trúc hoạt động

### 🔹 `testpd.py` – Python OCR Script

1. **Nhận đầu vào**: Đường dẫn ảnh từ dòng lệnh (`sys.argv[1]`)
2. **Chạy OCR** bằng PaddleOCR (`lang='vi'`)
3. **Ghi kết quả**:
   - Dòng văn bản nhận dạng được → file `output/<ảnh>_output.txt`
   - Ghi tên file kết quả vào `last_output.txt` để PAD truy cập

> ✅ Mỗi ảnh sẽ tạo ra 1 file kết quả tương ứng

---

### 🔸 `OCRpaddleRPA.txt` – Flow PAD

Flow thực hiện các bước:
1. **Lặp qua từng ảnh trong thư mục `ocrimg/`**
2. **Gọi `testpd.py` bằng dòng lệnh**, truyền ảnh + số thứ tự
3. **Đọc kết quả từ `last_output.txt`**
4. **Trích xuất thông tin:**
   - Tìm dòng có từ khóa `"Transport Number"` và `"Trailer Number"`
   - Gán giá trị vào các biến `TransportNumber1`, `TrailerNumber1`, ...

---

## ▶️ Hướng dẫn sử dụng

Bước 1: Cài đặt Python & PaddleOCR

```bash
pip install paddleocr
pip install paddlepaddle -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
⚠️ PaddleOCR cần máy hỗ trợ AVX. Nếu lỗi, dùng máy khác hoặc môi trường ảo phù hợp.

Bước 2: Chuẩn bị thư mục ảnh
Tạo thư mục ocrimg/
Thêm ảnh vào đó, ví dụ:
ocrimg/
├── image1.jpg
├── image2.jpg

Bước 3: Cấu hình trong PAD

Tạo biến:
PythonPath: đường dẫn Python (VD: C:\Users\...\python.exe)
ScriptPath: đường dẫn đến testpd.py
Thêm các hành động theo OCRpaddleRPA.txt, gồm:
Folder.GetFiles: lấy danh sách ảnh
RunDOSCommand: gọi Python OCR
ReadTextFromFile: đọc kết quả từ last_output.txt
SplitText: tách dòng
If: lọc đúng dòng "Transport Number" và "Trailer Number"
Gán vào biến: TransportNumber1, TrailerNumber1, ...

📁 Output mẫu
Sau khi chạy:

Mỗi ảnh tạo file: output/image1_output.txt

PAD lưu được:

TransportNumber1 = ...
TrailerNumber1 = ...

✅ Yêu cầu hệ thống

Python 3.8+
PaddleOCR & PaddlePaddle (Windows/Linux)
Power Automate Desktop (PAD) đã bật RPA


