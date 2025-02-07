# Project-1 Myth Busting
## Slack Channel
Join our Slack channel for project discussions and updates:
- Channel: #404-not-found
- Link: [404 Not Found](https://aiptwestnovem-cki2893.slack.com/archives/C089LSTUQER)

## Team Members
- Tiffany Jimenez
- Sam Lara
- Matthew Lundberg
- Jason Smoody
- Erin, Spencer-Priebe 

 ## Todo List
 [Git Project Board](https://github.com/users/mattlundberg/projects/1)
 ## Project Milestones

| Milestone | Due Date | Status |
|----------|----------|----------|
| Project Ideation | 1/23/25 | Complete |
| Git Project Creation | 1/23/25 | Complete |
| Data Fetching | 1/23/25 | Complete |
| Data Exploration | 1/27/25 | Complete |
| Data Transformation | 1/28/25 | Complete |
| Data Analysis | 1/30/25 | Complete |
| Testing | Ad Hoc | Complete |
| Create Documentation | 2/3/25 | Conplete |
| Create Presentation | 2/5/25 | Complete |

 ## Proposal
  Emergency calls of service and how they correlate to lunar cycles and planetary alignment. (We are measuring the increase of crazy).\
  This research aims to explore the potential relationship between celestial events, such as lunar cycles, eclipses, and planetary alignments, and fluctuations in the frequency of emergency calls for service. While anecdotal evidence and cultural beliefs suggest a link between "crazy" behavior and events like full moons or eclipses, this study seeks to examine these claims empirically using robust data analysis.
 - Does the number of emergency calls increase during a full moon?
   - Jason Smoody
   - jasons_full_moon_analysis.ipynb
 - Does the number of emergency calls increase during a new moon?
   - Tiffany Jimenez
   - TiffanyJ_NewMoon_Analysis.ipynb
 - Does the number of emergency calls increase during a partial solar eclipse?
 - Does the number of emergency calls increase during a partial lunar eclipse?
   - Sam Lara
   - Sam_Code.ipynb
 - Does the number of emergency calls increase during a total solar eclipse?
   - Matthew Lundberg
   - Matt_Lundberg_TLE.ipynb
 - Does the number of emergency calls increase during a planetary alignment?
   - Erin Spencer-Priebe
   - Erin_Spencer-Priebe_Mercury_Analysis.ipynb

## Slide Deck
[Superstitions in the Medical Field](https://docs.google.com/presentation/d/1UD1OkDFYxhyvThd9G9IcABsh1DPIvl7xYfk4pEMAzOQ/edit?usp=sharing)

## Data sets
Planetary Data Sets
 - https://www.timeanddate.com/eclipse/list.html?starty=2020
 - Nasa sources
 - merc_retro.csv (manually generated list of dates)

 Emergency Calls of Service From Phoenix, AZ
 - https://www.phoenixopendata.com/dataset/caf49f72-f22f-4ad9-9405-2a3db9619423/resource/45b13b01-d1c5-4159-b313-8d409dd431cb/download/calls-for-service-fire_calls-for-service-2019_calls-for-service.csv
 - https://www.phoenixopendata.com/dataset/caf49f72-f22f-4ad9-9405-2a3db9619423/resource/d0164e0f-8af4-4bbe-99f6-f952717aaf36/download/calls-for-service-fire_calls-for-service-2020_cfs2020.csv
 - https://www.phoenixopendata.com/dataset/caf49f72-f22f-4ad9-9405-2a3db9619423/resource/6b57764d-bb95-4c1e-85b3-77e3d0f14841/download/calls-for-service-fire_calls-for-service-2021_calls-for-service.csv
 - https://www.phoenixopendata.com/dataset/caf49f72-f22f-4ad9-9405-2a3db9619423/resource/f32a4ba0-0c18-45eb-b0c7-4d46170fbcb9/download/calls-for-service-fire_calls-for-service-2022_cfs2022.csv
 - https://www.phoenixopendata.com/dataset/caf49f72-f22f-4ad9-9405-2a3db9619423/resource/e832854c-6537-4223-ba26-674a7b799f49/download/calls-for-service-fire_calls-for-service-2023_calls-for-service.csv
 - https://www.phoenixopendata.com/dataset/caf49f72-f22f-4ad9-9405-2a3db9619423/resource/2169fba5-a64a-42da-893d-931b97ea10ef/download/calls-for-service-fire_calls-for-service-2024_calls_for_service.csv

# Program Information 
## Program Information
- Starting File: datachecker.ipynb

### Programming Languages
- Python 3.x

### Required Libraries/Dependencies
- Jupyter Notebook
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

### Development Environment
- Jupyter Notebook/JupyterLab for interactive data analysis
- Git for version control
- VS Code (optional)

### Data Files
- CSV files containing emergency call data (2019-2023)
- CSV files containing celestial event data:
  - Mercury retrograde periods
  - Full moon dates and types
  - New moon dates

### Project Structure
- /Resources: Contains all raw data files
- /notebooks: Jupyter notebooks for analysis
- README.md: Project documentation

### Overview and Analysis
#### Proposal
It is a common belief in emergency services that celestial events impact human behavior. This research aims to explore the potential relationship between lunar cycles, eclipses, and Mercury retrograde periods and the frequency of emergency calls.

While anecdotal evidence suggests a link between "unusual" behavior and celestial events, this study seeks to examine these claims empirically using robust data analysis techniques. By systematically investigating the correlation between emergency service demands and specific astronomical phenomena, we aim to provide a scientific perspective on these long-standing cultural beliefs.

#### Does the number of calls increase during a new moon?

Conclusion: No

The p-value is much greater than the common threshold of 0.05, indicating that the observed difference in incident counts between new moon and non-new moon days is not statistically significant. Any difference observed is likely due to random chance rather than an actual effect of the new moon.

![image](https://github.com/user-attachments/assets/a9ef79f9-c57b-4814-979c-9a4cea9dcf99)

#### Does the number of calls increase during a full moon?

Conclusion: No

This graph doesn't show any visible relationship between full moon day incidents vs non-full moon incidents.  There one spike, in 2022 where the full moon day had more incidents.

![image](https://github.com/user-attachments/assets/5a0b8679-21c8-4834-a442-1f7babd73cc4)

#### Does the number of calls increase during a partial solar/lunar eclipse?

Conclusion: No

- The total number of emergency calls between 2019 - 2024 was: 1,150,331
- The total number of emergency calls during a partial solar eclipse is: 598
- The total number of emergency calls during a partial solar eclipse is: <1%
- The total number of emergency calls between 2019 - 2024 was: 1,150,331
- The total number of emergency calls during a partial lunar eclipse is: 4,497
- The total number of emergency calls during a partial lunar eclipse is: <1%


It appears that the data does not support the hypothesis of the level of emergency calls increasing during a partial solar or lunar eclipse.

![image](https://github.com/user-attachments/assets/943d4ad2-3351-4d68-8d48-77889e77cdad)

![image](https://github.com/user-attachments/assets/e38e0fb9-ce05-4224-b9c5-21d7b3142677)

#### Does the number of calls increase during a total lunar eclipse?

Conclusion: No

Daily Analysis
- Average incidents on eclipse days: 630.03
- Average incidents on non-eclipse days: 614.29
- Percent difference: -2.50%

The nearly identical averages (just -2.50% difference) suggests that the occurrence of a total lunar eclipse has no impact on the daily volume of emergency incidents.

Hourly Analysis  
- Average incidents during eclipse hours: 26.29
- Average incidents during non-eclipse hours: 26.25
- Percent difference: 0.14%

Looking at the specific hours when eclipses occurred also shows virtually no difference (only 0.14%) compared to non-eclipse hours.

![image](https://github.com/user-attachments/assets/2f72c5ab-5ca2-4d9e-b467-98afc2e527ef)

#### Does the number of calls increase during mercury retrograde?

Conclusion: No

- Correlation between incident count and retrograde periods: 0.0411
- Correlation for 2019: 0.1084
- Correlation for 2020: 0.2956
- Correlation for 2021: -0.1126
- Correlation for 2022: -0.0041
- Correlation for 2023: -0.0508

![image](https://github.com/user-attachments/assets/64ca4ded-c769-49a6-827a-128d3016ef43)
