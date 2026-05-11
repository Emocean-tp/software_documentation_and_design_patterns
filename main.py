import json
from reader.csv_reader import CsvReader
from strategies.console_strategy import ConsoleStrategy
from strategies.file_strategy import FileStrategy
from strategies.redis_strategy import RedisStrategy

def main():
    # читаємо конфіг
    with open("config.json") as f:
        config = json.load(f)

    # читаємо CSV
    reader = CsvReader()
    data = reader.read("data.csv")

    # 🔥 вибір стратегії ТУТ (без factory)
    strategy_type = config["strategy"]

    if strategy_type == "console":
        strategy = ConsoleStrategy()

    elif strategy_type == "file":
        strategy = FileStrategy()

    elif strategy_type == "kafka":
        strategy = KafkaStrategy()

    elif strategy_type == "redis":
        strategy = RedisStrategy(config["redis"])

    else:
        raise Exception("Unknown strategy")

    # виконання
    strategy.output(data)


if __name__ == "__main__":
    main()