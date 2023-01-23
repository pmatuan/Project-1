import base64


class WorkflowController:
    def __init__(self, repo):
        self.repo = repo

    # Xem trạng thái workflow mới nhất của repo
    def stateOfPipeline(self, quantity):
        pipelines = self.repo.pipelines.list(get_all=True)
        for pipeline in pipelines[0:quantity+1]:
            for job in pipeline.jobs.list():
                print(f'Pipeline {pipeline.id} {pipeline.status}')
                print(f"Job: {job.name} {job.status}")
                print(f"Job Web URL: {job.web_url}")
            print("\n\n")

    # Lấy file .gitlab-ci.yml
    def getConfig(self):
        ci_config = self.repo.files.get(file_path='../.gitlab-ci.yml', ref='main')
        content = base64.b64decode(ci_config.content).decode("utf-8")
        content = content.replace('\\n', '\n')
        return content

    # Sửa file .gitlab-ci.yml
    def editConfig(self, new_content):
        ci_config = self.repo.files.get(file_path='../.gitlab-ci.yml', ref='main')
        encoded_content = base64.b64encode(new_content.encode()).decode()
        self.repo.files.update(file_path='../.gitlab-ci.yml', ref='main', content=encoded_content,
                               last_commit_sha=ci_config.sha)
        self.repo.commits.create(ref='main', message='Update .gitlab-ci.yml', actions=[{
            'action': 'update',
            'file_path': '.gitlab-ci.yml',
            'content': encoded_content
        }])

    # Tạo pipeline !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def createPipeline(self):
        pipeline = self.repo.pipelines.create({'ref': 'main'})
        print('Create pipeline successfully')
        return pipeline

    # Chạy pipeline: có vẻ đang thừa, vì khi create nó tự chạy
    def runPipeline(self, pipeline):
        # ?
        pipeline.play()

    # Hủy pipeline
    def cancelPipeline(self, pipeline):
        pipeline.cancel()
        print('Cancelled pipeline successfully')

    def historyPipeline(self):
        pipelines = self.repo.pipelines.list()
        for pipeline in pipelines:
            print("Pipeline ID: ", pipeline.attributes['id'])
            print("Ref: ", pipeline.attributes['ref'])
            print("Status: ", pipeline.attributes['status'])
            print("------")
