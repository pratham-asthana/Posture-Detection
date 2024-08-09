import tensorflow as tf
from tensorflow.keras.layers import Dense, Reshape, Flatten, Conv2D, Conv2DTranspose
from tensorflow.keras.models import Sequential
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

cap.release()
cv2.destroyAllWindows()