# Python program for face 
# comparison 
  
  
from __future__ import print_function, unicode_literals 
from facepplib import FacePP, exceptions 
import os
import pandas as pd
import matplotlib.pyplot as plt
   
# define face comparing function 
def face_compare(app, Image1, Image2): 
    cmp_ = app.compare.get(image_url1 = Image1, 
                           image_url2 = Image2) 
   
    return cmp_.confidence

def get_image_url(path):
    base_url = 'https://github.com/Rebeccaxu0/cs312/blob/main/'
    return base_url + path
   
# Driver Code  
if __name__ == '__main__': 
   
    # api details 
    api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'
   
           
    # call api 
    app_ = FacePP(api_key = api_key,  
                    api_secret = api_secret) 
    
    synthetic_folder = 'Synthetic-Images'
    training_folder = 'Training-Images'

    synthetic_images = [f for f in os.listdir(synthetic_folder)]
    training_images = [f for f in os.listdir(training_folder)]
        
    # Create an empty DataFrame to store results
    similarity_matrix = pd.DataFrame(index=synthetic_images, columns=training_images)

    # Loop through each pair
    for synth_img in synthetic_images:
        for train_img in training_images:
            url1 = get_image_url(os.path.join(synthetic_folder, synth_img))
            url2 = get_image_url(os.path.join(training_folder, train_img))
            similarity_matrix.at[synth_img, train_img] = face_compare(app_, url1, url2)

    
    plt.figure()
    plt.imshow(similarity_matrix)