# Affordance Highlighting project

## Project Overview

The **AML Group Project** focuses on highlighting given regions of 3D models given a prompt, using machine learning techniques. The primary implementation resides in `notebook.ipynb`, which contains the running code for executing the optimization loop, defining the loss function, and implementing the actual model used in the project. The main objective of the code is to highlight given regions in 3D models according to a specified prompt.

### Key Components:
- **refactor.ipynb**: The main execution file where the optimization process occurs. It includes:
  - The **optimization loop**, which iteratively updates the model parameters.
  - The **loss function**, used to guide the optimization.
  - The **core model implementation**, responsible for processing and improving the 3D representation.
  - **Three main parts of the project**:
    1. **Running the optimization** on the given models.
    2. **Passing from point cloud to mesh**, facilitating 3D structure generation.
    3. **Importing the AffordanceNet dataset** for further processing and analysis.
  - **Extension implementation**, which introduces additional augmentations in the processing pipeline.

- **mesh.py**: Handles the logic for managing and manipulating 3D meshes, ensuring proper structuring and transformations of the model.

- **render.py**: Responsible for rendering the 3D model, converting the optimized mesh into images. This rendering process is assisted by:
  - **utils.py**, which provides various helper functions for supporting the rendering pipeline and enhancing efficiency.

- **Normalization/**: Contains functions to normalize the rendered images according to **CLIP**. This normalization ensures that the images conform to expected input distributions, improving model performance and consistency.

This structured approach enables efficient 3D model optimization, rendering, and normalization, ensuring high-quality outputs aligned with machine learning principles while specifically focusing on highlighting relevant regions in 3D models based on a given prompt.

## Getting Started

We suggest using colab for the execution of the notebook because of the high demand of computational resources. 

All the necesary installations are executed in first cell of the notebook.

Just open the `notebook.ipnyb` file in a jupyter environment and run all the cells.

## Usage

For the first part, the code simply runs the optimization loop with a specific object and prompt, defined in the first cell under the optimization loop.

For the second part, we just left the definition of the needed functions without any cell ready to be executed.

For the third part, there is the execution cell, where the model type and prompt are defined, right under the mIOU evaluation function.

For the extension, the code resides at the bottom of the notebook, with an example with a model of scissors ready to be executed.




