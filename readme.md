## Why am I here today
I'm interested in tensorflow and learning applications
I'd like a fast response speech recognition for the Math Boxer game

## Other documents related to this status
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


## Running the basic models
To run the models associated with [1], run the start_asr.sh then open a web browser to http://localhost:8888

Then double click on WSJ_Domain_Specific_ASR.ipynb


