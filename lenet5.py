import torch.nn as nn

class LeNet5(nn.Module):
    def __init__(self):
        super(LeNet5,self).__init__()

        # 第一层卷积层
        self.c1=nn.Sequential(
            nn.Conv2d(in_channels=1,out_channels=6,kernel_size=5),
            nn.ReLU(),
            nn.AvgPool2d(kernel_size=2,stride=2)
        )

        # 第二层卷积层
        self.c2=nn.Sequential(
            nn.Conv2d(in_channels=6,out_channels=16,kernel_size=5),
            nn.ReLU(),
            nn.AvgPool2d(kernel_size=2,stride=2)
        )

        # 第三层卷积层
        self.c3=nn.Sequential(
            nn.Conv2d(in_channels=16,out_channels=120,kernel_size=5),
            nn.ReLU()
        )

        # 全连接层
        self.classifier=nn.Sequential(
            nn.Linear(in_features=120,out_features=84),
            nn.ReLU(),
            nn.Linear(in_features=84,out_features=10)
        )

    def forward(self,img):
        # 卷积部分
        output=self.c1(img)
        output=self.c2(output)
        output=self.c3(output)

        # 全连接层部分
        output=output.view(img.size(0),-1)
        output=self.classifier(output)

        return output















