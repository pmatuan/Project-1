import gitlab
import asyncio

from Login import login


class RepositoryController:
    def __init__(self, token):
        self.gl = login(token)

    # Xem danh sách repo
    async def listRepositories(self):
        repos = self.gl.projects.list(owned=True)
        return repos

    # Tạo mới repo
    async def createRepository(self, name, visibility):
        new_repo = self.gl.projects.create({'name': name, 'visibility': visibility})
        return new_repo

    # Xóa repo
    async def deleteRepository(self, name):
        repo = self.gl.projects.list(search=name)[0]
        self.gl.projects.delete(repo.id)

    # Liệt kê danh sách branch
    async def listBranches(self, repo_name):
        repo = self.gl.projects.list(search=repo_name)[0]
        # Trả về toàn bộ branch
        branches = repo.branches.list()
        return branches

    # Merge branch
    async def mergeBranchRequest(self, repo_name, source_branch, target_branch):
        repo = self.gl.projects.list(search=repo_name)[0]
        # check for open merge requests for the same source and target branches
        existing_merge_requests = repo.mergerequests.list(source_branch=source_branch, target_branch=target_branch,
                                                          state='opened')
        merge_request = None
        if existing_merge_requests:
            print(f"A merge request for source branch '{source_branch}' and target branch '{target_branch}' already exists.")
        else:
            # Create a merge request
            merge_request = repo.mergerequests.create({
                'source_branch': source_branch,
                'target_branch': target_branch,
                'title': f'Merging \'{source_branch}\' into \'{target_branch}\''
            })
            if merge_request.changes()['merge_status'] != 'can_be_merged':
                print(f"A merge request for source branch '{source_branch}' and target branch '{target_branch}' cannot be merged")
                merge_request.delete()
                merge_request = None
        return merge_request

    async def acceptRequest(self, merge_request):
        merge_request.merge()

    async def declineRequest(self, repo_name, merge_request_id):
        # Get the project by name
        project = self.gl.projects.list(search=repo_name)[0]

        # Delete the merge request
        project.mergerequests.delete(merge_request_id)
        print(f"Merge request {merge_request_id} deleted!")
