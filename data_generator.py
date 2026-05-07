import csv
import random


def generate_csv(filename="data.csv", rows=1050):

    headers = [
        "movie_title",
        "movie_description",
        "release_year",
        "genre",
        "actor_first_name",
        "actor_last_name",
        "role_name",
        "critic_name",
        "review_comment",
        "rating_score",
        "fact_text",
        "budget",
        "worldwide_gross"
    ]

    genres = ["Action", "Drama", "Comedy", "Thriller", "Sci-Fi", "Fantasy"]

    comments = [
        "Great movie with strong acting.",
        "Interesting plot and good visuals.",
        "The story was predictable but enjoyable.",
        "Excellent soundtrack and atmosphere.",
        "The movie has strong emotional scenes."
    ]

    facts = [
        "The movie was filmed in multiple countries.",
        "Several scenes were improvised by actors.",
        "The production used practical effects.",
        "The film received positive audience feedback.",
        "The director changed the ending during production."
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for i in range(1, rows + 1):
            budget = round(random.uniform(1_000_000, 200_000_000), 2)
            gross = round(budget * random.uniform(1.2, 5.5), 2)

            writer.writerow([
                f"Movie {i}",
                f"Description for movie {i}",
                random.randint(1980, 2025),
                random.choice(genres),
                f"ActorName{i}",
                f"ActorSurname{i}",
                f"Role {i}",
                f"Critic {i}",
                random.choice(comments),
                round(random.uniform(1, 10), 1),
                random.choice(facts),
                budget,
                gross
            ])

    print(f"CSV file '{filename}' created successfully with {rows} rows.")


if __name__ == "__main__":
    generate_csv()