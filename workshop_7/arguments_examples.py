def average_score(*scores):
    return sum(scores) / len(scores)


def format_message(message, *audiences, prefix="[INFO]"):
    targets = ", ".join(audiences) if audiences else "general"
    return f"{prefix} {message} -> {targets}"


def build_connection(host, *, port=5432, **credentials):
    settings = {"host": host, "port": port}
    settings.update(credentials)
    return settings


def enroll_student(name, /, *, course, level="beginner", **meta):
    record = {"name": name, "course": course, "level": level}
    record.update(meta)
    return record


if __name__ == "__main__":
    print("average:", average_score(88, 92, 79))
    print(format_message("Server restarted", "ops", "devs", prefix="[ALERT]"))
    print(build_connection("db.internal", user="admin", password="secret"))
    print(enroll_student("Nina", course="Python 101", mentor="Carlos"))
