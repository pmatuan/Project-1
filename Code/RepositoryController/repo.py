import gitlab

from Login import login


class RepositoryController:
    def __init__(self, token):
        self.gl = login(token)

    # Xem danh sách repo
    def listRepositories(self):
        repos = self.gl.projects.list(owned=True)
        return repos

    # Tạo mới repo
    def createRepository(self, name, visibility):
        new_repo = self.gl.projects.create({'name': name, 'visibility': visibility})
        return new_repo

    # Xóa repo
    def deleteRepository(self, name):
        repo = self.gl.projects.list(search=name)[0]
        self.gl.projects.delete(repo.id)

    # Liệt kê danh sách branch
    def listBranches(self, repo_name):
        repo = self.gl.projects.list(search=repo_name)[0]
        # Trả về toàn bộ branch
        branches = repo.branches.list()
        return branches

    # Merge branch
    def mergeBranchRequest(self, repo_name, branch_name):
        repo = self.gl.projects.list(search=repo_name)[0]
        # check for open merge requests for the same source and target branches
        existing_merge_requests = repo.mergerequests.list(source_branch=branch_name, target_branch='main',
                                                          state='opened')
        if existing_merge_requests:
            print(f"A merge request for source branch '{branch_name}' and target branch 'main' already exists.")
            return 0
        else:
            # Create a merge request
            merge_request = repo.mergerequests.create({
                'source_branch': branch_name,
                'target_branch': 'main',
                'title': f'Merging \'{branch_name}\' into main'
            })
            return merge_request

    def acceptRequest(self, repo_name='NMCNPM.20221-Nhom4', merge_request_id=198511948):
        repo = self.gl.projects.list(search=repo_name)[0]
        merge_request = repo.mergerequests.get(merge_request_id)
        merge_request.merge()

    def declineRequest(self, repo_name='NMCNPM.20221-Nhom4', merge_request_id=0):
        # Get the project by name
        project = self.gl.projects.list(search=repo_name)[0]

        # Delete the merge request
        project.mergerequests.delete(merge_request_id)
        print(f"Merge request {merge_request_id} deleted!")
