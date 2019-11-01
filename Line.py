class Line:
  def __init__(self,point1,point2):
    self.higher = max(point1,point2)
    self.lower = min(point1,point2)
    pass
  
  #check if a line overlaps with another line object
  def overLap(self,line):
    if (line.lower<=self.higher and line.lower>self.lower) or (line.higher>self.lower and line.higher<=self.higher):
      return True

    else:
      return False
    
    
