"""
created by Nagaj at 29/05/2021
"""
from data import groups
from group import Group
from user import UserProfile


def main():
    # john = UserProfile(name="john", phone='+20127111234')  # validation error
    john = UserProfile(name="john", phone='+201271112345')
    print(john)

    # john = UserProfile(name="testtesttesttesttesttesttesttesttesttesttesttest", phone='+201271112345')
    for group in groups:
        grp = Group(name=group["name"])
        john.join_group(grp)

    print(john.groups)
    print(len(john))
    # ###############################
    # devops, backend, python_export, automation, agile = [Group(group["name"]) for group in groups]
    # print(devops)
    # print(john in devops)
    print(john in grp)  # True
    print(len(grp))  # 1 means: grp contains only one member <john>
    print("#" * 100)
    for group in john:
        print(group)
    print("#" * 100)
    for member in grp:
        print(member)
    print("#" * 100)
    john.leave_group(grp)  # left
    print(john in grp)  # False
    print(len(grp))  # 0: after john left, there is no members


if __name__ == '__main__':
    main()
