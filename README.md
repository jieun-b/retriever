# retriever

## Installation

### Build environment

```bash
conda create -n retriever python=3.10 -y
conda activate retriever
```

This project uses **PyTorch 2.2.2** (with `torchvision==0.17.2`, `torchaudio==2.2.2`).

Please install the appropriate version for your system (CPU or CUDA) following the [official PyTorch instructions](https://pytorch.org/get-started/previous-versions/).

Example (CUDA 12.1):

```bash
conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 pytorch-cuda=12.1 -c pytorch -c nvidia
```

Note: If you have a custom CUDA install, you may need to export:

```bash
export CUDA_HOME=/usr/local/cuda-12.1
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
```

Install the remaining dependencies:

```bash
pip install -r requirements.txt
```