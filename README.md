# FractalTreeGenerator
Python program built using PyQt and NumPy that allows you to create and visualize fractal trees through a graphical user interface (GUI). The program empowers users to experiment with various fractal tree parameters, observe real-time visualizations of their changes, and export the generated fractal trees as images. This interactive GUI provides a comprehensive platform to explore the beauty and complexity of fractal geometry.

<img src="https://github.com/milckywayy/FractalTreeGenerator/assets/120181288/164673af-317a-45b4-9dda-981120424fad" alt="Recording" height="240">
<img src="https://github.com/milckywayy/FractalTreeGenerator/assets/120181288/0ab22166-0f62-4bba-ae50-eef5179c2884" alt="Image 1" height="240">
<img src="https://github.com/milckywayy/FractalTreeGenerator/assets/120181288/ca1a41ae-1a58-4214-a3ae-c7747a853f86" alt="Image 2" height="240">


## Features:
- Interactive GUI: The program offers an intuitive graphical interface that enables users to adjust parameters and visualize the changes in real-time. PyQt is utilized to create a user-friendly experience.
- Fractal Tree Generation: The core functionality revolves around generating fractal trees. The trees are composed of branches recursively branching out from a root. Users can modify parameters such as the number of iterations, angle differences, number of branches, branch length, and more.
- Parameter Customization: The GUI provides sliders, input boxes, and color pickers to customize various attributes of the fractal trees, including colors, angles, and dimensions. Users can instantly observe how changes affect the final tree.
- Dynamic Color Fade: Users can enable or disable a dynamic color fade effect, which gradually transitions the color of the branches from the tree color to a fade color as the iterations progress. This effect adds depth and visual appeal to the generated trees.
- Real-Time Visualization: Any modifications to the parameters are immediately reflected in the displayed fractal tree, allowing users to fine-tune their creations visually.
- Export as Image: Once satisfied with their fractal tree, users can export the generated image as a PNG file. This feature enables users to save and share their unique creations.
- Code Integration: The program's logic is encapsulated within a class called FractalGenerator. This separation of concerns makes it possible to integrate the fractal generation capabilities into larger projects, if desired.

## Usage:
- Clone the repository and navigate to the project directory.
- Install the required libraries (PyQt, NumPy, OpenCV).
- Run the program by executing the script.
- The GUI window will open, showcasing the generated fractal tree.
- Interact with the sliders, input boxes, and color pickers to customize the parameters.
- Observe the real-time changes in the displayed fractal tree.
- Click the "Export Image" button to save your fractal creation as a PNG image.
