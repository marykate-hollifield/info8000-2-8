class CylinderBucket:
    def __init__(self,height_cm,radius_cm):
        # Input: height and radius of the cylinder
        # Side Effect: an initialized cylinder, with properties height, radius
        #Output: None
        self.maxvolume_cm3 = 22/7*(self.radius_cm**2)*self.height_cm
        self.height_cm = height_cm
        self.radius_cm = radius_cm
        self.currentheight = self.height_cm
        self.area = 22/7*self.radius_cm**2
        pass

    def fill(self,quantity_cm3):
        # Input: a volume of water to fill the bucket with
        # Output: the amount of water put in, less any that spilled over
        #Convert volume to height

        height = quantity_cm3/self.area

        #self.quantity_cm3 += quantity_cm3

    if self.currentheight + height_cm > self.height_cm:
        height_over = self.currentheight + height - self.height
        volume_over = height_over*self.area
        self.currentheight = self.height
        return quantity_cm3 = volume_over
    else:
        self.currentheight += height 
        return quantity_cm3





        if self.quantity > self.maxvolume_cm3:
            return self.maxvolume_cm3
        self.
        pass
    def fill_level(self):
        # Input: None
        # Output: height of the water so far
        pass

