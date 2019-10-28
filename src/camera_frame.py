# Bibliotecas necessarias
import rospy
import cv2
import time
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Int32
from sensor_msgs.msg import Image

# Leitura do arquivo haar para criar um classificador
classificador = cv2.CascadeClassifier('cascades/haarcascade_blackbox_default.xml')



# Exibicao das imgs capturadas em forma de video
while True:
	conectado, frame = video.read()
	# print(conectado)
	# print(frame)

		cv2.imshow('Video', frame)

	# Interromper a exibicao
	if cv2.waitKey(1) == ord('q'):
		break

# Funcao q ira executar o movimento do robo
def callback(data):
    # Criacao do objeto da imagem
    #ros_frame = data.data

    # Criacao do objeto de convercao
    bridge = CvBridge()

    # Converter a imagem ros para imagem cv2
    cv2_frame = bridge.imgmsg_to_cv2(data, "bgr8")
  
    # Converssao da imagem para escala de cinza
	  frameCinza = cv2.cvtColor(cv2_frame, cv2.COLOR_BGR2GRAY)
	
	  # Deteccao da caixa na imagem 
	  # minSize = menor obj a ser reconhecido. 30 x 30 eh o padrao
	  caixasDetectadas = classificador.detectMultiScale(frameCinza, minSize=(50, 50))
	
	  # Desenho do retangulo para a caixa detectada
	  for (x, y, largura, altura) in caixasDetectadas:	
		  # Desenho do retangulo. No final cor e largura da borda
		  cv2.rectangle(cv2_frame, (x,y), (x + largura, y + largura), (0, 0 , 255), 2)  
      
    # Exibir a imagem em uma janela
    cv2.imshow('frame', cv2_frame)

    cv2.waitKey(1)  
    
    
def listener():
    # Inicio do node camera_sub
    rospy.init_node('camera_sub', anonymous=True)

    # Inscricao no topico e definicao da callback como funcao a ser executada
    rospy.Subscriber("camera_topic", Image, callback)

    # Mantem o python funcionando apos o encerramendo do node
    rospy.spin()


# Funcao main
if __name__ == '__main__':
    listener()
