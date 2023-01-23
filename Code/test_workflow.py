from Controller.RepositoryController import RepositoryController
from Controller.WorkflowController import WorkflowController


def main():
    repo_controller = RepositoryController('glpat-A4wxGBzLAgBxyYBueyS6')
    repo = repo_controller.getRepository('CI-CD-Project-1')
    workflow_controller = WorkflowController(repo)

    # workflow_controller.createPipeline()

    workflow_controller.stateOfPipeline(3)


if __name__ == '__main__':
    main()
