import gitlab

from Code.Login import login


class RepositoryController:
    def __init__(self, token):
        self.gl = login(token)

    # Xem danh sách repo
    def listRepositories(self):
        repos = self.gl.projects.list(owned=True)
        return repos

    # Tạo mới repo
    def createRepository(self, name):
        new_repo = self.gl.projects.create({'name': name, 'visibility': 'public'})
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
        for branch in branches:
            print(branch.name)

    # Merge branch
    def mergeBranch(self, repo_name, branch_name):
        repo = self.gl.projects.list(search=repo_name)[0]
        merge_request = repo.mergerequests.create({
            'source_branch': branch_name,
            'target_branch': 'main',
            'title': f'Merging {branch_name} into main'
        })
        if merge_request.merge_status == "failed":
            print(f"Merge failed: {merge_request.merge_error}")

    # Từ chối merge
