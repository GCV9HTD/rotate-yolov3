giou: 0.1       # giou loss gain 1.582
cls: 27.76      # cls loss gain  (CE=~1.0, uCE=~20)
cls_pw: 1.446   # cls BCELoss positive_weight
obj: 2.35      # obj loss gain (*=80 for uBCE with 80 classes)
obj_pw: 3.941   # obj BCELoss positive_weight
iou_t: 0.1      # iou training threshold
ang_t: 3.1415926/12
reg: 0.1
fl_gamma: 0.5   # focal loss gamma
context_factor: 1.0 # 按照短边h来设置的,wh的增幅相同； 调试时设为倒数直接检测


# lr
lr0: 0.00002
multiplier:10
warm_epoch:10
lrf: -4.        # final LambdaLR learning rate = lr0 * (10 ** lrf)
momentum: 0.97  # SGD momentum
weight_decay: 0.0004569  # optimizer weight decay


# aug
hsv_s: 0.5      # image HSV-Saturation augmentation (fraction)
hsv_v: 0.3      # image HSV-Value augmentation (fraction)
degrees: 5.0    # image rotation (+/- deg)
translate: 0.1  # image translation (+/- fraction)
scale: 0.15      # image scale (+/- gain)
shear: 0.0
gamma: 0.2
blur:  1.3
noise: 0.01
contrast: 0.15
sharpen: 0.15
copypaste: 0.1  # 3sigma=3, 船身 h 的 3sigma 段位以内 


# training
epochs: 600
batch_size: 4
save_interval: 300
test_interval: 10