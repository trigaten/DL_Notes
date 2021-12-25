import torch
from torch.utils.data import DataLoader
def test_accuracy(test, net):
    dataloader = DataLoader(test, 32)
    correct = 0
    for data, labels in dataloader:
        out = net(data)
        pred_labels = torch.argmax(out, dim=1)
        correct += torch.eq(labels, pred_labels).sum().detach().item()
    
    return correct / len(test)