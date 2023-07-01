# dataset settings
# dataset_type = 'VOCDataset'
# data_root = 'data/VOCdevkit/'
data_root = 'D:\Projects\data\OPIXray_voc/'
dataset_type = 'VOCDataset'
CLASSES = ('Folding_Knife','Straight_Knife','Scissor','Utility_Knife','Multi-tool_Knife')
img_scale=(320,320)
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=img_scale, keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=img_scale,
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=16,
    workers_per_gpu=4,
    train=dict(


            classes=CLASSES,


            type=dataset_type,
            ann_file=data_root + 'VOC2007/ImageSets/Main/train.txt',
            img_prefix=data_root + 'VOC2007/',
            pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        classes=CLASSES,
        ann_file=data_root + 'VOC2007/ImageSets/Main/test.txt',
        img_prefix=data_root +'VOC2007/' ,
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        classes=CLASSES,
        ann_file=data_root + 'VOC2007/ImageSets/Main/test.txt',
        img_prefix=data_root +'VOC2007/' ,
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='mAP')
