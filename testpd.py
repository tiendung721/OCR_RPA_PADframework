# pip install paddleocr
# pip install paddlepaddle -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html

from paddleocr import PaddleOCR
import os
import sys
import re

# Đảm bảo stdout in ra được tiếng Việt nếu PAD muốn đọc output
sys.stdout.reconfigure(encoding='utf-8')

# Nhận đường dẫn ảnh từ dòng lệnh
if len(sys.argv) < 2:
    print("loi : khong co anh truyen dan vao.")
    sys.exit(1)

image_path = sys.argv[1]

# Tạo thư mục output nếu chưa có
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, 'output')
os.makedirs(output_dir, exist_ok=True)

# Tạo tên file kết quả .txt
output_txt_filename = os.path.splitext(os.path.basename(image_path))[0] + '_output.txt'
output_txt_path = os.path.join(output_dir, output_txt_filename)

# Khởi tạo OCR
ocr = PaddleOCR(use_angle_cls=True, lang='vi')
result = ocr.ocr(image_path)

# Làm sạch và ghi kết quả OCR
# Làm sạch và ghi kết quả OCR
with open(output_txt_path, 'w', encoding='utf-8') as f:
    for line in result[0]:
        text = line[1][0]
        if text.strip():  # Bỏ dòng rỗng
            f.write(f"{text.strip()}\n")  # KHÔNG thêm (conf: ...)


# ✅ Ghi thêm file log last_output.txt để PAD đọc
last_output_log = os.path.join(script_dir, "last_output.txt")
with open(last_output_log, 'w', encoding='utf-8') as log:
    log.write(output_txt_path)

# In ra màn hình để kiểm tra thủ công nếu cần
print(f"OCR hoan tat: {output_txt_path}")
