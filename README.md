# Complete-Waste-Management-System-Udgir-City-ML-Project

Problem Statement -

Udgir is a small city with a municipal council in the Latur district, which is located in the Indian state of Maharashtra and facing one the most common problem which even most of the big Cities face which is – There is no definitive route which is followed for collection of Waste from respective areas and which often and in turn leads to waste not being collected at proper time and having really no definitive knowledge of exactly which area produce how much of Waste, for trips to be optimally scheduled 
Not enough Waste being processed out of the total waste collected. According to officials of municipality of Udgir one of the reason that this is causing is the guess work and uncertainty in the amount of waste collected next day. 

Proactively, getting an estimate of amount of Wet Waste will help officials to plan and make necessary arrangement for upcoming days. Ie. like making an compost, fertilizer etc

Data Collection – Permission and Site Visit

![image](https://user-images.githubusercontent.com/75486718/126214901-ce40f603-144f-4ded-9178-a51365a76082.png)

![image](https://user-images.githubusercontent.com/75486718/126214885-c117d865-75e8-4db9-8763-3a128e906c4f.png)

Data –  For different Wards

Sample Data in Raw format for Ward A -

![image](https://user-images.githubusercontent.com/75486718/126215006-6ce786e1-af7d-4489-90ba-2f38554c2370.png)
Similarly, there are total 4 Wards and data is present for Ward A, B, C and D

Encoded Data – In Excel. 

Making Sense of Data 

Date, Day, Ward, Vehicle Number (from where the Waste is collected from every Area)are entered as it is and then for Route we have defined specific labels. 
That means – Every Route from where the Waste is picked are set of Locations Predefined. 
Time - Recorded time at which Data is dumbed in the Ground
Waste  (Kgs ) is the waste the Vehicle brought 
Animal found in that area for that Location/Route by that Vehicle Number

Final Excel Data -

![image](https://user-images.githubusercontent.com/75486718/126215106-93f27c58-7f2a-44dd-ad3c-a715d0d40418.png)

Following is the way we defined our label for each Route -  

![image](https://user-images.githubusercontent.com/75486718/126215171-3c095086-72d0-404a-af3c-f8d5d32cd052.png)

Data Preprocessing, Data Cleaning  and EDA -

Of course, the manually entered Data had many typing errors as well the data in the raw format had null values, zeros and blank spaces which are treated
Missing Value Imputation and Data Cleaning is done (Detailed Explanation in the ipynb file)
After, the same EDA is done – Univariate and Bivariate Analysis, plots and graphs which focusses and aims at finding the pattern, distribution and type of Data 

Making Sense of the Data – Bird’s Eye View


![image](https://user-images.githubusercontent.com/75486718/126215270-131ec39d-d070-4f02-9674-4420f8728a19.png)


Using Regression Model Approach

![image](https://user-images.githubusercontent.com/75486718/126215330-a6face6e-de77-4391-a6cd-98658b79b951.png)

Classification model

![image](https://user-images.githubusercontent.com/75486718/126215386-f276ec7c-fe74-4177-a714-eb3a82ba90dd.png)


Conclusion

Given, Ward, Vehicle Number, Route, and other details we offer solution which enables any employee of the Municipality to optimize and automate planning of waste collection routes.
https://waste-estimation.herokuapp.com
Finally, we deployed the same using Flask and Heroku

Input -

![image](https://user-images.githubusercontent.com/75486718/126215456-00537614-8d46-4fa6-ac1a-92c479eae431.png)

Output -

![image](https://user-images.githubusercontent.com/75486718/126215501-ed8994d5-8bd9-4805-9004-101fa714d723.png)

Future Scope

1) Optimal Route Planning for waste collection using Operation Research Techniques 
2) Asset Management for trash bins for effective management 
3) Eventually setting up the system to – Asset Management, Waste Monitoring and Route Planning solution which can then finally be delivered to the Government as a complete end to end solution.

Note - This Project is done with authorization from Udgir Muncipal Corportaion and is for academic purpose only hence dataset cannot be shared nor distributed publicly. Above is the methodology and solution we proposed. Strictly no permission for copyright or any infringement.

















