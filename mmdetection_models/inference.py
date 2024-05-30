from pathlib import Path
import glob
import os
import cv2
import numpy as np
import argparse
from mmdet.apis import DetInferencer

def contrast_stretching(img):
  min_val = np.min(img)
  max_val = np.max(img)

  LUT = np.zeros(256, dtype = np.uint8)
  for i in range(256):
    LUT[i] = ((i - min_val) / (max_val - min_val)) * 255

  stretched_img = cv2.LUT(img, LUT)

  return stretched_img

def convert_images_to_grayscale(input_folder, output_folder):
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  for file in os.listdir(input_folder):
    if file.endswith(".jpg"):
      img = cv2.imread(os.path.join(input_folder, file))
      if img is not None:
        grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        stretched_img = contrast_stretching(grayscale_img)
        cv2.imwrite(os.path.join(output_folder, file), stretched_img)

def inference(inferencer, input_path, output_dir):
    # output_dir = './val_predictions'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    # input_path = 'wb_localization_dataset_coco/images/val'
    files = glob.glob(f"{input_path}/*.jpg")
    result = inferencer(input_path)
    print(len(result['predictions']))
    print(len(files))
    for file, res in zip(files, result['predictions']):
        im = cv2.imread(file)
        h, w = im.shape[0], im.shape[1]
        pred_boxes = np.array(res['bboxes'])
        scores = np.array(res['scores'])
        classes = np.array(res['labels'])
        pred_boxes[:, 2] -= pred_boxes[:, 0]
        pred_boxes[:, 3] -= pred_boxes[:, 1]
        pred_boxes[:, 0] += pred_boxes[:, 2] / 2
        pred_boxes[:, 1] += pred_boxes[:, 3] / 2
        pred_boxes[:, 0] /= w
        pred_boxes[:, 2] /= w
        pred_boxes[:, 1] /= h
        pred_boxes[:, 3] /= h
        final = np.concatenate([classes[:, None], pred_boxes, scores[:, None]], axis=1)
        np.savetxt(os.path.join(output_dir, Path(file).stem + ".txt"), final, fmt=['%d', '%f', '%f', '%f', '%f', '%f'])
        print(file)
        
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--model', default='best.pth', help='Input your model model.')
  parser.add_argument('--config', default='config.py', help='MMDetection model config')
  parser.add_argument('--input-dir', default='./test/images', help='Path to input image.')
  parser.add_argument('--output-dir', default='./result', help='Directory to save result')
  args = parser.parse_args()
  # Preprocessing: Convert images to grayscale
  convert_images_to_grayscale(args.input_dir, './input_inference')
  inferencer = DetInferencer(model=args.config, weights=args.model)
  inference(inferencer, './input_inference', args.output_dir)