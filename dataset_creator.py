import cv2, sys, numpy, os

def create_dataset():
    haar_file = 'haarcascade_frontalface_default.xml'
  
    # All the faces data will be 
    #  present this folder 
    datasets = 'datasets'  
      
      
    # These are sub data sets of folder,  
    
    sub_data = str(input('enter your name: '))

    # defining the size of images  
    (width, height) = (100, 100)   
      
    path = os.path.join(datasets, sub_data) 
    if not os.path.isdir(path): 
        os.mkdir(path) 
      
    #'0' is used for my webcam,  
    # if you've any other camera 
    #  attached use '1' like this 
    face_cascade = cv2.CascadeClassifier('./haar_cascade_face.xml') 
    webcam = cv2.VideoCapture(0)

  
    # The program loops until it has 100 images of the face. 
    count = 0
    while count < 100:
        # get frames from webcam
        ret, cap = webcam.read()
        if ret == 0:
            break
        # grayscale filter on frames
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        
        for (x, y, w, h) in faces:
            cv2.putText(cap, 'Creating face dataset',  (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0)) 
            # draw rectangle on face
            cv2.rectangle(cap, (x, y), (x + w, y + h), (255, 0, 0), 2) 
            face = gray[y:y + h, x:x + w] 
            face_resize = cv2.resize(face, (width, height)) 
            cv2.imwrite('% s/% s.png' % (path, count), face_resize) 
        count += 1
          
        cv2.imshow('OpenCV', cap)
        key = cv2.waitKey(10) 
        if key == 27:
            cv2.destroyAllWindows()
            break

    cv2.destroyAllWindows()

