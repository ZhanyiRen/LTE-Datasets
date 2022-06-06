# LTE-Datasets
40GB LTE dataset of raw signals collect in shielding box.

## How to get the dataset
This repository contains the source dataset of LTE raw signals. All the dataset is available in https://gas.graviti.cn/dataset/pikachu/LTE_Dataset.
Please email ren12852@stu.xjtu.edu.cn for Accesskey.

Step1: Run get_data_urls.py for the dictionary including each segment, and their data url;    
Step2: Copy each data_url to browser and download automatically. Besides, you can download using API or spider;  
Step3: Rename the downloaded file by 'XXX.mat', the filename extension must be '*.mat';  
Step4: Now you can load these mat files

## Description
Each mat file includes a two-dimension matrix size of M*N, where M is the number of sample and N is the data length (8192) of each sample.

The collection system, including shield box, switch, PC and GPU server. The raw signals are collected in a shield box with an ideal environment to eliminate channel influences, and PC for collection system, GPU server for data storage and processing.  
The configuration of the collection base station is frequency division duplexing (FDD) mode with downlink and uplink of 1.82GHz and 1.725GHz respectively. The intermediate frequency is 140 MHz and the sampling rate of intermediate frequency acquisition is 122.88 MHz with the frame length of 8192, real signal. Ultimately, we obtained over 40000 frames per mobile phone, total up to 40GB.


## Citing This Paper
@inproceedings{ren2022deep,\\
  title={Deep RF Device Fingerprinting by Semi-Supervised Learning with Meta Pseudo Time-Frequency Labels},\\
  author={Ren, Zhanyi and Ren, Pinyi and Zhang, Tiantian},\\
  booktitle={2022 IEEE Wireless Communications and Networking Conference (WCNC)},\\
  pages={2369--2374},\\
  year={2022},\\
  organization={IEEE} \\
}

## Acknowledgement
If you have any problems, please contact us with ren12852@stu.xjtu.edu.cn.
