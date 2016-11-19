# Blender Custom User Preferences

To find out where Blender user preferences are stored on your machine run the following command in its Python Console.

```
bpy.utils.user_resource('CONFIG')
```

This should be something along these lines:
```
// Linux
~/.config/blender

// Mac
/Users/username/Library/Application Support/Blender/

// Windows
%APPDATA%\Roaming\Blender Foundation\Blender
```

Within, sub-folders correspond to the versions of Blender that have been used on the machine: `2.77`, `2.78`, et cetera. Focus on the folder for your current version. Within each version folder the `config` directory should contain `startup.blend` and `userpref.blend`, the files that store user preferences. The path should be similar to `/Users/username/Library/Application Support/Blender/2.78/config/`.

To copy these settings to your machine, replace those files with these:
* [startup.blend](startup.blend)
* [userpref.blend](userpref.blend)

Or for only the input settings (key configuration), open the User Preferences Window. Navigate to the Input tab, click the Import Key Configuration button, and open this file:
* [keyconfig.py](keyconfig.py)

___

Documentation of changes to the standard user preferences. A `✓` next to an item indicates that it is now enabled (standard setting was disabled). A `☐` next to an item indicates that it is disabled (standard setting was enabled). An `X` is an option that may not always be necessary, but should be noted for possible activation. Items within brackets (`[]`) reference a standard setting; a correlating custom setting will be indicated. Settings with quotation blocks are under consideration or in a trial period.

## Changes made within the User Preferences window:

### Interface

![Interface Preferences](assets/interface-prefs.png)

#### Display

✓ Global Scene

#### View Manipulation

✓ Auto Depth

✓ Zoom To Mouse Position

☐ Manipulator

___

### Editing

___

### Input

Select With: Left

#### View2D


#### 3D View

##### 3D View (Global)

Context Toggle Values [Alt Z]: Change first value to `TEXTURED`, second to `MATERIAL`.

![Toggle Material Shading Mode](assets/input-toggle-material-shading.png)

☐ Rotate View [Mouse/Trackpad Pan]

Zoom View [Mouse/Trackpad Zoom]: Mouse/Trackpad Pan

___

### Add-ons

✓ Node Wrangler

X [Animation Nodes](https://github.com/JacquesLucke/animation_nodes)

X [Sverchok](https://github.com/nortikin/sverchok)
___

### Themes

___

### File

___

### System

Images Draw Method [2D Texture]: GLSL

___

## Changes made within the GUI:

### Info Window

Render Engine [Blender Render]: Cycles Render
