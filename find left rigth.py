import cv2 
from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.5,maxHands=2)
cap = cv2.VideoCapture(0)
finger0 = "pong"
finger1 = "chi"
finger2 = "klang"
finger3 = "nang"
finger4 = "koy"
while True:
    ret,frame=cap.read()
    #frame=cv2.flip(frame,1)
    hands,frame=detector.findHands(frame)
    if hands:
        hands1=hands[0]
        fingers1=detector.fingersUp(hands1)
        print(fingers1)
        if fingers1[0] == 1 :
            cv2.putText(frame, str(finger0), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 1)
        if fingers1[1] == 1 :
            cv2.putText(frame, str(finger1), (100, 70), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 1)
        if fingers1[2] == 1 :
            cv2.putText(frame, str(finger2), (160, 70), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 1)    
        if fingers1[3] == 1 :
            cv2.putText(frame, str(finger3), (250, 70), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 1)
        if fingers1[4] == 1 :
            cv2.putText(frame, str(finger4), (350, 70), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 1)
                                
    if len(hands)==2:
        hands2=hands[1]
        fingers2=detector.fingersUp(hands2)
        print(fingers1,fingers2)
        if fingers2[0] == 1 :
            cv2.putText(frame, str(finger0), (10, 150), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 1)
        if fingers2[1] == 1 :
            cv2.putText(frame, str(finger1), (100, 150), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 1)
        if fingers2[2] == 1 :
            cv2.putText(frame, str(finger2), (160, 150), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 1)    
        if fingers2[3] == 1 :
            cv2.putText(frame, str(finger3), (250, 150), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 1)
        if fingers2[4] == 1 :
            cv2.putText(frame, str(finger4), (350, 150), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 1)
    frame=cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
    
cap.relase()
cv2.destroyAllWinfdows()
    