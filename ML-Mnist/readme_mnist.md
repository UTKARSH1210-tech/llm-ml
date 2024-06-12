Model Architecture
The neural network model consists of two convolutional layers followed by max pooling and two fully connected layers. The first convolutional layer has 32 filters of size 3x3, and the second convolutional layer has 64 filters of size 3x3. The fully connected layers have 128 and 10 neurons respectively.

Training Process
The model is trained using the Adam optimizer with a learning rate of 0.001 and the cross-entropy loss function. The model was trained for 5 epochs on the MNIST dataset.

Results
The model is not trained fully but it is acheiving a good accuracy.

Instructions for Using the Visualization Interface
Visualize Weights:

Run the visualize_weights(model) function to see the weights of the first convolutional layer.
Interactive Prediction:


The Gradio interface demonstrating the interactive visualization.

Note : In the notebook the markdowns shows where things are done.