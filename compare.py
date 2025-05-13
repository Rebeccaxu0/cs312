# Python program for face 
# comparison 
  
  
from __future__ import print_function, unicode_literals 
from facepplib import FacePP, exceptions 
  
   
# define face comparing function 
def face_comparing(app, Image1, Image2): 
      
    print() 
    print('-'*30) 
    print('Comparing Photographs......') 
    print('-'*30) 
  
   
    cmp_ = app.compare.get(image_url1 = Image1, 
                           image_url2 = Image2) 
   
    print('Photo1', '=', cmp_.image1) 
    print('Photo2', '=', cmp_.image2) 

    print('Confidence', '=', cmp_.confidence)
   
    # Comparing Photos 
    if cmp_.confidence > 70: 
        print('Both photographs are of same person......') 
    else: 
        print('Both photographs are of two different persons......') 
  
          
# Driver Code  
if __name__ == '__main__': 
   
    # api details 
    api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'
   
    try: 
           
        # call api 
        app_ = FacePP(api_key = api_key,  
                      api_secret = api_secret) 
          
        # Pair
        image1 = 'https://ew.com/thmb/52qjEp3tdLZOHZG80S9GDlDRgoo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Sabrina-Carpenter-080624-1-305ff7f67fba42569018822292f09f09.jpg'
        image2 = 'https://media.glamour.com/photos/674de951e3207eff7c778ed4/master/w_2560%2Cc_limit/GettyImages-2177695508.jpg'
        face_comparing(app_, image1, image2)         
   
    except exceptions.BaseFacePPError as e: 
        print('Error:', e) 