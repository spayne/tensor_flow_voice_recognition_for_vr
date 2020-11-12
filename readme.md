## Motivation / Project Purpose
I'm interested in tensorflow and learning applications
I'd like a fast response speech recognition for the Math Boxer game

## Other documents related to this status
A dataflow diagram of the model building scripts/process:
https://www.figma.com/file/v8Luqqm0WzLP2dPko37xXB/tensor-flow?node-id=0%3A1


## Primary References
NVidia Developer Blog on "How to build Domain Specific Automatic Speech Recognition Models on GPUs"
[1] https://developer.nvidia.com/blog/how-to-build-domain-specific-automatic-speech-recognition-models-on-gpus/

## Supplemental References
[2] CUDA on WSL User Guide
https://docs.nvidia.com/cuda/wsl-user-guide/index.html
[3] Workaround for cgroup issue
https://github.com/docker/for-linux/issues/219#issuecomment-375160449

## Current Status
Docker configuration is working on PC/WSL2
* Follow [2]
 * In particular note that you need to:
 ** be on windows insider builds
 ** run sudo service docker start


# Install Notes
Installed TensorRT 7.2.1 and CUDA 11.1 zip from 
to download go to: https://developer.nvidia.com/nvidia-tensorrt-7x-download

Follow install guide: https://docs.nvidia.com/deeplearning/tensorrt/archives/tensorrt-721/install-guide/index.html#installing-zip
Specifically 4.5 zip file install
1. unzip to d:\tensorrt

2. download and install cuda11.1.1 https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork
don't let it overwrite the display driver I'm using 460.20 because of wsl/docker with it's 456.81
let it use default install directory of C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.1


3. download and install cuDNN 8.0.4 from https://developer.nvidia.com/cudnn
it comes down as a zip file:  cudnn-11.1-windows-x64-v8.0.4.30.zip

4. extract to d:\cudnn-11.1-windows-x64-v8.0.4.30

5. copy over the bin lib include into the tensorrt folder

6. Per 4.2 "Copy the DLL files from <installpath>/lib to your CUDA installation" copy lib to 
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.1\bin

7. Open "D:\tensorrt\TensorRT-7.2.1.6\samples\sampleMNIST" and see if it builds - 
fails to link cannot open cudnn.lib.  move libs from x64 of D:\tensorrt\TensorRT-7.2.1.6\lib\x64 to D:\tensorrt\TensorRT-7.2.1.6\lib


## To run the basic models
To run the models associated with [1], run the start_asr.sh then open a web browser to http://localhost:8888

Then double click on WSJ_Domain_Specific_ASR.ipynb


