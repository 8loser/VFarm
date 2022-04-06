#!/bin/bash

# 模糊
# ffmpeg -f concat -safe 0 -protocol_whitelist file,https,tls,tcp -i $1 -vf "split[original][copy];[copy]scale=ih*16/9:-1,crop=h=iw*9/16,gblur=sigma=20[blurred];[blurred][original]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2" -y $2
ffmpeg -f concat -safe 0 -protocol_whitelist file,https,tls,tcp -i $1 -filter_complex "[0]scale=hd720,setsar=1,boxblur=20:20[b]; [0]scale=-1:720[v];[b][v]overlay=(W-w)/2" -y $2

# 黑色pad
# ffmpeg -f concat -safe 0 -protocol_whitelist file,https,tls,tcp -i $1 -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:-1:-1:color=black" -r 60 -strict experimental -y $2