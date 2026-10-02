# TODO 1: Give your robot a name.
ROBOT_NAME = "ScoutBot-X1"

# TODO 2: Describe your robot's mission.
MISSION_GOAL = "Exploring the surface of Mars for signs of water"

# TODO 3: Create a mission containing at least six commands.
# You may use: forward, backward, turn_left, turn_right, scan, beep, stop,
# and the custom command you create below.
MISSION = [
    "forward",
    "forward",
    "turn_left",
    "scan",
    "analyze_soil",
    "stop",
]

# TODO 4: Rename this command. Some ideas: dance, celebrate, wave, or recharge.
CUSTOM_COMMAND = "analyze_soil"


def custom_behavior():
    """Return a description of the student's original robot behavior."""
    # TODO 5: Replace this sentence with a description of your behavior.
    return "Analyzing soil samples"

# ============================================================
# ROBOT PROGRAM
# You do not need to change the code below for the assignment.
# ============================================================


def perform_action(action):
    """Translate one command into a description of the robot's action."""
    if action == "forward":
        return "Moving forward"
    elif action == "backward":
        return "Moving backward"
    elif action == "turn_left":
        return "Turning left"
    elif action == "turn_right":
        return "Turning right"
    elif action == "scan":
        return "Scanning the area"
    elif action == "beep":
        return "Beep boop!"
    elif action == "stop":
        return "Stopping"
    elif action == CUSTOM_COMMAND:
        return custom_behavior()
    else:
        return f"Unknown command: {action}"


def run_mission():
    """Perform the mission, display each step, and create a log file."""
    opening = f"Starting mission for {ROBOT_NAME}: {MISSION_GOAL}"
    print(opening)
    print("-" * len(opening))

    mission_log = [opening]

    for step_number, action in enumerate(MISSION, start=1):
        result = perform_action(action)
        message = f"Step {step_number}: {result}"
        print(message)
        mission_log.append(message)

    closing = "Mission complete!"
    print(closing)
    mission_log.append(closing)

    with open("mission_log.txt", "w", encoding="utf-8") as log_file:
        for message in mission_log:
            log_file.write(message + "\n")

    print("Mission log saved to mission_log.txt.")


if __name__ == "__main__":
    run_mission()
    