# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "rSelection",
    "author": "Paweł Łyczkowski",
    "version": (0, 1),
    "blender": (2, 70, 0),
    "location": "View3D",
    "description": "Modifies the selection method.",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"}

import bpy

addon_keymaps = []

def kmi_props_setattr(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except AttributeError:
        print("Warning: property '%s' not found in keymap item '%s'" %
              (attr, kmi_props.__class__.__name__))
    except Exception as e:
        print("Warning: %r" % e)
        
#------------------- REGISTER ------------------------------     

def register():
    
    # Set Preferences
    bpy.context.user_preferences.inputs.select_mouse = 'LEFT'

    #----KEYMAP----
    wm = bpy.context.window_manager

    if True:
            view3d_km_items = wm.keyconfigs.default.keymaps['3D View'].keymap_items
            for j in view3d_km_items:
                if j.name == 'Activate/Select':
                   j.active = False
   
    #----EDIT MODE----
    
    km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
    addon_keymaps.append(km)

    #Element Select Modes
    kmi = km.keymap_items.new('mesh.select_mode', 'ONE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'type', 'VERT')
    kmi = km.keymap_items.new('mesh.select_mode', 'TWO', 'PRESS')
    kmi_props_setattr(kmi.properties, 'type', 'EDGE')
    kmi = km.keymap_items.new('mesh.select_mode', 'THREE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'type', 'FACE')

    #Select Linked
    kmi = km.keymap_items.new('mesh.select_linked_pick', 'SELECTMOUSE', 'DOUBLE_CLICK')
    kmi_props_setattr(kmi.properties, 'limit', True)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi = km.keymap_items.new('mesh.select_linked_pick', 'SELECTMOUSE', 'DOUBLE_CLICK', shift=True)
    kmi_props_setattr(kmi.properties, 'limit', True)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi = km.keymap_items.new('mesh.select_linked_pick', 'SELECTMOUSE', 'DOUBLE_CLICK', ctrl=True)
    kmi_props_setattr(kmi.properties, 'limit', True)
    kmi_props_setattr(kmi.properties, 'deselect', True)
    
    #----OBJECT MODE----

    km = bpy.context.window_manager.keyconfigs.addon.keymaps.new('3D View', space_type='VIEW_3D', region_type='WINDOW', modal=False)
    addon_keymaps.append(km)

    kmi = km.keymap_items.new('view3d.select_or_deselect_all', 'SELECTMOUSE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', False)
    kmi_props_setattr(kmi.properties, 'center', False)
    kmi_props_setattr(kmi.properties, 'enumerate', False)
    kmi_props_setattr(kmi.properties, 'object', False)
    
    kmi = km.keymap_items.new('view3d.select_or_deselect_all', 'SELECTMOUSE', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', True)
    kmi_props_setattr(kmi.properties, 'center', False)
    kmi_props_setattr(kmi.properties, 'enumerate', False)
    kmi_props_setattr(kmi.properties, 'object', False)
    
    kmi = km.keymap_items.new('view3d.select_or_deselect_all', 'SELECTMOUSE', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', True)
    kmi_props_setattr(kmi.properties, 'toggle', False)
    kmi_props_setattr(kmi.properties, 'center', False)
    kmi_props_setattr(kmi.properties, 'enumerate', False)
    kmi_props_setattr(kmi.properties, 'object', False)
    
    kmi = km.keymap_items.new('view3d.select_or_deselect_all', 'SELECTMOUSE', 'PRESS', alt=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', False)
    kmi_props_setattr(kmi.properties, 'center', False)
    kmi_props_setattr(kmi.properties, 'enumerate', True)
    kmi_props_setattr(kmi.properties, 'object', False)
    
    kmi = km.keymap_items.new('view3d.select_or_deselect_all', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', True)
    kmi_props_setattr(kmi.properties, 'center', True)
    kmi_props_setattr(kmi.properties, 'enumerate', False)
    kmi_props_setattr(kmi.properties, 'object', False)
    
    kmi = km.keymap_items.new('view3d.select_or_deselect_all', 'SELECTMOUSE', 'PRESS', ctrl=True, alt=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', False)
    kmi_props_setattr(kmi.properties, 'center', True)
    kmi_props_setattr(kmi.properties, 'enumerate', True)
    kmi_props_setattr(kmi.properties, 'object', False)
    
    kmi = km.keymap_items.new('view3d.select_or_deselect_all', 'SELECTMOUSE', 'PRESS', shift=True, alt=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', True)
    kmi_props_setattr(kmi.properties, 'center', False)
    kmi_props_setattr(kmi.properties, 'enumerate', True)
    kmi_props_setattr(kmi.properties, 'object', False)
    
    kmi = km.keymap_items.new('view3d.select_or_deselect_all', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True, alt=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', True)
    kmi_props_setattr(kmi.properties, 'center', True)
    kmi_props_setattr(kmi.properties, 'enumerate', True)
    kmi_props_setattr(kmi.properties, 'object', False)

    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY')
    kmi_props_setattr(kmi.properties, 'extend', False)

    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY', shift=True)
    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY', ctrl=True)
    kmi_props_setattr(kmi.properties, 'extend', False)

    kmi = km.keymap_items.new('view3d.manipulator', 'SELECTMOUSE', 'PRESS', any=True)
    kmi_props_setattr(kmi.properties, 'release_confirm', True)

    # Map Gesture Border
    km = bpy.context.window_manager.keyconfigs.addon.keymaps.new('Gesture Border', space_type='EMPTY', region_type='WINDOW', modal=True)
    addon_keymaps.append(km)

    kmi = km.keymap_items.new_modal('CANCEL', 'ESC', 'PRESS', any=True)
    kmi = km.keymap_items.new_modal('BEGIN', 'LEFTMOUSE', 'PRESS')
    kmi = km.keymap_items.new_modal('SELECT', 'LEFTMOUSE', 'RELEASE')
    kmi = km.keymap_items.new_modal('SELECT', 'LEFTMOUSE', 'RELEASE', shift=True)
    kmi = km.keymap_items.new_modal('DESELECT', 'LEFTMOUSE', 'RELEASE', ctrl=True)

def unregister():

    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()

    if True:
            view3d_km_items = wm.keyconfigs.default.keymaps['3D View'].keymap_items
            for j in view3d_km_items:
                if j.name == 'Activate/Select':
                   j.active = True
        
if __name__ == "__main__":
    register()