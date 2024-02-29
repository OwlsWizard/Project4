from panda3d.core import PandaNode, Loader, NodePath, CollisionNode, CollisionSphere, CollisionInvSphere, CollisionCapsule, Vec3

#LEAVE ALL DEBUG Messages around

class PlacedObject():
    #Generic node for Placed object
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        self.modelNode: NodePath = loader.loadModel(modelPath)
        
        #if modelnode is not a nodePath. Not strictly needed, but can help with troubleshooting
        if not isinstance(self.modelNode, NodePath):
            raise AssertionError("PlacedObject loader.loadModel(" + modelPath + ") did not return a proper PandaModel")
        
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setName(nodeName)
        
        
class CollidableObject(PlacedObject):
    #adds colliders to PlacedObject
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        super(CollidableObject, self).__init__(loader, modelPath, parentNode, nodeName)
        
        self.collisionNode = self.modelNode.attachNewNode(CollisionNode(nodeName + "_cNode"))#Adds a collider to the object
        #self.collisionNode.show() 
    
class InverseSphereCollideObj(CollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, colPositionVec: Vec3, colRadius: float):
        super(InverseSphereCollideObj, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionInvSphere(colPositionVec, colRadius))
        #self.collisionNode.show
        
class CapsuleCollidableObject(CollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, ax:float, ay:float, bx:float, by:float, bz:float, r:float):
        super(CapsuleCollidableObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().add_solid(CollisionCapsule(ax,ay,bx,by,bz,r))
        #self.collisionNode.show()
             