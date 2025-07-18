import bpy

class FILE_OT_NameCharacter(bpy.types.Operator):
    bl_idname = "squaredmedia.namecharacter"
    bl_label = "FILE_OT_NameCharacter"
    bl_options = {'REGISTER', 'UNDO'}


    new_name: bpy.props.StringProperty(name="New Name:")

    def switch_names(self, context):
        rig = bpy.context.active_object
        DataBone = rig.data.bones["Data_Obj"]
        DataBone["OldName"] = DataBone["Name"]
        DataBone["Name"] = self.new_name


    def rename_collections(self, collection, context):
        for col in bpy.data.collections:
                    col.name = self.rename(context, col.name)

    def rename_objects_in_collection(self, collection, context):
        data = collection.all_objects
        for d in data:
            d.name = self.rename(context,name = d.name)

    def rename(self, context, name):
            rig = bpy.context.active_object
            DataBone = rig.data.bones["Data_Obj"]
            Name = DataBone["Name"]
            OldName = DataBone["OldName"]

            prefix = f"{OldName}"
            if not name.startswith(prefix):
                return name

            first_half = name[:(len(prefix))]
            second_half = name[(len(prefix)):]

            new_name = f"{Name}{second_half}" 
            print(new_name)
            return new_name


    def invoke(self, context, event):
        # Trigger the file dialog
        context.window_manager.invoke_props_dialog(self)
        return {'RUNNING_MODAL'}


    

    def execute(self, context):
        rig = bpy.context.active_object
        DataBone = rig.data.bones["Data_Obj"]
        Collection = DataBone["Collection"]

        self.switch_names(context)
        self.rename_objects_in_collection(context = context, collection=Collection)
        self.rename_collections(context=context, collection=Collection)

        return {"FINISHED"}

