import time

from RepositoryController import RepositoryController
from WorkflowController import WorkflowController


def main():
    repo_controller = RepositoryController('glpat-A4wxGBzLAgBxyYBueyS6')
    repo = repo_controller.getRepository('CI-CD-Project-1')
    workflow_controller = WorkflowController(repo)
    # pipeline = workflow_controller.createPipeline()
    # time.sleep(10)
    # print(workflow_controller.stateOfPipeline())
    # workflow_controller.historyPipeline()

    workflow_controller.stateOfPipeline()


if __name__ == '__main__':
    main()
