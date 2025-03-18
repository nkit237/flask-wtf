from data import db_session
from data.jobs import Jobs
from faker import Faker

fake = Faker()


def main():
    db_session.global_init("db/mars_explorer.db")

    session = db_session.create_session()

    job = Jobs(
        team_leader=1,
        job='deployment of residential modules 1 and 2',
        work_size=15,
        collaborators='2, 3',
    )
    session.add(job)
    session.commit()


if __name__ == '__main__':
    main()
