import time
from RepositoryController import RepositoryController


def main():
    repo_controller = RepositoryController('glpat-A4wxGBzLAgBxyYBueyS6')
    merge_request = repo_controller.mergeBranchRequest('ProjectOOP', 'pmatuan', 'master')
    #######################
    time.sleep(3)
    if merge_request is not None:
        repo_controller.acceptRequest(merge_request)


if __name__ == '__main__':
    main()
