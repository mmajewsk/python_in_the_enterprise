import random
import time
import optparse

class Plane:
    def __init__(self, range_of_tilt=(-5,5)):
        self.minima, self.maxima = range_of_tilt
        self.middle = (self.minima+self.maxima)/2
        self.orientation = 0
        
    def tilt(self):
        return random.gauss(self.middle,self.middle-self.maxima) 
    
    def fly(self, fly_range):
        for _ in fly_range:
            self.orientation = self.orientation + self.tilt()
            yield True
    
class FlightCorrectorSimulator:
    def __init__(self, plane):
        self.plane = plane
        
    def simulate(self,iterator):
        for sim_step in self.plane.fly(iterator):
            if sim_step:
                tilt_correction = -self.plane.orientation
                self.plane.orientation = self.plane.orientation + tilt_correction
                print "tilt corrected by:"+str(tilt_correction)
                print "current orientation"+str(self.plane.orientation)
                print ""
            else:
                raise Except
                
    @staticmethod
    def timed_while_iterator(waittime_s = 2 ):
        while True:
        	try:
	            time.sleep(waittime_s)
	            yield True
	        except KeyboardInterrupt:
    			print 'landing!'
    			break

if __name__ == "__main__":
	usage="\nexit by ctrl-c \nyou must specify -w \nuse -h to view help"
	parser = optparse.OptionParser(usage=usage)
	parser.add_option("-w",dest="waittime",type="int",help = "-w waittime_in_seconds")
	opts, args = "",""
	try:
		opts, args = parser.parse_args()
		p = Plane()
		fs = FlightCorrectorSimulator(p)
		fs.simulate(fs.timed_while_iterator(opts.waittime))
	except:
		parser.print_usage()
