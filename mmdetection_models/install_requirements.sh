pip3 install openmim
mim install mmengine
mim install "mmcv>=2.0.0"
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -e .
sed -i -e 's/2.2.0/2.2.1/g' ./mmdet/__init__.py