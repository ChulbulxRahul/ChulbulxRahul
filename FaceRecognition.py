import  cgi
from base64 import b64decode
import face_recognition
import pint as pint

formData = cgi.FieldStorage()
face_match = 0
image = formData.getvalue("current_image")
email = formData.getlist("email")
data_uri = image
header, encoded = data_uri.split(",", 1)
data = b64decode(encoded)
with open("image.png", "wb") as f:
    f.write(data)
got_image = face_recognition.loade_image_file("image.png")
existing_image = face_recognition.loade_image_file("student/"+email+".jpg")
got_image_facialfeatures = face_recognition.face_encodings(got_image)[0]
existing_image_facialfeatures = face_recognition.face_encodings(existing_image)[0]
results = face_recognition.campare_faces([existing_image_facialfeatures], got_image_facialfeatures)
if (results[0]):
    face_match = 1
else:
    face_match = 0
print("Content-Type: text/html")
pint()
if (face_match ==  1):
    print("<script>alert('welcome ", email," ' )</script>")
else:
    print("<script>alert('face not recognized')</script>")

