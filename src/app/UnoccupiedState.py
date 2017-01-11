'''
Created on 30 Dec 2016

@author: chrisdoherty
'''

class UnoccupiedState():        
    # Interval to check for between detections (Seconds)
    max_detection_interval_ = 10
    
    # Number of back to back detections with "interval" or less between
    # them before we trigger the next state.
    required_consecutive_detections_ = 5
    
    # The number of detections currently identified with an "interval" or less between
    # them
    consecutive_detection_count_ = 0
    
    # Function to call when the state is ready for change
    occupied_callback_ = None
    
    # The previous detection we received.
    previous_detection_ = None
    
    # Are we, or aren't we handling detections?
    handle_detections_ = False
    
    # Initialises internal variables.
    def __init__(self,  max_detection_interval, required_consecutive_detections, occupied_callback):        
        print "UnoccupiedState: initialised (max_detection_interval=%s, required_consecutive_detections=%s)" % (max_detection_interval, required_consecutive_detections)
        
        self.max_detection_interval_ = max_detection_interval
        self.required_consecutive_detections_ = required_consecutive_detections
        self.occupied_callback_ = occupied_callback
    
    # A method called when a new detection is ready to be processed. Essentially a callback
    # for the detection manager.
    def new_detection(self, detection):
        if self.handle_detections_: 
            print "UnoccupiedState: new detection"
            current_detection = detection
            
            if self.previous_detection_ == None:
                print "UnoccupiedState: first detection set"
                self.previous_detection_ = detection
                return
            elif (current_detection.start - self.previous_detection_.end) > self.max_detection_interval_:
                print "UnoccuepiedState: interval too short, resetting consecutive detection count"
                self.consecutive_detection_count_ = 0
            else:
                print "UnoccupiedState: consecutive detection count increased"
                self.consecutive_detection_count_+= 1
                            
            if self.consecutive_detection_count_ >= self.required_consecutive_detections_:
                print "UnoccupiedState: activation count equal to threshold, triggering change state"
                self.occupied_callback_()
                
            self.previous_detection_ = current_detection
            
    # Stop/start handling the detections
    def handle_detections(self, status):
        self.handle_detections_ = status 
            