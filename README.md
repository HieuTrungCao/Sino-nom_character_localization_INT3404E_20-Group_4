# Bài tập lớn: Khoanh vùng kí tự Hán Nôm
Lớp: INT3404E 20 - Xử lý ảnh\
Nhóm: 4
## Thông tin các thành viên nhóm
- [Cao Trung Hiếu - 21021490](https://github.com/HieuTrungCao)
- [Đoàn Đức Kiên - 21020207](https://github.com/duckiendoan)
- [Nguyễn Minh Kiên - 21020638](https://github.com/nmk-k66-uet)
- [Bùi Minh Thành - 2102020050](https://github.com/thabumi)
## Mục tiêu
Repository này cung cấp mã nguồn để huấn luyện và chạy các mô hình YOLOv8n và các mô hình trong thư viện MMDetection nhằm giải quyết bài toán khoanh vùng kí tự Hán Nôm.
## Cấu trúc thư mục
```
.
├── Image_Processing_Projects_Full_Report.pdf
├── README.md
├── Run.ipynb                 # Chạy mô hình YOLOv8n trên tập test
├── YOLOv8n_fine_tuning.ipynb # Huấn luyện mô hình YOLOv8n
├── convert
│   └── convert.py            # Chuyển tập dữ liệu sang định dạng YOLO
├── datasets
│   └── orginal_preprocess_augment.rar # Tập dữ liệu được tăng cường
├── mmdetection_models        # Huấn luyện mô hình trong thư viện MMDetection
│   ├── centripetalnet.ipynb
│   ├── deformable_detr.ipynb
│   ├── inference.py # Chạy mô hình trên tập test
│   ├── install_requirements.sh
│   ├── sabl_training.ipynb
│   └── tood.ipynb # Huấn luyện mô hình TOOD
├── nom_v8.yaml # Config huấn luyện YOLOv8n
└── nom_v8_test.yaml # Config test YOLOv8n
```
## Hướng dẫn chạy
- Tải tập dữ liệu của nhóm tại [đây](https://drive.google.com/drive/folders/1pzujLSmMjvtfSpkZuJkRt49er0YXEFQx?usp=sharing).
- Mã nguồn trong repository đều ở dạng Jupyter Notebook. Vì vậy, cách tốt nhất là upload notebook lên [Google Colab](https://colab.research.google.com) và chạy lần lượt từng cell.
- Để chạy `mmdetection_models/inference.py`, đầu tiên chạy file `mmdetection_models/install_requirements.sh` để cài đặt `mmdetection`. Sau đó chạy file `inference.py` với cú pháp 
    ```
    python inference.py \
    --input-dir [thư mục chứa ảnh] \
    --model [đường dẫn đến mô hình đã được lưu] \
    --config [đường dẫn đến config của mô hình] \
    --output-dir [thư mục lưu kết quả]
    ```
## Kết quả
Các mô hình được đánh giá trên tập validation của thầy Thương. Kết quả mAP được tính bằng code thầy Thương cung cấp. 
### Kết quả mô hình YOLOv8n
| Mô hình                                                              | mAP@[.5:.95] |
| -------------------------------------------------------------------- | ------------ |
| Baseline                                                             | 0.771        |
| YOLOv8n (Tiền xử lí & Tăng cường)                                    | **0.872**    |
| YOLOv8n sử dụng bộ dữ liệu bổ sung (Base)                            | 0.863        |
| YOLOv8n sử dụng bộ dữ liệu bổ sung (Tiền xử lí dữ liệu)              | 0.863        |
| YOLOv8n sử dụng bộ dữ liệu bổ sung (Tiền xử lí & Tăng cường dữ liệu) | 0.821        |


### Kết quả các mô hình trong thư viện MMDetection
| Mô hình         | mAP@[.5:.95] |
| --------------- | ------------ |
| SABL RetinaNet  | 0.841        |
| TOOD R50        | 0.842        |
| CentripetalNet  | **0.873**    |
| Deformable DETR | 0.669        |

## Báo cáo
Báo cáo đầy đủ của nhóm có thể xem tại [đây](Image_Processing_Projects_Full_Report.pdf).