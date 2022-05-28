import cv2
import mediapipe as mp
import time 

cap =cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
 
while True :
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)  
   
    if not success:
        break
    key =cv2.waitKey(1)
    if key == ord('e'):
        cv2.destroyAllWindows()
        break
  
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                
        #pixal
                x,y,z = img.shape
                #print(img.shape)
                cx,cy,cz = int(lm.x * y),int(lm.y*x),int(lm.z*z)
                #print (id,cx,cy,cz)
                if id == 0:
                    cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)
                if id==0:
                    print (id,cx,cy)
                    if cx<=400:
                        print ("its working")
                
            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(31, 147, 224),2)
    
    cv2.imshow("image" , img)
    