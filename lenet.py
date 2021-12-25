import torchvision.datasets as datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

import torch
import torch.optim as optim
import torch.nn as nn

from utils import test_accuracy

from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter()


# from pytorch docs
train = datasets.FashionMNIST(
    root="data",
    train=True,
    download=False,
    transform=ToTensor()
)

test = datasets.FashionMNIST(
    root="data",
    train=False,
    download=False,
    transform=ToTensor()
)

print(len(train))
print(len(test))


class LeNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.CNN = nn.Sequential(
            nn.Conv2d(1, 6, 5, padding=2),
            nn.Sigmoid(),
            nn.AvgPool2d(2, 2),
            nn.Conv2d(6, 16, 5),
            nn.Sigmoid(),
            nn.AvgPool2d(2, 2),

        )
        self.fc = nn.Sequential(
            nn.Linear(16*5*5, 120),
            nn.Sigmoid(),
            nn.Linear(120, 84),
            nn.Sigmoid(),
            nn.Linear(84, 10)
        )

    def forward(self, x):
        batch_size = x.shape[0]
        CNN_out = self.CNN(x)
        flat = CNN_out.view(batch_size, 16*5*5)
        fc_out = self.fc(flat)
        return fc_out


EPOCHS = 20
BATCH_SIZE = 32
loss_func = torch.nn.CrossEntropyLoss()
net = LeNet()
optimizer = optim.Adam(net.parameters(), lr=1e-3)

dataloader = DataLoader(train, batch_size=BATCH_SIZE, shuffle=True)

for epoch in range(EPOCHS):
    for batch in dataloader:
        data, labels = batch
        out = net(data)
        loss = loss_func(out, labels)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        writer.add_scalar("loss", loss)
        writer.add_scalar("acc", test_accuracy(test, net))