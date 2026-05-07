from models import Movie, Actor, MovieActor, Review, Rating, Fact, BoxOffice
from dal import IRepository, IFileLoader


class MovieImportService:

    def __init__(self, repo: IRepository, loader: IFileLoader):
        self.repo = repo
        self.loader = loader

    def process_data(self, file_path):

        rows = self.loader.load_csv(file_path)

        movies = {}
        actors = {}

        for row in rows:

            movie_title = row['movie_title']
            actor_key = f"{row['actor_first_name']}_{row['actor_last_name']}"

            if movie_title not in movies:

                movie = Movie(
                    title=row['movie_title'],
                    description=row['movie_description'],
                    releaseYear=int(row['release_year']),
                    genre=row['genre']
                )

                movies[movie_title] = movie
                self.repo.add(movie)

                box_office = BoxOffice(
                    movie=movie,
                    budget=float(row['budget']),
                    worldwideGross=float(row['worldwide_gross'])
                )

                self.repo.add(box_office)

            if actor_key not in actors:

                actor = Actor(
                    firstName=row['actor_first_name'],
                    lastName=row['actor_last_name']
                )

                actors[actor_key] = actor
                self.repo.add(actor)

            movie_actor = MovieActor(
                movie=movies[movie_title],
                actor=actors[actor_key],
                roleName=row['role_name']
            )

            review = Review(
                movie=movies[movie_title],
                criticName=row['critic_name'],
                comment=row['review_comment']
            )

            rating = Rating(
                movie=movies[movie_title],
                criticName=row['critic_name'],
                score=float(row['rating_score'])
            )

            fact = Fact(
                movie=movies[movie_title],
                factText=row['fact_text']
            )

            self.repo.add(movie_actor)
            self.repo.add(review)
            self.repo.add(rating)
            self.repo.add(fact)

        self.repo.commit()