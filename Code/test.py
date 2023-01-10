import time
import asyncio

from RepositoryController.repo import RepositoryController
import gitlab

if __name__ == '__main__':
    repo_controller = RepositoryController('glpat-A4wxGBzLAgBxyYBueyS6')
    merge_request = repo_controller.mergeBranchRequest('NMCNPM.20221-Nhom4', 'pmatuan')
    time.sleep(3)
    merge_request.merge()
