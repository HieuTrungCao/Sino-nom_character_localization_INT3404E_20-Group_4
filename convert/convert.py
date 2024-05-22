import cv2
import os
import shutil
def convert(x1, y1, x2, y2, size_x, size_y):
    x1 /= size_x
    x2 /= size_x
    y1 /= size_y
    y2 /= size_y
    return (x1 + x2) / 2, (y1 + y2) / 2, x2 - x1, y2 - y1
# files = os.listdir("./TKH/pack2/img")
# # print(files)
# for filename in files:
#     img = cv2.imread(f"./TKH/img/{filename}")
#     weight = img.shape[1]
#     height = img.shape[0]
#     # cute .png or .jpg
#     filename = filename[0:len(filename) - 4]
#     old_format = open(f"./TKH/label_char/{filename}.txt", mode = "r", encoding = "utf-8")
#     yolo_format = open(f"./TKH/label_char_yolo/{filename}.txt", mode = "w", encoding = "utf-8")
#     for line in old_format:
#         tmp = line.split()
#         if len(tmp) == 5:
#             x1, y1, x2, y2 = int(tmp[1]), int(tmp[2]), int(tmp[3]), int(tmp[4])
#             x, y, w, h = convert(x1, y1, x2, y2, weight, height)
#         yolo_format.write(f"0 {x} {y} {w} {h}\n")
#     old_format.close()
#     yolo_format.close()
files = os.listdir("./TKH/pack3/img")
for filename in files:
    filename = filename[0:len(filename) - 4]
    shutil.copy(f"./TKH/label_char_yolo/{filename}.txt", f"./TKH/pack3/label/{filename}.txt")



