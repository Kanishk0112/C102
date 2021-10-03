import cv2
import dropbox
import time
import random
Starttime=time.time()
def TakeSnapShot():
    number=random.randint(0,100)
    VideoCaptureObj=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=VideoCaptureObj.read()
        Imgname="Img"+str(number)+".png"
        cv2.imwrite(Imgname,frame)
        Starttime=time.time()
        result=False
    return Imgname
    print("Snapshot Taken")
    VideoCaptureObj.release()
    cv2.destroyAllWindows()
def Upload_File(Imagename):
    access_token="HS2eKpkUaVcAAAAAAAAAAebXw_S-Ax7SAPi29AJ95kExL2GJVGeclpn1_fu3KCGd"
    file=Imagename
    file_from=file
    file_to="/test/"+(Imagename)
    dbx=dropbox.Dropbox(access_token)
    with open (file_from, "rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()-Starttime)>=5):
            name=TakeSnapShot()
            Upload_File(name)
main()            
