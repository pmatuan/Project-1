import gitlab


def login(token):
    return gitlab.Gitlab(private_token=token)
