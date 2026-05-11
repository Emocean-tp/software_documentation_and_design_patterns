from strategies.output_strategy import OutputStrategy

class ConsoleStrategy(OutputStrategy):

    def output(self, data):
        print("\n=== OUTPUT TO CONSOLE ===")
        for row in data[:10]:
            print(row)