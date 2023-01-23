import time

from Login import login


class RepositoryController:
    def __init__(self, token):
        self.gl = login(token)

    # Xem danh sách repo
    def listRepositories(self):
        repos = self.gl.projects.list(owned=True)
        return repos

    def getRepository(self, name):
        return self.gl.projects.list(search=name)[0]

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
    def mergeBranchRequest(self, repo_name, source_branch, target_branch):
        repo = self.gl.projects.list(search=repo_name)[0]
        # kiểm tra merge requests đã tồn tại hay chưa
        existing_merge_requests = repo.mergerequests.list(source_branch=source_branch, target_branch=target_branch,
                                                          state='opened')
        merge_request = None
        if existing_merge_requests:
            print(
                f"A merge request for source branch '{source_branch}' and target branch '{target_branch}' already exists.")
        else:
            # Tạo merge request
            merge_request = repo.mergerequests.create({
                'source_branch': source_branch,
                'target_branch': target_branch,
                'title': f'Merging \'{source_branch}\' into \'{target_branch}\''
            })
            time.sleep(2)
            # Nếu không thể tự động merge (tồn tại conflict, merge request không thay đổi ...)
            if merge_request.changes()['merge_status'] != 'can_be_merged':
                print(
                    f"A merge request for source branch '{source_branch}' and target branch '{target_branch}' cannot be merged due to {merge_request.changes()['merge_status']}")
                merge_request.delete()
                merge_request = None
        return merge_request

    def acceptRequest(self, merge_request):
        merge_request.merge()
        print(f"Merge request '{merge_request.title}' has been accepted")

    def declineRequest(self, merge_request):
        merge_request.delete()
        print(f"Merge request '{merge_request.title}' has been declined")
