import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

#DESCOMENTE O CORRETO PARA FUNCIONAR:
#finger =[8, 12, 16, 20]
#finger_tips =[8, 12, 20]
#finger_tips =[8, 12, 16, 20]
thumb_tip= 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            #acessando os pontos de referência pela sua posição
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

            #array para manter verdadeiro ou falso se o dedo estiver dobrado    
            finger_fold_status =[]
            for tip in finger_tips:
                #obtendo a posição da ponta do ponto de referência e desenhando o círculo azul
                #FAÇA IGUALZINHO O PASSO 2 DO PROJETO
                






                #escrevendo a condição para verificar se o dedo está dobrado, ou seja, verificar se o valor inicial da ponta do dedo é menor que a posição inicial do dedo que é o marco interno para o dedo indicador    
                #se o dedo estiver dobrado, mudar a cor para verde

                #DESCOMENTE O CORRETO BASEADO NO PASSO 3:


                #if lm_list[tip].x < lm_list[tip - 3].x:
                    ##cv2.circle(img, (x,y), 15, (0, 255, 0), cv2.FILLED)
                    ##finger_fold_status.append(True)
                #else:
                    ##finger_fold_status.append(False)

                #if lm_list[tip].x < lm_list[tip - 3].x:
                    ##cv.circle(img, (x,y), 15, (0, 255, 0), cv2.FILLED)
                    ##finger_fold_status.append(FALSE)
                #else:
                    ##finger_fold_status.append(TRUE)

            print(finger_fold_status)

             #verificando se todos os dedos estão dobrados
            if all(finger_fold_status):
                #verificando se o polegar está para cima
                if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y:
                    #COLOQUE A MENSAGEM NO PRINT CORRETAMENTE IGUAL NO PASSO 5
                    ####print()  
                    cv2.putText(img ,"CURTI", (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

                #verificando se o polegar está para baixo
                if lm_list[thumb_tip].y > lm_list[thumb_tip-1].y > lm_list[thumb_tip-2].y:
                    #COLOQUE A MENSAGEM NO PRINT CORRETAMENTE IGUAL NO PASSO 6
                    ###print()   
                    cv2.putText(img ,"NÃO CURTI", (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)




            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("rastreador de maos", img)
    cv2.waitKey(1)
