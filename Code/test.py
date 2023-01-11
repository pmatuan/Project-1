import time
import asyncio

from RepositoryController.repo import RepositoryController
import gitlab


async def main():
    repo_controller = RepositoryController('glpat-A4wxGBzLAgBxyYBueyS6')
    merge_request = await repo_controller.mergeBranchRequest('ProjectOOP', 'pmatuan', 'master')
    await asyncio.sleep(3)
    if merge_request is not None:
        if merge_request.changes()['merge_status'] == 'can_be_merged':
            await repo_controller.acceptRequest(merge_request)
        else:
            print('Cannot merge')


if __name__ == '__main__':
    asyncio.run(main())
