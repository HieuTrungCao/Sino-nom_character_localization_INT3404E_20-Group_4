pip3 install openmim
mim install mmengine
pip install mmcv==2.2.0 -f https://download.openmmlab.com/mmcv/dist/cu121/torch2.3/index.html
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -e .
sed -i -e 's/2.2.0/2.2.1/g' ./mmdet/__init__.py