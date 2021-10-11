
This program loads an image and build it in 3d enviroment

imports
import bpy
from simpleimage import SimpleImage
import colorsys

def main()
    image = SimpleImage('imagesthat1.png')
    width = image.width
    height = image.height
    nx=0
    print(looppixels(image,height,width,nx)) 

def looppixels(image,height,width,nx)
    for y in range(height)
        for x in range(width)  
            nx+=1
            pixel = image.get_pixel(x,y)
            clrs=((pixel.red255),(pixel.green255),(pixel.blue255))
            to_hsv=(colorsys.rgb_to_hsv(clrs[0],clrs[1],clrs[2]))
            makes a dict
            keys=(hsv_h,hsv_s,hsv_v)
            color_dic = dict(zip(keys, (clrs)))
            print(color_dic)
            print(colorsys.rgb_to_hsv(1,1,1));
            mcube(y,x,color_dic,nx)

            

            
        
def mcube(y,x,color_dic,nx)
    
    pass in location info and hsv color 
    make a cube with the color or make a cube create the color asing it 
    
    bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location=((x2), (-abs(y2)),0 ), scale=(1, 1, 1))
    obj = bpy.context.selected_objects
    mname=(obje+str(nx))
    obj[0].name=mname
    newmat = bpy.data.materials.new(mname)
    newmat.diffuse_color = (color_dic[hsv_h], color_dic[hsv_s], color_dic[hsv_v],200)
    obj[0].data.materials.append(newmat)






if __name__ == '__main__'
    main()