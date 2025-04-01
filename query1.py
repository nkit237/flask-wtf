global_init(input())
session = create_session()
users = session.query(User).filter(User.address == 'module_1', User.speciality.notilike("%engineer%"),
                                   User.position.notilike("%engineer%")).all()
for u in users:
    print(u.id)
