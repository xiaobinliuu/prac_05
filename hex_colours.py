color_to_code = {"aliceblue": "#f0f8ff", "amber": "#ffbf00", "aqua": "#00ffff", "barn red": "#7c0a02", "beaver":
    "#9f8170", "bistre": "#3d2b1f", "blond": "#faf0be", "blue green": "#0d98ba", "bone": "#e3dac9",
                 "bronze": "#cd7f32"}

color_choice = (input("Enter the color: ")).lower()
while color_choice != "":
    if color_choice in color_to_code:
        print(f"{color_to_code[color_choice]}")
        color_choice = (input("Enter the color: ")).lower()
    else:
        print("Invalid name")
        color_choice = (input("Enter the color: ")).lower()
