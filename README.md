# RAY_-Right_Above_You-
Will output the 5 closest timings from current time of when the ISS (International Space Station) is right above your entered latitudes and longitudes. 

Isn't it cool if you are able to know about when recently the ISS has passed from above where you are standing or is about to come above your specified location?

Run following in your terminal (after changing your present working directory to the location where your main.py file is located) if you are not having python3 installed on your machine
```
python main.py --latitude your_latitudes --longitude your_longitudes
```
or (if you have python3 installed in your machine)
```
python3 main.py --latitude your_latitudes --longitude your_longitudes
```

Considering you are in Rajkot, Gujarat, India then your latitudes and longitudes are

**Latitudes = 22.3039** (> 0 if it is in the North of the equator or else append '-' sign before the number) <br>
**Longitudes = 70.8022** (> 0 if it is in the East of the prime meridian or else append '-' sign before the number)

My command for the sample argument will be
```
 python3 main.py --latitude 22.3039 --longitude 70.8022
```

Output will be as follows for sample data 
```
2020-02-17 05:38:43
2020-02-17 07:10:31
2020-02-17 08:48:53
2020-02-17 15:24:41
2020-02-17 17:00:35
```
