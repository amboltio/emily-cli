import cv2


class FaceDetector:

    def __init__(self, model_name='haarcascade_eye.xml', scale_factor=1.1, min_neighbors=8):

        # Initialize OpenCV's cascading classifier
        self.eye_cascade_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + model_name)

        # Parameters for the detectMultiScale method which is used for detects the eyes (see detect_eyes)
        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors

    def detect_face(self, image):
        """
        Detects a single face in the image based on detected eyes.
        Input: img (dtype: uint8).
        Attention: The detect_face only works for a single person in the image an the persons's eyes has to be visible
        """
        eyes = self.detect_eyes(image)

        if eyes is not None:
            # Convert eyes to face
            right_eye, left_eye = eyes
            img_h, img_w = image.shape[:2]
            face = self._eyes_2_face(right_eye, left_eye, img_h, img_w)
            return face, eyes
        else:
            return None

    def detect_eyes(self, image):
        """
        Detects the eyes of a person using OpenCV's CascadeClassifier
        Input: img (dtype: uint8).
        Attention: The detect_face only works for a single person in the image an the persons's eyes has to be visible
        """
        # Resize the input image and convert to gray scale
        # image = self._resize(image, 256)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


        # Detect eyes
        eyes = self.eye_cascade_classifier.detectMultiScale(gray, self.scale_factor, self.min_neighbors)
        if len(eyes) == 2:
            eye_1, eye_2 = eyes[:2]
            right_eye, left_eye = self._get_left_and_right_eye(eye_1, eye_2)
            return right_eye, left_eye
        else:
            return None

    def _resize(self, image, max_height=256):
        scale = self._get_resize_scale_from_img_height(image, max_height)
        image = cv2.resize(image, dsize=(int(image.shape[1] * scale), int(image.shape[0] * scale)))
        return image

    @staticmethod
    def _eyes_2_face(right_eye, left_eye, img_height, img_width):

        # Get the top left corner (x1, y1) of each eye and their width and height
        (x_right_eye, y_right_eye, w_right_eye, h_right_eye) = right_eye
        (x_left_eye, y_left_eye, w_left_eye, h_left_eye) = left_eye

        # Set the top left corner and bottom right corner of the face based on the eye's postions
        face_x1 = x_right_eye - int(w_right_eye * 2)
        face_y1 = y_right_eye - int(h_right_eye * 3)
        face_x2 = x_left_eye + w_left_eye + int(w_right_eye * 2)
        face_y2 = y_left_eye + int(h_right_eye * 4)

        # Make sure the eye bbox doesn't surpass the img border
        if face_x1 <= 0:
            face_x1 = 0
        if face_y1 <= 0:
            face_y1 = 0
        if face_x2 >= img_width - 1:
            face_x2 = img_width - 1
        if face_y2 >= img_height - 1:
            face_y2 = img_height - 1

        return face_x1, face_y1, face_x2, face_y2

    @staticmethod
    def _get_left_and_right_eye(eye1, eye2):
        if eye1[0] > eye2[0]:
            right_eye = eye2
            left_eye = eye1
        else:
            right_eye = eye1
            left_eye = eye2

        return right_eye, left_eye

    @staticmethod
    def _get_resize_scale_from_img_height(image, max_height=256):
        img_height = image.shape[0]
        if img_height > max_height:
            return max_height / img_height
        else:
            return 1.
