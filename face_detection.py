import cv2

# Make sure to upload a picture that has a face.

# Load the cascade
face_cascade = cv2.CascadeClassifier("face_detection.xml")

# Read the input image
img = cv2.imread("img.jpg")

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the output
cv2.imshow("Faces", img)
cv2.waitKey()


