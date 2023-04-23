import os
import shutil
import subprocess

# 清除之前的打包结果
shutil.rmtree('dist', ignore_errors=True)
shutil.rmtree('build', ignore_errors=True)

# 执行打包命令
subprocess.call(['pyinstaller', 'detect.py', '--name', 'yolov5', '--onefile', '--clean'])

# 将必要的文件复制到 dist 目录中
shutil.copy('yolov5-master2/data/garbage1', 'dist/yolov5-master2/data/garbage1')
shutil.copy('yolov5-master2/models/yolov5s.yaml', 'dist/yolov5-master2/models/yolov5s.yaml')
shutil.copytree('yolov5-master2/models/yolov5s', 'dist/yolov5-master2/models/yolov5s')
