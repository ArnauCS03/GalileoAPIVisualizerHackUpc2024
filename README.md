# Galileo API Visualizer. HackUpc 2024

Challenge of the European Space Agency's HackUPC 2024. The main challenge was to develop an Android app that gathers information about the satellite Galileo, and sends it to a database ([*influxDB*](https://www.influxdata.com/)) using our own API. And with that information, show it graphically using the plots of the web app [*Grafana*](https://grafana.com).    
---

<br>**Authors:**
- Arnau Claramunt
- Pau Rambla
- Gleb Semenov
---
<br>
Also, it was important after showing the results, help aswer some questions of the challenge:<br><br>
- How many Galileo satellites are used on your phone?<br>
- How is Galileo contributing to your position accuracy?<br> 
- Are the signals being altered?<br>

<br>
<p float="left">
  <img src="https://github.com/ArnauCS03/GalileoESAHackUpc2024/assets/95536223/f3cedaef-2fe2-4415-8418-ea24fe2268da" width="400" height="400" />
  <img src="https://github.com/ArnauCS03/GalileoESAHackUpc2024/assets/95536223/944b9d8a-b801-44ec-a7f1-0b80780c318f" width="400" height="400" />
</p>
<br>
Graphical interface and plots made with (Frontend):<br><br>
<p float="center">
 <img src="https://github.com/ArnauCS03/GalileoESAHackUpc2024/assets/95536223/29050e04-2d11-44af-a7ae-9aad010d2819" />
</p>

<br>
To obtain the data (.logs) we used the GNSS Logger Google app in order to read the GPS/GNSS raw measurement signals of the satellites.<br><br>

![androidGNSS](https://github.com/ArnauCS03/GalileoESAHackUpc2024/assets/95536223/62b1412b-e38f-4eab-b348-83cec5af0c4e)<br><br>

GNSS (Global Navigation Satellite System) is continuously transmitting navigation signals in two 
or more frequencies and some apps can get a record of them.<br><br>

---

### API
The API was made in Python using [Flask](https://flask.palletsprojects.com/en/3.0.x/) and the data in format json.<br><br> 
![flask](https://github.com/ArnauCS03/GalileoESAHackUpc2024/assets/95536223/ca8e5948-e79a-436e-be50-de7c55732b9c)<br>


### Results<br>
This are some screenshots about how would look our partial implementation.<br><br>

![Screenshot from 2024-05-05 04-08-23](https://github.com/ArnauCS03/GalileoESAHackUpc2024/assets/95536223/678d2942-b8c9-489e-95d4-fffece762234)<br><br>

![Screenshot from 2024-05-05 04-28-53](https://github.com/ArnauCS03/GalileoESAHackUpc2024/assets/95536223/f92462e0-bc6a-4f1b-a097-2b7cf4af334d)<br><br>



We end up experimenting and setting up new tools rather than finishing the complete challenge.<br><br>
