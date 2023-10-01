"# Hand-Digit-Gesture-Identification" 

This is a basic hand gesture identification project which uses mediapipe and opencv along with machine learning to recognise hand gesture
made by the user.

Requirements:
Numpy 
Matplotlib
Pandas
Scikit-Learn
Opencv
Mediapipe
PIL
csv

## Hand Gesture Identification.ipynb - 
            Run this file to record the coordinates of hand gesture of your hand and record it in the file.
            You can make any gesture and record it in the csv file. However you have to tweak/change the code 
            to assign the coordinates with the labels. You can also do that manually.

            Next import the csv file after completion of recording of coordinates using pandas. Split the dataset
            into training and testing.

            I have choosen random forest to train the model. Feel free to use any other model of your choice.

            Finally save the model using pickle.

## Coords.csv - Coordinates of hand gestures: 
            There are 21 landmarks on hands along in x,y,z axis along with label of the gesture.

## Hand Gesture Identification - 
            This python file detects your hand and reads the landmark of your gesture. Next it imports the saved model 
            and then predicts the gesture based on the positions of your landmarks.


### Feel free to play around with the project - record your own random hand gesture like sign language and have fun!
