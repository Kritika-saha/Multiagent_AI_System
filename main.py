from agents.planner_agent import PlannerAgent
from agents.spacex_agent import SpaceXAgent
from agents.weather_agent import WeatherAgent
from agents.summary_agent import SummaryAgent
from dotenv import load_dotenv
import os

load_dotenv()

def main(user_goal):
    planner = PlannerAgent()
    tasks = planner.plan(user_goal)

    agent_map = {
        "spacex_agent": SpaceXAgent(),
        "weather_agent": WeatherAgent(),
        "summary_agent": SummaryAgent()
    }

    data = None
    for task in tasks:
        agent = agent_map[task]
        data = agent.enrich(data)

    print("\nFINAL OUTPUT:", data)

if __name__ == "__main__":
    goal = input("Enter your goal: ")
    main(goal)