#Created by: Alireza Teimoori
#Created on: 25 Sep 2017
#Created for: ICS3UR-1
#Lesson: Unit 1-04
#This program gets a radius and calculates circumference

import ui

def calculate_circumferenece(sender):
    #calculate circumference
    
    #input
    radius = int(view['radius_text_field'].text)
    
    #process
    circumference=2*3.14*radius
    
    #output
    view['answer_lable'].text = "Circumference is: " + str(circumference) + "cm"
view = ui.load_view()
view.present('sheet')
