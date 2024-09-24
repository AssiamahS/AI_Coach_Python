class AICoach:
    def __init__(self, name):
        self.name = name
        self.attributes = {
            "communication": 5,
            "leadership": 5,
            "technical_skills": 5,
            "time_management": 5,
            "problem_solving": 5
        }

    def assess_employee(self, attribute):
        if attribute in self.attributes:
            return f"{self.name}'s {attribute} skill is currently at level {self.attributes[attribute]}."
        else:
            return "Attribute not found."

    def provide_feedback(self, attribute):
        feedback = {
            "communication": "Improve your communication by practicing active listening and clear articulation.",
            "leadership": "Enhance your leadership by taking initiative and motivating your team.",
            "technical_skills": "Boost your technical skills by staying updated with the latest technologies.",
            "time_management": "Improve your time management by prioritizing tasks and setting deadlines.",
            "problem_solving": "Enhance your problem-solving skills by analyzing issues and brainstorming solutions."
        }
        return feedback.get(attribute, "No feedback available for this attribute.")

    def develop_plan(self, attribute):
        plans = {
            "communication": "Attend a communication skills workshop and practice public speaking.",
            "leadership": "Take a leadership course and seek mentorship from a senior leader.",
            "technical_skills": "Enroll in an advanced technical course and work on relevant projects.",
            "time_management": "Use a planner to organize your tasks and set realistic goals.",
            "problem_solving": "Participate in problem-solving exercises and case studies."
        }
        return plans.get(attribute, "No development plan available for this attribute.")

# Example usage
employee = AICoach("John Doe")
print(employee.assess_employee("communication"))
print(employee.provide_feedback("communication"))
print(employee.develop_plan("communication"))
