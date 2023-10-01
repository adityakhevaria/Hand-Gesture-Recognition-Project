import cv2
import numpy
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
Hands = mpHands.Hands()
draw = mp.solutions.drawing_utils
lmp=cv2.imread('puy.jfif')
lpp=cv2.imread('pio.jfif')
ltp=cv2.imread('wew.jfif')
lop=cv2.imread('hgh.jfif')
Finger_tips =[8,12,16,20]
thumb_tip=4

while True:
    sucess, img = cap.read()
    img=cv2.flip(img,1)
    h,w,c =img.shape
    rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    

    results = Hands.process(rgb)

    if results.multi_hand_landmarks:
        for hands in results.multi_hand_landmarks:
            lm_list=[]
            for id,lm in enumerate(hands.landmark):
                lm_list.append(lm)
                Finger_fold_status =[]

            for tip in Finger_tips:
                m,n=int(lm_list[tip].x*w),int(lm_list[tip].y*h)
                #print(id,':',m,n)
                cv2.circle(img,(m,n),13,(0,255,0),cv2.FILLED)

                if lm_list[tip].x < lm_list[tip-3].x:
                       cv2.circle(img,(m,n),13,(0,0,255),cv2.FILLED)
                       Finger_fold_status.append(True)
                else:
                     Finger_fold_status.append(False)

            #print(Finger_fold_status)

        if all(Finger_fold_status):
            if lm_list[thumb_tip].y < lm_list[thumb_tip -1].y < lm_list[thumb_tip -2].y:
              
                    print("LIKE")
                    h,w,c=lmp.shape
                    img[0:h,0:w]=lmp
            else:
                    print("DISLIKE") 
                    h,w,c = lpp.shape
                    img[0:h,0:w]=lpp     


        
        if lm_list[tip].x>lm_list[tip-1].x:
            print("NEUTRAL")
            h,w,c =ltp.shape
            img[0:h,0:w]=ltp


        if lm_list[tip].x<lm_list[tip-3].x:
            if lm_list[thumb_tip].x<lm_list[thumb_tip-2].x:
                print("DYBALA CELEBRATION")  
                h,w,c =lop.shape
                img[0:h,0:w]=lop  



        
               


            draw.draw_landmarks(img, hands, mpHands.HAND_CONNECTIONS )
            

    cv2.imshow('img',img)


    if cv2.waitKey(1) == ord('q'):
        break
