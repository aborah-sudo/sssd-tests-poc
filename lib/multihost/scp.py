import os


class CopyWithScp:

    def __init__(self, hostname, user, password, local_file, remote_location):
        self.hostname = hostname
        self.user = user
        self.password = password
        self.local_file = local_file
        self.remote_location = remote_location
        os.system(f"sshpass -p {self.password}"
                  f" scp -o StrictHostKeyChecking=no {self.local_file}"
                  f" {self.user}@{self.hostname}:{self.remote_location}")


def copy_with_scp(hostname, user, password, local_file, remote_location):
    os.system( f"sshpass -p {password}"
               f" scp -o StrictHostKeyChecking=no {local_file}"
               f" {user}@{hostname}:{remote_location}")
