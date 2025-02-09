class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    @property
    def width(self):
        return f"{self._width :.1f}cm"
        


    @property
    def height(self):
        return f"{self.height:.1f}cm"
    
    @width.setter
    def width(self ,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("Width Should be greater than zero")
    

    @height.setter
    def height(self ,new_height):
        if new_height>0:
            self._height=new_height
        else:
            print("Height Should be greater than zero")


    


rectangle =Rectangle(3,4)

# print(rectangle._width,rectangle._height)
print(rectangle._width)
print(rectangle._height)

        