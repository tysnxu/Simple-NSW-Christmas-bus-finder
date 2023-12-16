import requests

import tfnsw_gtfs_realtime_pb2
import tfnsw_gtfs_realtime_pb2 as transit_realtime

with open("apiKey", "r") as f:
    apiKey = f.read()

url = "https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/buses"
headers = {"Authorization": f"apikey {apiKey}"}

response = requests.get(url, headers=headers)

feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(response.content)

matching_counter = 0

for entity in feed.entity:
    vehicle = entity.vehicle.vehicle

    if vehicle.Extensions[transit_realtime.tfnsw_vehicle_descriptor].special_vehicle_attributes == 4:
        print(f'Name: {entity.id.split("_")[-2]}, position: {entity.vehicle.position.latitude}, {entity.vehicle.position.longitude}')

        matching_counter += 1

print(f"Found {matching_counter} out of {len(feed.entity)} vehicles")
