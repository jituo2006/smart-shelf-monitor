# YOLOv8 实时物体检测 (Ubuntu)

这是一个基于 **YOLOv8** 和 **OpenCV** 的实时物体检测项目。  
程序使用电脑摄像头进行画面采集，并在检测到指定物体时，绘制边界框并显示中心点坐标。

---

## 环境配置

### 1. 克隆项目
```bash
git clone https://github.com/jituo2006/yolov8-realtime-detection.git
cd yolov8-realtime-detection
```
### 2. 创建虚拟环境（可选）
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. 安装依赖
```bash
pip install -r requirements.txt
```
### 4. 运行程序
```bash
python3 main.py
```
