import os
import cv2
import shutil

logic = True
while logic:
    try:
        #Get file name
        fileName = str(input("\n Video (.mp4/.mov)>>> ")).strip()
        cap= cv2.VideoCapture(fileName)
        #Get fps and total frames
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        #Get number sample to make directories
        totalFrame =int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        logic = False
    except:
        print("<ERROR> The file does not excist or invalid file format")

#Get number sample to make directories
logic = True
while logic:
    try:
        numSample , numStart , imgName = str(input("\nNo_Sample,Starts_with,Img_Name _,_,_ >>> ")).strip().split(',')
        if int(numSample) > 0 and int(numStart) >= 0:logic = False
        else:print("<ERROR> Not be negative or zero")
    except:
        print("<ERROR> Invalid input")


for i in range(int(numStart),int(numSample)+1):
    dirName = f"Level-{i}"
    if os.path.exists(dirName):
        shutil.rmtree("./"+dirName,ignore_errors=True)
        os.mkdir(dirName)
    else:
        os.mkdir(dirName)
#Get startFrame and endFrame
logic = True
while logic:
    try:
        start,end = str(input("\nStart and end(sec) _,_>>> ")).strip().split(',')
        if (int(start) >= 0) or (int(end) >= 0) :logic = False
        else:print("<ERROR> Invalid input")
    except:
      print("<ERROR> Invalid input")  

logic = True
while logic:
    try:
        width,height = str(input("\nWidth and height(px) _,_>>> ")).strip().split(',')
        if (int(width) >= 0) or (int(height) >= 0) :logic = False
        else:print("<ERROR> Invalid input")
    except:
        print("<ERROR> Invalid input")  
print("\n Process getting started...")

startFrame = int(start)*fps
startFrame = startFrame if startFrame != 0 else  0

endFrame = int(end)*fps
endFrame = endFrame if endFrame != 0 else  totalFrame-1

val = (endFrame - startFrame) / int(numSample)
frameCount = 0
while frameCount <= endFrame :
    ret,frame = cap.read()
    if frameCount >= startFrame:
        err = 0.5 - (1/val)
        count = frameCount - startFrame 
        print(f"\r Extracting.....{count-1} / {endFrame - startFrame -1} images",end = "\r")
        dircount = round((count /val) + err) + int(numStart) -1
        output = f"Level-{dircount}/{imgName}-{count-1}.jpg"
        resized_img = cv2.resize(frame,(int(width),int(height)))
        cv2.imwrite(output,resized_img)

    else: print(f"\r Triming.... {frameCount} / {startFrame}",end = "\r")
    frameCount += 1
print(f"\n Finished Batch processing.....\n | {count-1} images extracted into {numSample} samples |\n")









