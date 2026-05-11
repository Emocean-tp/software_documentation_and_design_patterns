from strategies.output_strategy import OutputStrategy
import json

class FileStrategy(OutputStrategy):

    def output(self, data):
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print("Saved to output.json")