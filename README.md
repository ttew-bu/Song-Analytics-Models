# SpotiPy_Models
This is the work behind the dataset and the model notebooks for what I want to put into the analytics webapp. I utilized the web APIs for both Genius and Spotify to get the job done. 

By the end, this repo will include my model notebooks, the data, and the scripts I used to collect the data. The final models here are going to be one that classifies a song via song attributes and another will do the same classification with lyrics. I also have a topic model in one of the workbooks that I used to generate a single label for each song so the classification could test accuracies. 

This is my first draft of the project. It was difficult to get the lyrics data to build the models, so I am in the process of trying to make an even dataset of 900-1000 songs per genre and see if I can get accuracy to improve with balanced classes. I currently only have 5 classes in the predictor due to this issue, so I am actively working to correct the song counts per genre so I can use all 8 of the final labels I created. 
