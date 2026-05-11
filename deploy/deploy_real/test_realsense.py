import pyrealsense2 as rs
import numpy as np
import cv2
import torch
import torch.nn.functional as F
np.set_printoptions(threshold=np.inf)

@torch.no_grad()
def resize2d_numpy(img_np, size):
    img_tensor = torch.from_numpy(img_np).float()  # 需转为float类型

    if img_tensor.ndim == 2:  # [H, W] → [1, 1, H, W]
        img_tensor = img_tensor.unsqueeze(0).unsqueeze(0)
    elif img_tensor.ndim == 3:  # [H, W, C] → [1, C, H, W]
        img_tensor = img_tensor.permute(2, 0, 1).unsqueeze(0)
    pooled = F.adaptive_avg_pool2d(img_tensor, size)

    result = pooled.squeeze().numpy()
    return result

# 初始化相机
pipeline = rs.pipeline()
config = rs.config()
# config.enable_stream(rs.stream.depth, 424,240, rs.format.z16, 30)
config.enable_stream(rs.stream.depth,640,480,rs.format.z16,30)
pipeline.start(config)
rs_align = rs.align(rs.stream.depth)
rs_hole_filling_filter = rs.hole_filling_filter()
rs_spatial_filter = rs.spatial_filter()
rs_spatial_filter.set_option(rs.option.filter_magnitude, 5)
rs_spatial_filter.set_option(rs.option.filter_smooth_alpha, 0.75)
rs_spatial_filter.set_option(rs.option.filter_smooth_delta, 1)
rs_spatial_filter.set_option(rs.option.holes_fill, 4)
rs_temporal_filter = rs.temporal_filter()
rs_temporal_filter.set_option(rs.option.filter_smooth_alpha, 0.75)
rs_temporal_filter.set_option(rs.option.filter_smooth_delta, 1)
rs_filters = [
    rs_hole_filling_filter,
    rs_spatial_filter,
    rs_temporal_filter
]


crop_bottom = 2
crop_left_right = 4
cfg_depth_near_clip = 0
cfg_depth_far_clip = 2

def _process_depth_image(depth_image):
    # cv2.imshow('depth_image_0', depth_image)
    depth_image = -1 * cv2.resize(depth_image, (106, 60), interpolation=cv2.INTER_CUBIC)
    # cv2.imshow('depth_image_1', depth_image)

    depth_image = __crop_depth_image(depth_image)
    # cv2.imshow('depth_image_2', depth_image)
    # DEPTH_IMAGE 2: [59,98], -1057,0365, float32

    depth_image = np.clip(depth_image,a_min=-cfg_depth_far_clip,a_max=-cfg_depth_near_clip)
    # cv2.imshow('depth_image_3', depth_image)
    # DEPTH_IMAGE 3: [58,98], -1.25, float32

    depth_image = __resize_transform(depth_image).squeeze()
    # cv2.imshow('depth_image_4', depth_image)
    # DEPTH_IMAGE 4: [58,87], -1.26, float32

    depth_image = __normalized_depth_image(depth_image)
    # cv2.imshow('depth_image_5', depth_image)
    # DEPTH_IMAGE 5: [58,87], 0.26, float32

    depth_image += 0.5
    # cv2.imshow('depth_image_6', depth_image)

    return depth_image

def __crop_depth_image(depth_image):
    return depth_image[:-crop_bottom,crop_left_right:-crop_left_right]

def __resize_transform(depth_image):
    target_size = (87,58)
    resized = cv2.resize(depth_image,target_size,interpolation=cv2.INTER_CUBIC)
    return resized

def __normalized_depth_image(depth_image):
    depth_image = depth_image * -1
    depth_image = (depth_image - cfg_depth_near_clip) / (cfg_depth_far_clip - cfg_depth_near_clip) - 0.5
    return depth_image

def _process_depth_image_v2(depth_image):
    cropping = [60,100,80,36]
    depth_range = (0.0, 3.0 * 1000)
    output_resolution = [58,87]


    depth_image = depth_image[cropping[0]:-cropping[1]-1,cropping[2]:-cropping[3]-1]
    # cv2.imshow('depth_image_3',depth_image)

    depth_image = np.clip(depth_image,-depth_range[1],-depth_range[0])
    # cv2.imshow('depth_image_4',depth_image)

    # depth_image =  cv2.resize(depth_image,output_resolution,interpolation=cv2.INTER_CUBIC)
    depth_image = resize2d_numpy(depth_image, output_resolution)
    # cv2.imshow('depth_image_5', depth_image)

    depth_image *= -1
    depth_image = depth_image / (depth_range[1] - depth_range[0]) - 0.5
    # cv2.imshow('depth_image_6', depth_image)

    depth_image += 0.5
    # cv2.imshow('depth_image_7', depth_image)
    # print('The shape of depth_image is:', depth_image.shape)
    return depth_image

try:
    while True:
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        if not depth_frame:
            continue

        depth_image = np.asanyarray(depth_frame.get_data()).astype(np.float32)
        # cv2.imshow('depth_image_0', depth_image)
        depth_image = -1 * cv2.resize(depth_image, (106, 60), interpolation=cv2.INTER_CUBIC)
        # cv2.imshow('depth_image_1', depth_image)

        for rs_filter in rs_filters:
            depth_frame = rs_filter.process(depth_frame)


        depth_image = np.asanyarray(depth_frame.get_data()).astype(np.float32)
        depth_image *= -1
        # cv2.imshow('depth_image_2', depth_image)


        # cv2.imshow("Depth Image",_process_depth_image(depth_image))
        cv2.imshow("Depth Image", _process_depth_image_v2(depth_image))




        if cv2.waitKey(1) == 27:
            break
finally:
    pipeline.stop()
    cv2.destroyAllWindows()
