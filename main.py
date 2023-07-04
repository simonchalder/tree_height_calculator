from math import sin, cos, tan, radians
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 1
        self.spacing = 10

        self.inside = GridLayout()
        self.inside.cols = 2
        self.spacing = 10

        self.inside.add_widget(Label(bold = True, text="Distance (m):" ))
        self.distance = TextInput(multiline=False, halign="center", padding=25)
        self.inside.add_widget(self.distance)

        self.inside.add_widget(Label(bold = True, text="Base Angle: "))
        self.angle1 = TextInput(multiline=False, halign="center", padding=25)
        self.inside.add_widget(self.angle1)

        self.inside.add_widget(Label(bold = True, text="Top Angle: "))
        self.angle2 = TextInput(multiline=False, halign="center", padding=25)
        self.inside.add_widget(self.angle2)

        self.add_widget(self.inside)

        self.calculate = Button(text="Calculate", bold = True, background_normal = "", background_color = "#336600", size_hint = (0.5, 0.4))
        self.calculate.bind(on_press=self.buttonPress)
        self.add_widget(self.calculate)

        self.result = Label(bold = True, text = "")
        self.add_widget(self.result)

    def buttonPress(self, instance):
        ob = float(self.distance.text)
        base_angle = float(self.angle1.text)
        top_angle = float(self.angle2.text)

        if base_angle < 0: # observer is higher than tree base (base angle is negative)
            base_angle = 360 + base_angle
            base_angle = radians(base_angle)
            top_angle = radians(top_angle)
            oc = ob * (cos(base_angle))
            bc = abs(ob * (sin(base_angle)))
            ac = oc * (tan(top_angle))
            ab = str(round(ac + bc, 2))
            self.result.text = "Tree Height: " + ab

        else: # observer is lower than tree base        
            base_angle = radians(float(self.angle1.text))
            top_angle = radians(float(self.angle2.text))
            oc = ob * (cos(base_angle))
            bc = ob * (sin(base_angle))
            ac = oc * (tan(top_angle))
            ab = str(round(ac - bc, 2))
            self.result.text = "Tree Height: " + ab

class TreeApp(App):
    def build(self):
        return Grid()
    
if __name__ == "__main__":
    TreeApp().run()