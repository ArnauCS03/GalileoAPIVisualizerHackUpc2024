from influxdb import InfluxDBClient

# Connect to InfluxDB
client = InfluxDBClient(host='127.0.0.1', port=8086, username='ArnauCS', password='1df2b623f2f3a33c', database='fullfocus')

# Sample data
data = [
    {
        "measurement": "galileo_data",
        "tags": {},
        "fields": {
            "latitude_degrees": 12.34,
            "longitude_degrees": 56.78
        }
    }
]

# Write data to InfluxDB
client.write_points(data)