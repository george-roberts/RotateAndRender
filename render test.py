#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, math, traceback

renderPath = "D:\\"
steps = 4

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        doc = app.activeDocument
        
        design = adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
        view = app.activeViewport
        camera = view.camera
        startEye = camera.eye
        step = math.pi*2/steps
        rotX = adsk.core.Matrix3D.create()    
        rotX.setToRotation(math.radians(step), adsk.core.Vector3D.create(0,0,1), adsk.core.Point3D.create(0,0,0))
        renderManager = design.renderManager
        renderManager.sceneSettings.isDepthOfFieldEnabled = False
        renderManager.sceneSettings.isGroundDisplayed = False
        renderManager.activateRenderWorkspace()
        for i in range(0,steps):
            newEye = startEye
            newEye.transformBy(rotX)
            camera.eye = newEye
            camera.target = adsk.core.Point3D.create(0,0,0)
            camera.upVector = adsk.core.Vector3D.create(0,0,1)
            view.camera = camera
            view.refresh()
            renderManager.rendering.startLocalRender(renderPath + str(i) + ".png")
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
