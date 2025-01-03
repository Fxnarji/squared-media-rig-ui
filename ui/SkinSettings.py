import bpy
from ..utils import get_material_object, is_packed
from .. import properties

rigID = properties.RigProperties.rigID
category = properties.UIProperties.category


def eye_settings(self, context, Eye, ParentBox, name):
    rig = bpy.context.active_object

    ParentBox.label(text=name, icon = "HIDE_OFF")
    row = ParentBox.column(align=True)

    row.prop(rig.pose.bones["Settings"],'["Eye Offset"]',expand = True, index = 1 if name == "Right" else 0)

    row = ParentBox.row()
    row.prop(Eye[0], "default_value", text = Eye[0].name)
    
    row = ParentBox.row()
    row.prop(Eye[1], "default_value", text =Eye[1].name)
    
    row = ParentBox.row()
    row.prop(Eye[2], "default_value", text =Eye[2].name)
    
    row = ParentBox.row()
    row.prop(Eye[3], "default_value", text = Eye[3].name, toggle = True)

    row = ParentBox.row()
    row.prop(Eye[4], "default_value", text = Eye[4].name)

def advanced_eye_settings(self, context, EyeR, ParentBox, name):
          #Advanced Settings

    ParentBox.label(text=name, icon = "HIDE_OFF")
    col = ParentBox.column()

    Pupil = col.box()
    Pupil.label(text="Pupil")
    Pupil = Pupil.column(align=True)
    Pupil.prop(EyeR[5], "default_value", text = EyeR[5].name)
    Pupil.prop(EyeR[6], "default_value", text = EyeR[6].name)
    Pupil.prop(EyeR[7], "default_value", text = EyeR[7].name)
    Pupil.prop(EyeR[8], "default_value", text = EyeR[8].name)
#
    Pupil.label(text="Iris")
    Pupil.prop(EyeR[9], "default_value", text = EyeR[9].name)
#
#
    Reflection = col.box()
    Reflection.label(text="Reflection")
    Reflection = Reflection.column(align=True)
#
    Reflection.prop(EyeR[12], "default_value", text = EyeR[12].name)
    Reflection.prop(EyeR[13], "default_value", text = EyeR[13].name)
    
    row = Reflection.row()
    row = row.split(factor=0.5)
    row.label(text="Rotation")
    row.prop(EyeR[14], "default_value", text = "")


def draw_eyebrows(self,context,Parentbox):
     rig = bpy.context.active_object

def draw_skin_settings(self, context):
    rig = bpy.context.active_object
    Mat_obj = get_material_object(rig)
    
    layout = self.layout

    if Mat_obj is None:
            Errorbox = layout.box()
            Errorbox.label(text="ERROR: No material object found")
            return

    #face settings
    FaceBox = layout.box()
    FaceBox.label(text="Face")
    FaceBox.prop(rig.pose.bones["MCH-FaceSlider"],"location", text= "Face position", index = 1, toggle = True)  
    FaceBox.prop(rig.pose.bones["MCH-Eyebrows"],"location", text= "Eyebrow position", index = 2, toggle = True)    
    FaceBox.prop(rig.pose.bones["MCH-Eyes"],"location", text= "Eye position", index = 1, toggle = True) 
    FaceBox.prop(rig.pose.bones["MCH-Mouth"],"location", text= "Mouth position", index = 2, toggle = True)   
    
    #Proportions
    ProportionsBox = layout.box()
    ProportionsBox.label(text="Proportions")

    row = ProportionsBox.row()
    col = row.column(align=True)
    col.prop(rig.pose.bones["MCH-ScaleOffset-Eye.R"],"scale",index= 0, toggle = True, text = "Eye R Width")
    col.prop(rig.pose.bones["MCH-ScaleOffset-Eye.R"],"scale",index= 1, toggle = True, text = "Eye R Height")

    col = row.column(align=True)
    col.prop(rig.pose.bones["MCH-ScaleOffset-Eye.L"],"scale",index= 0, toggle = True, text = "Eye L Width")
    col.prop(rig.pose.bones["MCH-ScaleOffset-Eye.L"],"scale",index= 1, toggle = True, text = "Eye L Height")    

    row = ProportionsBox.row()
    col = row.column(align=True)
    col.prop(rig.pose.bones["MCH-ScaleOffset-Eyebrow.L"],"scale",index= 0, toggle = True, text = "Eyebrow Width")
    col.prop(rig.pose.bones["MCH-ScaleOffset-Eyebrow.L"],"scale",index= 1, toggle = True, text = "Eyebrow Thick")
    col.prop(rig.pose.bones["MCH-ScaleOffset-Eyebrow.L"],"scale",index= 2, toggle = True, text = "Eyebrow Height")

    col = row.column(align=True)
    col.prop(rig.pose.bones["MCH-ScaleOffset-Eyebrow.R"],"scale",index= 0, toggle = True, text = "Eyebrow Width")
    col.prop(rig.pose.bones["MCH-ScaleOffset-Eyebrow.R"],"scale",index= 1, toggle = True, text = "Eyebrow Thick")
    col.prop(rig.pose.bones["MCH-ScaleOffset-Eyebrow.R"],"scale",index= 2, toggle = True, text = "Eyebrow Height")
    
    #Eyebrows
    EyebrowBox = layout.box()
    EyebrowBox.label(text="Eyebrows")
    row = EyebrowBox.row()
    row.prop(rig.pose.bones["Settings"],'["Eyebrow_R_enabled"]', text="Eyebrow R", toggle = True)
    row.prop(rig.pose.bones["Settings"],'["Eyebrow_L_enabled"]', text="Eyebrow L", toggle = True)
    draw_eyebrows(self, context, EyebrowBox)

   
    
    #Eye Settings
    ColorBox = layout.box()
    ColorBox.label(text="Eye Settings")
    row = ColorBox.row()
    row.prop(rig.pose.bones["Settings"],'["Eye_R_enable"]', text="Eye R", toggle=True)
    row.prop(rig.pose.bones["Settings"],'["Eye_L_enable"]', text="Eye L", toggle=True)


    Eye = ColorBox.row()

    if rig.pose.bones["Settings"]["Eye_R_enable"] and rig.pose.bones["Settings"]["Eye_L_enable"]:
        Eye = Eye.split(factor=0.5)
    
    EyeRBox = Eye.box()
    EyeLBox = Eye.box()

    EyeAdvanced = ColorBox.box()

    EyeAdvanced.prop(rig.pose.bones["Settings"],'["EyeAdvanced"]', toggle = True, icon = "DOWNARROW_HLT" if rig.pose.bones["Settings"]["EyeAdvanced"] else "RIGHTARROW", emboss = False, text = "Advanced Eye Settings")
    if rig.pose.bones["Settings"]["Eye_R_enable"] and rig.pose.bones["Settings"]["Eye_L_enable"]:
        EyeAdvanced = EyeAdvanced.split(factor=0.5)



    #Right Eye 
    if rig.pose.bones["Settings"]["Eye_R_enable"]:
        EyeR = Mat_obj.material_slots[1].material.node_tree.nodes["Eye.R"].inputs
        eye_settings(self, context, EyeR, EyeRBox, "Right")
        if rig.pose.bones["Settings"]["EyeAdvanced"]:
            EyeAdvancedR = EyeAdvanced.box()
            advanced_eye_settings(self, context, EyeR, EyeAdvancedR, "Right")
    else:
         EyeRBox.label(text="disabled")


    #Left Eye
    if rig.pose.bones["Settings"]["Eye_L_enable"]:
        EyeL = Mat_obj.material_slots[2].material.node_tree.nodes["Eye.L"].inputs
        eye_settings(self, context, EyeL, EyeLBox, "Left")
        if rig.pose.bones["Settings"]["EyeAdvanced"]:
            EyeAdvancedL = EyeAdvanced.box()
            advanced_eye_settings(self, context, EyeL, EyeAdvancedL, "Left")
    else:
        EyeLBox.label(text="disabled")

    
    

    
    #mouth
    MouthBox = layout.box()
    MouthBox.label(text="Mouth")
    MouthBox.prop(rig.pose.bones["Settings"],'["Mouth_enable"]', toggle = True)



        




    # Second Skin Layer
    SecondLayerBox = layout.box()
    SecondLayerBox.label(text="Second Layer")
    left = SecondLayerBox.row(align=True)
    left.prop(rig.pose.bones["Settings"], '["Skin Layer 02"]', toggle=True, text = "Viewport", icon ="RESTRICT_VIEW_OFF")
    right = left.row(align=True)
    right.prop(rig.pose.bones["Settings"], '["Skin Layer 02 Render"]', toggle=True , text = "Render", icon = "RESTRICT_RENDER_OFF")


    #Texture Box
    TexutureBox = layout.box()
    TexutureBox.label(text="Skin Texture")
    img = Mat_obj.material_slots[0].material.node_tree.nodes["SkinTexture"].image

    left = TexutureBox.row(align=True)
    left.operator("squaredmedia.imgpack", icon="PACKAGE").id_name = img.name

    main = left.row(align=True)
    main.enabled = not is_packed(img)
    main.prop(img, "filepath", text="")
    main.operator("squaredmedia.imgreload", icon="FILE_REFRESH").id_name = img.name   