# Projects
- The Jolly
- Unity
- Be sure to see other public repositories (MAUI APP, Chore Assigner, Calculator with Roman Numerals)

This Repository contains some challenge questions I encountered in Python Entry Praticitioner courses as well as Projects that are on going that I do not yet want to reveal the datasets for. 

My most recent project is a mobile application built with .NET MAUI that puts the visualizations and insights gained from below, into something I plan on using. My app predicts water visibility and provides a mechanism to record fish observations based on depth. He is a video of the app on an android emulator. The predictions are made with API calls and running through my model. API Calls are mostly on hte conditions page.

https://github.com/joerezo/Projects/assets/50391987/1eb7aeca-b160-43dc-b315-785fb356e618




For example, for these visualizations, I gathered data from the __National Oceanic Atmospheric Administration__ sensors in the Pacific Ocean. I then cleaned the data, and merged it with 8 years of organic data on water visibility in the locals. I had to transform both datasets to make sure I could run a model on it.

Initially, I wanted to use ML.NET, but I did not have enough rows for ML.NET to function (NOAA data for the specific sensor only went back until 2013, while mine went back to 2007. I had to get rid of about 300 rows leaving 400 to train with), so I used Python scikit learn to run a linear regression model. Once I verified my code worked in generating a model, I experimented with various features to determine the optimal time frame to forecast, as well as which features had the greatest effect.

This project, The Jolly, is currently private on GITHUB (as I have alot left I want to develop/pursue) but here is some of my findings:

_This visualization and linear regression equation tells me this feature is not useful for my purpose:_
![TheJolly_Tp_Sec](https://github.com/joerezo/Projects/assets/50391987/4778850c-cb46-4594-ac40-cc2d801ef476)

_This is a visualization of all of my features at once to verify I could generate a model and my code worked._ This finding also re-affirmed that I need to find other external open source data to add as features to create a better model. The search continues!
![TheJolly_LinearRegression](https://github.com/joerezo/Projects/assets/50391987/8a5e9e93-a2b9-47b7-8795-546d690a18dc)



# Unity
Other projects include learning how to use Unity. Even though it is a game development tool, I wanted to learn about it as "Unity is used for creating simulations in fields such as training, education, and research. Flight simulators, medical training modules, and physics simulations benefit from Unity’s robust engine." The Physics Major in me thoroughly enjoyed seeing physics applied in the game development!

The first video is of rigid body events before I made the boxes trigger events to be collected. Words like rigid body, kinematics, vectors are regularly used in Unity. The second video is the completed game.

https://github.com/joerezo/Projects/assets/50391987/b9713511-4749-441f-861d-8c4ecf315a44

Completed Game:



https://github.com/joerezo/Projects/assets/50391987/31c6e850-19f8-4b95-95f7-6078cb407713


