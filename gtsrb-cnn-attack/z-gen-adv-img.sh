#!/bin/bash
export SIGN_PREFIX="usstop-l1rectangles-less-256"
export SIGN_MASK="mask_l1rectangles-less_256.png"
export EPOCH=999

python apply_noise_no_resize.py \
    --img_cols 256 \
    --img_rows 256 \
    --nb_channels 3 \
    --src_image ./input_images/Sign_Stop_no_alpha.png \
    --output_path ./printed_images/Sign_Stop_no_alpha-${SIGN_PREFIX}-epoch-${EPOCH}-noresize.png \
    --model_path ./optimization_output/${SIGN_PREFIX}/model/${SIGN_PREFIX}-${EPOCH} \
    --attack_mask ./masks/${SIGN_MASK} \
    --device="/cpu"
