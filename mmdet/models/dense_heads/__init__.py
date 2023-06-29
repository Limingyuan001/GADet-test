# Copyright (c) OpenMMLab. All rights reserved.
from .anchor_free_head import AnchorFreeHead
from .anchor_head import AnchorHead
from .ascend_anchor_head import AscendAnchorHead
from .ascend_retina_head import AscendRetinaHead
from .ascend_ssd_head import AscendSSDHead
from .atss_head import ATSSHead
from .autoassign_head import AutoAssignHead
from .cascade_rpn_head import CascadeRPNHead, StageCascadeRPNHead
from .centernet_head import CenterNetHead
from .centripetal_head import CentripetalHead
from .corner_head import CornerHead
from .ddod_head import DDODHead
from .deformable_detr_head import DeformableDETRHead
from .detr_head import DETRHead
from .embedding_rpn_head import EmbeddingRPNHead
from .fcos_head import FCOSHead
from .fovea_head import FoveaHead
from .free_anchor_retina_head import FreeAnchorRetinaHead
from .fsaf_head import FSAFHead
from .ga_retina_head import GARetinaHead
from .ga_rpn_head import GARPNHead
from .gfl_head import GFLHead
from .guided_anchor_head import FeatureAdaption, GuidedAnchorHead
from .lad_head import LADHead
from .ld_head import LDHead
from .mask2former_head import Mask2FormerHead
from .maskformer_head import MaskFormerHead
from .nasfcos_head import NASFCOSHead
from .paa_head import PAAHead
from .pisa_retinanet_head import PISARetinaHead
from .pisa_ssd_head import PISASSDHead
from .reppoints_head import RepPointsHead
from .retina_head import RetinaHead
from .retina_sepbn_head import RetinaSepBNHead
from .rpn_head import RPNHead
from .sabl_retina_head import SABLRetinaHead
from .solo_head import DecoupledSOLOHead, DecoupledSOLOLightHead, SOLOHead
from .solov2_head import SOLOV2Head
from .ssd_head import SSDHead
from .tood_head import TOODHead
from .vfnet_head import VFNetHead
from .yolact_head import YOLACTHead, YOLACTProtonet, YOLACTSegmHead
from .yolo_head import YOLOV3Head
from .yolof_head import YOLOFHead
from .yolox_head import YOLOXHead
from .yolox_head_visual import YOLOXHead_visual
# from .yolox_head_cyber import YOLOXHead_cyber
# from .yolox_head_cyber01 import YOLOXHead_cyber
# from .yolox_head_cyber02 import YOLOXHead_cyber
# from .yolox_head_cyber03 import YOLOXHead_cyber
from .yolox_head_cyber04 import YOLOXHead_cyber
# from .yolox_head_cyber05 import YOLOXHead_cyber
# from .yolox_head_cyber06 import YOLOXHead_cyber

# from .yolox_head_PDLC import YOLOXHead_PDLC # 使用arealoss
# from .yolox_head_PDLC02 import YOLOXHead_PDLC # 使用factor + arealoss
# from .yolox_head_PDLC03 import YOLOXHead_PDLC # 使用giouloss+factor
# from .yolox_head_PDLC168 import YOLOXHead_PDLC #
# from .yolox_head_PDLC169 import YOLOXHead_PDLC #
# from .yolox_head_PDLC170 import YOLOXHead_PDLC #
# from .yolox_head_PDLC171 import YOLOXHead_PDLC #
# from .yolox_head_PDLC172 import YOLOXHead_PDLC #
# from .yolox_head_PDLC173 import YOLOXHead_PDLC #
# from .yolox_head_PDLC174 import YOLOXHead_PDLC #
# from .yolox_head_PDLC175 import YOLOXHead_PDLC #
from .yolox_head_PDLC149 import YOLOXHead_PDLC #


from .yolo_head_multi5 import YOLOV3HeadMulti5
from .yolo_head_loss_area import YOLOV3Head_area
from .yolo_head_loss_area_L1 import YOLOV3Head_area_L1
from .yolo_head_loss_true_area import YOLOV3Head_true_area
__all__ = [
    'AnchorFreeHead', 'AnchorHead', 'GuidedAnchorHead', 'FeatureAdaption',
    'RPNHead', 'GARPNHead', 'RetinaHead', 'RetinaSepBNHead', 'GARetinaHead',
    'SSDHead', 'FCOSHead', 'RepPointsHead', 'FoveaHead',
    'FreeAnchorRetinaHead', 'ATSSHead', 'FSAFHead', 'NASFCOSHead',
    'PISARetinaHead', 'PISASSDHead', 'GFLHead', 'CornerHead', 'YOLACTHead',
    'YOLACTSegmHead', 'YOLACTProtonet', 'YOLOV3Head', 'PAAHead',
    'SABLRetinaHead', 'CentripetalHead', 'VFNetHead', 'StageCascadeRPNHead',
    'CascadeRPNHead', 'EmbeddingRPNHead', 'LDHead', 'AutoAssignHead',
    'DETRHead', 'YOLOFHead', 'DeformableDETRHead', 'SOLOHead',
    'DecoupledSOLOHead', 'CenterNetHead', 'YOLOXHead',
    'DecoupledSOLOLightHead', 'LADHead', 'TOODHead', 'MaskFormerHead',
    'Mask2FormerHead', 'SOLOV2Head', 'DDODHead', 'AscendAnchorHead',
    'AscendRetinaHead', 'AscendSSDHead',
    'YOLOV3HeadMulti5','YOLOV3Head_area','YOLOV3Head_area_L1'
    ,'YOLOV3Head_true_area','YOLOXHead_cyber','YOLOXHead_PDLC'
]
