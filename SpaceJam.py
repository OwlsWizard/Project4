from direct.showbase.ShowBase import ShowBase

import SpaceJamClasses as spaceJamClasses
import DefensePaths as defensePaths


class MyApp(ShowBase): 
    def __init__(self):
        ShowBase.__init__(self) 
        self.setupScene()
        self.setCamera()
           
                   
    def setupScene(self):
        
        """
        #LINES FOR TESTING
        self.camera.setPos(0.0, 0.0, 30000.0)
        self.camera.setHpr(0.0, -90.0, 0.0)
        self.disableMouse()
        
        
        self.camera.setPos(0.0, 0.0, 500.0)
        self.camera.setHpr(0.0, -90.0, 0.0)
        self.disableMouse()
        """
          
        self.Universe = spaceJamClasses.Universe("Universe", self.loader, self.render, 
                                                 "./Assets/Universe/Universe.x",  "./Assets/Universe/starfield-in-blue.jpg", 
                                                 (0,0,0),(0,0,0), 15000)
        
        self.Planet1 = spaceJamClasses.Planet("Planet1", self.loader, self.render, 
                                              "./Assets/Planets/protoPlanet.x",  "./Assets/Planets/gas-giant.png",
                                              (150, 5000, 67), (90,90,90), 350)
        
        self.Planet2 = spaceJamClasses.Planet("Planet2", self.loader, self.render, 
                                              "./Assets/Planets/redPlanet.x",  "./Assets/Planets/marslike.jpg", 
                                              (-150, -5000, 67), (0,0,0), 300)
        
        self.Planet3 = spaceJamClasses.Planet("Planet3", self.loader, self.render, 
                                              "./Assets/Planets/redPlanet.x",  "./Assets/Planets/rockyMoon.jpg", 
                                              (-800, -5000, 67), (0,0,0), 100)
        
        self.Planet4 = spaceJamClasses.Planet("Planet4", self.loader, self.render, 
                                              "./Assets/Planets/protoPlanet.x",  "./Assets/Planets/icyPlanet.jpg", 
                                              (5000, 150, 67), (0,0,0), (300))
        
        self.Planet5 = spaceJamClasses.Planet("Planet5", self.loader, self.render,
                                              "./Assets/Planets/protoPlanet.x",  "./Assets/Planets/redGasGiant.png", 
                                              (-5000, -150, 67), (270,90,0), (320))
        
        self.Planet6 = spaceJamClasses.Planet("Planet6", self.loader, self.render, 
                                              "./Assets/Planets/protoPlanet.x",  "./Assets/Planets/greenGasGiant.jpg", 
                                              (3000, 2500, 67), (90,90,90), (300)) 
        
        self.SpaceStation = spaceJamClasses.SpaceStation("SpaceStation", self.loader, self.render, 
                                                         "./Assets/SpaceStation/spaceStation.x",  "./Assets/SpaceStation/SpaceStation1_Dif2.png", 
                                                         (-100, -100, 20), (0,90,0), (1))
        
        self.Player = spaceJamClasses.Player("Spaceship", self.loader, self.render, 
                                             "./Assets/Spaceships/theBorg/theBorg.x",  "./Assets/Spaceships/theBorg/small_space_ship_2_color.jpg", 
                                             (0,0,0), (0,0,0), (0.75),
                                             self.taskMgr, self.render) 
        
        fullCycle = 60 #Controls num drones to spawn
        for i in range(fullCycle): #Populates drones
            self.DrawCloudDefense(self.Planet1, 500)
            
            self.DrawBaseballSeams(self.Planet4, i, fullCycle)
            
            circlePosition = i / float(fullCycle)
            self.DrawXYRing(self.SpaceStation, circlePosition, 50)
            self.DrawYZRing(self.SpaceStation, circlePosition, 50)
            self.DrawXZRing(self.SpaceStation, circlePosition, 50)
                     
                     
    def DrawCloudDefense(self, centralObject, radius):
        droneName = self.UpdateDroneCount()
        unitVec = defensePaths.cloud()
        unitVec.normalize()
        position = unitVec * radius + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(droneName, self.loader, self.render, 
                            "./Assets/Spaceships/DroneDefender/DroneDefender.x", "./Assets/Spaceships/DroneDefender/octotoad1_auv.png", 
                            position, (0,0,0), 10)     
        
    def DrawBaseballSeams(self, centralObject, step, numSeams, radius = 1):
        droneName = self.UpdateDroneCount()
        unitVec = defensePaths.baseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 500 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(droneName, self.loader, self.render, 
                            "./Assets/Spaceships/DroneDefender/DroneDefender.x", "./Assets/Spaceships/DroneDefender/octotoad1_auv.png", 
                            position, (0,0,0), 5)    
      
    def DrawXYRing(self, centralObject, position, radius):
        droneName = self.UpdateDroneCount()
        unitVecXY = defensePaths.XYRing(position)
        unitVecXY.normalize()
        positionXY = unitVecXY * radius + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(droneName, self.loader, self.render, 
                "./Assets/Spaceships/DroneDefender/DroneDefender.x", "./Assets/Spaceships/DroneDefender/octotoad1_auv.png", 
                positionXY, (0,0,0), 1)

    def DrawYZRing(self, centralObject, position, radius):
        droneName = self.UpdateDroneCount()
        unitVecYZ = defensePaths.YZRing(position)
        unitVecYZ.normalize()
        positionYZ = unitVecYZ * radius + centralObject.modelNode.getPos()
        
        spaceJamClasses.Drone(droneName, self.loader, self.render, 
                    "./Assets/Spaceships/DroneDefender/DroneDefender.x", "./Assets/Spaceships/DroneDefender/octotoad1_auv.png", 
                    positionYZ, (0,0,0), 1)

    def DrawXZRing(self, centralObject, position, radius):
        droneName = self.UpdateDroneCount()
        unitVecXZ = defensePaths.XZRing(position)
        unitVecXZ.normalize()
        positionXZ = unitVecXZ * radius + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(droneName, self.loader, self.render, 
                    "./Assets/Spaceships/DroneDefender/DroneDefender.x", "./Assets/Spaceships/DroneDefender/octotoad1_auv.png", 
                    positionXZ, (0,0,0), 1) 
        
    def UpdateDroneCount(self):
        spaceJamClasses.Drone.droneCount += 1
        nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
        return nickName
    
    
    def setCamera(self):
        self.disableMouse()
        self.camera.reparentTo(self.Player.modelNode)
        self.camera.setFluidPos(0,1, 0)#sets camera to ship cockpit    
                
#main        
app = MyApp()
app.run()