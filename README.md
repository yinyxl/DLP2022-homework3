# Reappearance [Single Image Reflection Removal through Cascaded Refinement]

The original code for the Paper:  https://github.com/JHL-HUST/IBCLN.git

**[Single Image Reflection Removal through Cascaded Refinement  ][1]**\
Chao Li, Yixiao Yang, Kun He, Stephen Lin, John E. Hopcroft\
[CVPR 2020]


## Description of the files in this repository

1) ``train.py``: Execute this file to train the model  
2) ``test.py``: Execute this file to test the model  
3) ``model/IBCLN_model_origin.py``: Contains the class defining our model,the original code   
4) ``model/IBCLN_model_modify.py``: Contains the class defining our model,the modified code for my modifications  
5) ``model/networks_origin.py``: Contains the function that defining the networks and losses, the original code. 
6) ``model/networks_modify.py``: Contains the function that defining the networks and losses, the modified code for my modifications. 
7) ``options/base_options.py``: This file contains the basic options 
8) ``options/train_options.py``: This file contains the options for training 
9) ``options/test_options.py``: This file contains the options for testing 


### Details for my modifications
``model/IBCLN_model_modify.py``: I add the ``SSIM_loss`` and modify the loss functions on line 230  
``model/networks_modify.py``: I delete the ``conv5`` and ``conv6`` and add the ``diconv5``   


### Details for the pre-trained models
``final_net_G_R.pth`` and ``final_net_G_T.pth``:the pre-trained model provided by the author  
``80_net_G_R.pth`` and ``80_net_G_T.pth``:my trained model for 80 epoch
``80new_net_G_R.pth`` and ``80new_net_G_T.pth``:the trained model of new network architecture, 80 epoch  
``90loss2_net_G_R.pth`` and ``90loss2_net_G_T.pth``: the trained model of new loss functions, 90 epoch  
``80_2_net_G_R.pth`` and ``80_2_net_G_T.pth``: the trained model,lr = 0.0001 for 5 epoch, 80+5  
``90new_net_G_R.pth`` and ``90new_net_G_T.pth``:the trained model with added ssim_loss  


### Train
I trained the model on Bitahub and tested on my PC, so the base_options, train_options and test_options are different from my actual use.   

### pre-trained models and datasets  
download here :https://rec.ustc.edu.cn/share/4d358100-9667-11ed-863b-35c509b9e673  
