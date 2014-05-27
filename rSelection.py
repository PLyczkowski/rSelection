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
    "version": (0.1),
    "blender": (2, 71, 0),
    "location": "View3D",
    "description": "Modifies the selection method.",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"}

import bpy
        
#------------------- REGISTER ------------------------------     

def register():

    wm = bpy.context.window_manager
    
    #----EDIT MODE----
    
    km = wm.keyconfigs.addon.keymaps.new(name='Edit Mode', space_type='EMPTY')

    #Element Select Modes
    kmi = km.keymap_items.new('mesh.select_mode', 'ONE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'type', 'VERT')
    kmi = km.keymap_items.new('mesh.select_mode', 'TWO', 'PRESS')
    kmi_props_setattr(kmi.properties, 'type', 'EDGE')
    kmi = km.keymap_items.new('mesh.select_mode', 'THREE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'type', 'FACE')
    
    #----OBJECT MODE----
    
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    
    kmi = km.keymap_items.new('view3d.select', 'LEFTMOUSE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', False)
    kmi_props_setattr(kmi.properties, 'center', False)
    kmi_props_setattr(kmi.properties, 'enumerate', False)
    kmi_props_setattr(kmi.properties, 'object', False)
    kmi = km.keymap_items.new('view3d.select', 'SELECTMOUSE', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', True)
    kmi_props_setattr(kmi.properties, 'center', False)
    kmi_props_setattr(kmi.properties, 'enumerate', False)
    kmi_props_setattr(kmi.properties, 'object', False)
    kmi = km.keymap_items.new('view3d.select', 'SELECTMOUSE', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', False)
    kmi_props_setattr(kmi.properties, 'center', True)
    kmi_props_setattr(kmi.properties, 'enumerate', False)
    kmi_props_setattr(kmi.properties, 'object', True)
    kmi = km.keymap_items.new('view3d.select', 'SELECTMOUSE', 'PRESS', alt=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', False)
    kmi_props_setattr(kmi.properties, 'center', False)
    kmi_props_setattr(kmi.properties, 'enumerate', True)
    kmi_props_setattr(kmi.properties, 'object', False)
    kmi = km.keymap_items.new('view3d.select', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', True)
    kmi_props_setattr(kmi.properties, 'center', True)
    kmi_props_setattr(kmi.properties, 'enumerate', False)
    kmi_props_setattr(kmi.properties, 'object', False)
    kmi = km.keymap_items.new('view3d.select', 'SELECTMOUSE', 'PRESS', ctrl=True, alt=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', False)
    kmi_props_setattr(kmi.properties, 'center', True)
    kmi_props_setattr(kmi.properties, 'enumerate', True)
    kmi_props_setattr(kmi.properties, 'object', False)
    kmi = km.keymap_items.new('view3d.select', 'SELECTMOUSE', 'PRESS', shift=True, alt=True)
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi_props_setattr(kmi.properties, 'deselect', False)
    kmi_props_setattr(kmi.properties, 'toggle', True)
    kmi_props_setattr(kmi.properties, 'center', False)
    kmi_props_setattr(kmi.properties, 'enumerate', True)
    kmi_props_setattr(kmi.properties, 'object', False)
    kmi = km.keymap_items.new('view3d.select', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True, alt=True)
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

    # Map Gesture Border
    km = kc.keymaps.new('Gesture Border', space_type='EMPTY', region_type='WINDOW', modal=True)

    kmi = km.keymap_items.new_modal('CANCEL', 'ESC', 'PRESS', any=True)
    kmi = km.keymap_items.new_modal('BEGIN', 'LEFTMOUSE', 'PRESS')
    kmi = km.keymap_items.new_modal('SELECT', 'LEFTMOUSE', 'RELEASE')
    kmi = km.keymap_items.new_modal('SELECT', 'LEFTMOUSE', 'RELEASE', shift=True)
    kmi = km.keymap_items.new_modal('DESELECT', 'LEFTMOUSE', 'RELEASE', ctrl=True)
    
    
    addon_keymaps.append(km)


def unregister():

    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
        
if __name__ == "__main__":
    register()
    


