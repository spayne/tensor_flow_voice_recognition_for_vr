sudo mkdir /sys/fs/cgroup/systemd
sudo mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd

sudo service docker start

export DATA_DIR="/data/asr"
sudo docker run --gpus all -it --rm --name run_nemo_asr_app --ipc=host \
--env DATA_DIR=$DATA_DIR -v $DATA_DIR:$DATA_DIR \
-p 8888:8888 nvcr.io/nvidia/nemo_asr_app_img:20.07