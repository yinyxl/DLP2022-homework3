from skimage.metrics import mean_squared_error as mse
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
import cv2
import os
from glob import glob
from natsort import natsorted


target_dir = './test_true_zhang'  # lable ground-truth
target_files = natsorted(glob(os.path.join(target_dir, '*.png')) + glob(os.path.join(target_dir, '*.jpg')))  

test_result_dir = './test_fake_zhang_80new'  # prediction
test_result_files = natsorted(glob(os.path.join(test_result_dir, '*.png')) + glob(os.path.join(test_result_dir, '*.jpg'))) 

psnr_total = 0
ssim_total = 0
for i in range(0, len(target_files)):
    img1 = cv2.imread(target_files[i])
    img2 = cv2.imread(test_result_files[i])
    p = psnr(img1, img2)
    s = ssim(img1, img2, multichannel=True)  # multichannel True
    print(p)
    print(s)
    # s = ssim(img1, img2)  
    m = mse(img1, img2)

    psnr_total = p + psnr_total
    ssim_total = s + ssim_total

mean_psnr = psnr_total/len(target_files)
mean_ssim = ssim_total/len(target_files)
print('average psnr:',mean_psnr)
print('average ssim:',mean_ssim)
