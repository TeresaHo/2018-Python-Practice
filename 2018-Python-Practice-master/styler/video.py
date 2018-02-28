import cv2

from styler.utils import resize


class Video:

    def __init__(self, path):
        self.path = path
        self.cap = cv2.VideoCapture(self.path)
        self.frames = []

    def __enter__(self):
        if not self.cap.isOpened():
            raise Exception('Cannot open video: {}'.format(self.path))
        return self

    def __len__(self):
        return len(self.frames)

    def read_frames(self, image_h, image_w):
        '''
        5.
         - Read video frames from `self.cap` and collect frames into list
         - Apply `resize()` on each frame before add it to list
         - Also assign frames to "self" object
         - Return your results
        '''
        # 5-1 /5-2 Read video and collect them
        
        
        # Read until video is completed
        while(self.cap.isOpened()):       
            ret, frame = self.cap.read()
            if ret == True: 
                frame_r=resize(frame,image_h,image_w)
                cv2.imshow('Frame',frame)
                self.frames.append(frame_r)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else :
                break
                
        # Press Q on keyboard to  exit
            
            
        # When everything done, release the video capture object
        
        # Closes all the frames
        cv2.destroyAllWindows()
        

        #self.frames = ...  # 5-3 let object have the result
        return self.frames  # return your results

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cap.release()
