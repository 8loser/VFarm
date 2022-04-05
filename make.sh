#!/bin/bash

# 模糊
ffmpeg -f concat -safe 0 -protocol_whitelist file,https,tls,tcp -i video.list -vf "split[original][copy];[copy]scale=ih*16/9:-1,crop=h=iw*9/16,gblur=sigma=20[blurred];[blurred][original]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2" -y out.mp4

# 黑色pad
# ffmpeg -f concat -safe 0 -protocol_whitelist file,https,tls,tcp -i video.list -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:-1:-1:color=black" -y out.mp4