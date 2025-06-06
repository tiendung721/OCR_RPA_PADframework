# OCR_RPA_PADframework
📄 OCR PaddleOCR + Power Automate Desktop (PAD)
Dự án này là một hệ thống tự động trích xuất văn bản từ ảnh bằng PaddleOCR, tích hợp cùng Power Automate Desktop (PAD) để xử lý hàng loạt file ảnh, đọc dữ liệu và gán vào biến động.

📦 Cấu trúc dự án
testpd.py
▸ Script Python dùng PaddleOCR để:

Đọc ảnh truyền vào (qua dòng lệnh)

Trích xuất văn bản bằng OCR tiếng Việt

Ghi kết quả ra file output/<ten_file>_output.txt

Ghi lại đường dẫn output gần nhất vào last_output.txt để PAD có thể lấy

OCRpaddleRPA.txt
▸ Flow Power Automate Desktop thực hiện:

Duyệt toàn bộ file ảnh trong thư mục (*.jpg; *.png)

Gọi testpd.py cho từng ảnh

Đọc kết quả OCR từ file output

Tự động trích xuất các thông tin cụ thể như Transport Number, Trailer Number

Gán dữ liệu vào biến OCR1 → OCR5, TransportNumber1 → TrailerNumber1, ...

🧠 Quy trình hoạt động
PAD lấy danh sách các ảnh trong thư mục ocrimg/.

Với mỗi ảnh:

Gọi script testpd.py bằng dòng lệnh.

Script lưu file kết quả vào thư mục output/ và ghi lại đường dẫn vào last_output.txt.

PAD đợi file kết quả xuất hiện, đọc nội dung file và gán vào biến tương ứng.

PAD phân tích dòng có chứa "Transport Number" → lưu vào TransportNumberX, TrailerNumberX tương ứng.

Quá trình lặp lại cho tới hết ảnh.

🛠 Yêu cầu hệ thống
Python 3.x

PaddleOCR

PaddlePaddle

Power Automate Desktop

Cấu hình đúng biến đường dẫn:
#OCR_RPA_PADframework
PythonPath: đường dẫn Python.exe

ScriptPath: đường dẫn tới testpd.py

ocrimg/: thư mục chứa ảnh đầu vào

🚀 Hướng dẫn sử dụng
Cài đặt thư viện:

bash
Sao chép
Chỉnh sửa
pip install paddleocr
pip install paddlepaddle -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
Tạo thư mục ảnh: C:\Users\...\ocrimg

Đặt ảnh cần nhận dạng vào thư mục.

Mở PAD, chạy file OCRpaddleRPA.txt.

Kết quả sẽ được gán vào các biến OCR1, TransportNumber1, ... trong flow.

⚠️ Lưu ý
Script hỗ trợ ảnh tiếng Việt, có xoay góc tự động (use_angle_cls=True).

Mỗi ảnh sẽ sinh ra 1 file kết quả riêng trong output/.

Biến PAD đang xử lý tối đa 5 ảnh và 5 kết quả (OCR1 đến OCR5) – bạn có thể mở rộng dễ dàng.
