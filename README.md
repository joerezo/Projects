# Projects
This Repository contains some challenge questions I encountered in Python Entry Praticitioner courses as well as Projects that are on going that I do not yet want to reveal the datasets for. 

For example, for these visualizations, I webscraped data from the National Oceanic Atmospheric Administration sensors in the Pacific Ocean. I then cleaned the data, and merged it with 8 years of organic data on water visibility in the locals. I had to transform both datasets to make sure I could run a model on it.

Initially, I wanted to use ML.NET, but I did not have enough rows for ML.NET to function, so I used Python scikit learn to run a linear regression model. Once I verified my code worked in generating a model, I experimented with various features to deteremine the optimal time frame to forecast, as well as which features had the greatest effect.

This project, The Jolly, is currently private on GITHUB (as I have alot left I want to develop/pursue) but here is some of my findings:

This visualization and linear regression equation tells me this feature is not useful for my purpose:
![TheJolly_Tp_Sec](https://github.com/joerezo/Projects/assets/50391987/4778850c-cb46-4594-ac40-cc2d801ef476)

This is a visualization of all of my features at once to verify I could generate a model and my code worked.
![TheJolly_1hrData](https://github.com/joerezo/Projects/assets/50391987/0125d67b-77d2-4775-871d-60a5285b1f0b)

This feature is more useable, but the r^2 value is still low, but from the added data from NOAA, was one of my better features. This finding also re-affirmed that I need to find other external open source data to add as features to create a better model. The search continues!
![TheJolly](https://github.com/joerezo/Projects/assets/50391987/6f5cac01-0a99-4f99-897a-38b79f456d3f)
