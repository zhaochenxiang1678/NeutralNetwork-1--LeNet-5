这是一篇LeNet-5的简单复现，其中lenet5.py是神经网络类；run.py是主要逻辑部分；find.py是一个查看保存的模型的文件，运行即可输出模型参数。
需要注意以下两点：
1. 数据集是MNIST手写数字，于是图像是28x28x1的灰色图像，在输入之前需要将其转换为32x32x1。
2. 运行程序之前运行visdom：python -m visdom.server，然后访问http://localhost:8097,可以检查visdom服务器是否运行，并且查看损失曲线图像。
   <img width="2965" height="1658" alt="image" src="https://github.com/user-attachments/assets/4cf72ca9-e386-40ff-a6b4-be64b1ae73a1" />
   <img width="3000" height="1515" alt="image" src="https://github.com/user-attachments/assets/bb3cea2c-47a8-404e-811d-9b5c32c1d2d0" />
