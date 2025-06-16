class SummaryAgent:
    def enrich(self, input_data):
        weather = input_data.get("weather", "")
        summary = f"The next launch is {input_data['launch_name']} at {input_data['location_name']}. "
        summary += f"Current weather is '{weather}' with temperature {input_data['temperature']}°C. "
        if "rain" in weather.lower() or "storm" in weather.lower():
            summary += "Potential delay due to weather conditions."
        else:
            summary += "Launch is likely to proceed on schedule."
        return summary