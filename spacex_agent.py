import requests

class SpaceXAgent:
    def enrich(self, input_data=None):
        res = requests.get("https://api.spacexdata.com/v5/launches/next")
        data = res.json()

        location_id = data["launchpad"]
        location_res = requests.get(f"https://api.spacexdata.com/v4/launchpads/{location_id}")
        loc_data = location_res.json()

        return {
            "launch_name": data["name"],
            "launch_time": data["date_utc"],
            "location_name": loc_data["name"],
            "lat": loc_data["latitude"],
            "lon": loc_data["longitude"]
        }