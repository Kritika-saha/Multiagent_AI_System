class PlannerAgent:
    def plan(self, user_goal):
        tasks = []
        if "spacex" in user_goal.lower():
            tasks.append("spacex_agent")
        if "weather" in user_goal.lower():
            tasks.append("weather_agent")
        if "summarize" in user_goal.lower():
            tasks.append("summary_agent")
        return tasks
