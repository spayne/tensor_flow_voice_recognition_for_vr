

import os

# APP directory
if os.environ.get("APP_DIR") == None:
    os.environ["APP_DIR"] = "/nemo_asr_app"
app_dir = os.environ.get("APP_DIR")

# Data directory for datasets and results
if os.environ.get("DATA_DIR") == None:
    os.environ["DATA_DIR"] = "/data/asr/"
data_dir = os.environ.get("DATA_DIR")
print("APP DIR:", app_dir,"DATA DIR:", data_dir)


import pandas as pd
import numpy as np
from easydict import EasyDict as edict

from tools.System.config import cfg
from tools.System.reader import Reader
from tools.System.nemo_fns import get_onnx_cmd, get_onnx_trt_cmd
from tools.filetools import file_exists
from tools.misc import create_lm_dataset, parse_manifest_wer, barplot_manifest, get_transcript, get_gtruth

# download the pretrained model
if not file_exists("/nemo_asr_app/models/quartznet15x5/JasperEncoder-STEP-247400.pt"):
    os.system('cd /nemo_asr_app/models && wget --content-disposition https://api.ngc.nvidia.com/v2/models/nvidia/quartznet15x5/versions/2/zip -O quartznet15x5_2.zip')
    os.system('cd /nemo_asr_app/models && unzip quartznet15x5_2.zip')

#
# This writes a bunch of files.
#   The manifest is pre-populated with the baseline acoustic model - a model pretrained on LibriSpeech 
#    and using greedy decoder.
project_id = 'WSJ'
project = Reader.new(project_id)


