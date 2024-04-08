#Proyecto 3er Periodo

import json
from flet import App, Text, VBox, Button, TextInput, FileDialog

class TeacherSurveyApp:
    def __init__(self):
        self.strategies = []

        self.app = App(
            title="Teaching Strategies App",
            layout=VBox(
                Text("Survey Section"),
                TextInput("What is the current problem that could be solved with an app?", id="problem"),
                TextInput("What features should the app have?", id="features"),
                TextInput("How big do you expect the impact of this application to be?", id="impact"),
                Button("Submit", on_click=self.submit_survey),

                Text("App Section"),
                Text("Teaching Strategies App"),
                FileDialog("Load Strategies", on_click=self.load_strategies),
                Button("Export as PDF", on_click=self.export_to_pdf)
            )
        )

    def submit_survey(self, data):
        problem = data["problem"]
        features = data["features"]
        impact = data["impact"]

        survey_data = {
            "problem": problem,
            "features": features,
            "impact": impact
        }

        with open("survey_data.json", "w") as file:
            json.dump(survey_data, file)

    def load_strategies(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.strategies = json.load(file)

            # Update the UI or perform other actions with loaded strategies
            print("Strategies loaded:", self.strategies)

        except FileNotFoundError:
            print("Teaching strategies file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON file.")

    def export_to_pdf(self):
        # Implement PDF export functionality (you can use a library like ReportLab)
        print("Exporting to PDF...")

    def run(self):
        self.app.run()

if __name__ == "__main__":
    app = TeacherSurveyApp()
    app.run()
