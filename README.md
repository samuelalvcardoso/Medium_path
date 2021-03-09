# Medium_path

This repository contains code capable of returning an average path from several raw nmea files. The input files can have different sampling frequencies.

The work was developed by João Louro and Samuel Cardoso as a project for the Navigation Systems course at Instituto Superior Técnico using Matlab (https://github.com/fernandeslouro/gps-automatic-mapping). 

This Python implementaion aimed to be a self project proposal to increase my skills in Python scripting.
The main differences between both implementations was the path cleaning. In the Python implementation it was used a moving average filter. The results from this cleaning are presentend in the following image, being the yellow lines the raw data and the blue ones the cleaned data.

![plot](./Medium_path/moving_average_filter.png?raw=true)

This way, the final result after run the full algorithm is presented by red line:

![plot](./Medium_path/final_result.png?raw=true)


More detailed documentation (in portuguese) from the Matlab implementation can be found in documentation.pdf.
