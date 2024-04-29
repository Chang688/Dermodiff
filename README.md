### 基于边界感知的皮肤病灶分割扩散模型 
#### 软件23-1常炜 472321725

皮肤病变分割对皮肤病的早期发现和准确诊断起着至关重要的作用。消噪扩散概率模型(ddpm)最近因其出色的图像生成能力而受到关注。在这些进展的基础上，我们提出了DermoSegDiff，这是一个在学习过程中包含边界信息的皮肤病变分割的新框架。我们的方法引入了一种新的损失函数，在训练过程中对边界进行优先排序，逐渐降低其他区域的重要性。我们还介绍了一种新的基于u - net的去噪网络，该网络可以熟练地将网络内的噪声和语义信息集成在一起。在多个皮肤分割数据集上的实验结果表明，DermoSegDiff优于现有的基于CNN、transformer和diffusion的方法，显示了其在各种场景下的有效性和泛化性。
<p align="center">
  <em>Network</em><br/>
  <img width="600" alt="image" src="https://github.com/mindflow-institue/DermoSegDiff/assets/6207884/7619985e-d894-4ada-9125-9f40a32bae7d">
  <br/>
  <br/>
  <em>Method</em></br>
  <img width="800" alt="image" src="https://github.com/mindflow-institue/DermoSegDiff/assets/61879630/0919e613-972a-47ac-ac79-04a2ae51ed1e">
</p>

<p align="center">
  <img width="620" alt="image" src="https://github.com/mindflow-institue/DermoSegDiff/assets/6207884/30bb1483-e9f8-44df-bede-13238df6f4f0">
</p>

## How to use

  ### Requirements
  
  - Ubuntu 16.04 or higher
  - CUDA 11.1 or higher
  - Python v3.7 or higher
  - Pytorch v1.7 or higher
  - Hardware Spec
    - GPU with 12GB memory or larger capacity (With low GPU memory you need to change and decrease `dim_x_mults`, `dim_g_mults`, `dim_x`, and `dim_g` params. You also need to change `batch_size` respectively. If you tune it well you won't lose considerable capability!)
    - _For our experiments, we used 1GPU(A100-80G)_

  
  ```albumentations==1.3.1
  einops==0.6.1
  ema_pytorch==0.2.3
  matplotlib==3.7.2
  numpy==1.24.4
  opencv==4.6.0
  opencv_python_headless==4.8.0.74
  Pillow==10.0.0
  PyYAML==6.0.1
  scikit_image==0.19.3
  scipy==1.6.3
  termcolor==2.3.0
  torch==2.0.1
  torchvision==0.15.2
  tqdm==4.65.0
  ```
  `pip install -r requirements.txt`

  ### Training
对于训练阶段，你需要选择相关的配置文件，并通过设置所需的目录和更改变量来修改它，如果需要的话，从' src '文件夹中运行以下命令，通过路径准备好的配置文件:
  
  ```python src/training.py -c /path/to/config/file```

你也可以在运行上面的命令时重载一些参数:

  ```bash
usage: [-h] -c CONFIG_FILE [-n MODEL_NAME] [-s INPUT_SIZE] [-b BATCH_SIZE] [-l LEARNING_RATE]
         [-t TIMESTEPS] [-S {linear,quadratic,cosine,sigmoid}] [-e EPOCHS] [--beta_start BETA_START]
         [--beta_end BETA_END] [-D [MODEL_DIM_MULTS [MODEL_DIM_MULTS ...]]] [-E ENSEMBLE]
         [--model_dim_x MODEL_DIM_X] [--model_dim_g MODEL_DIM_G]
         [--model_dim_x_mults [MODEL_DIM_X_MULTS [MODEL_DIM_X_MULTS ...]]]
         [--model_dim_g_mults [MODEL_DIM_G_MULTS [MODEL_DIM_G_MULTS ...]]]
         [--training_optimizer_betas [TRAINING_OPTIMIZER_BETAS [TRAINING_OPTIMIZER_BETAS ...]]]
         [--training_scheduler_factor TRAINING_SCHEDULER_FACTOR]
         [--training_scheduler_patience TRAINING_SCHEDULER_PATIENCE] [--augmentation_p AUGMENTATION_P]
 
  ```
  

  
